from dataclasses import dataclass

import urllib3
import xml.etree.ElementTree as ET
from core.shared.models import AppBaseException
from core.shared.ports import MediumContentParserPort


class CantGetMediumFeed(AppBaseException):
    msg = "Can't get Medium feed."


@dataclass
class MediumScraper:
    account_name: str
    medium_content_parser: MediumContentParserPort

    async def get_medium_feed(self):
        rss_url = f"https://medium.com/feed/@{self.account_name}"
        xml_namespaces = {
            "dc": "http://purl.org/dc/elements/1.1/",
            "content": "http://purl.org/rss/1.0/modules/content/",
        }

        http = urllib3.PoolManager()
        response = http.request("GET", rss_url)

        filtered_output = []

        if response.status != 200:
            raise CantGetMediumFeed()

        xml_tree = ET.fromstring(response.data)

        for element in xml_tree.iter("item"):
            content_parser = self.medium_content_parser
            content_parser.feed(element.find("content:encoded", xml_namespaces).text)

            parsed_content = "".join(content_parser.HTMLDATA)

            categories = [item.text for item in element.findall("category")]
            filtered_categories = categories.copy()

            if "english" in categories:
                filtered_categories.remove("english")

                filtered_element = {
                    "title": element.find("title").text,
                    "subtitle": content_parser.subtitle,
                    "img": content_parser.header_img_src,
                    "guid": element.find("guid").text,
                    "tags": filtered_categories,
                    "pubDate": element.find("pubDate").text,
                    "content": parsed_content,
                }

                filtered_output.append(filtered_element)

            content_parser.clean()
            content_parser.close()

        return filtered_output
