import urllib3
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from decouple import config
from core.shared.models import AppBaseException


class CantGetMediumFeed(AppBaseException):
    msg = "Can't get Medium feed."


class MediumContentParser(HTMLParser):
    header_img_src = ""

    def __init__(self):
        HTMLParser.__init__(self)
        self.HTMLDATA = []

    def handle_starttag(self, tag, attrs):
        if tag == 'img':
            attrs_map = dict((key, value) for key, value in attrs)

            if attrs_map['alt'] == 'Header':
                self.header_img_src = attrs_map['src']

    def handle_data(self, data):
        self.HTMLDATA.append(data.strip())

    def clean(self):
        self.HTMLDATA = []


class MediumScraper():
    @staticmethod
    async def get_medium_feed():
        account_name = config('MEDIUM_ACCOUNT')
        rss_url = f'https://medium.com/feed/@{account_name}'
        xml_namespaces = {'dc': 'http://purl.org/dc/elements/1.1/',
                          'content': 'http://purl.org/rss/1.0/modules/content/'}

        content_parser = MediumContentParser()
        http = urllib3.PoolManager()
        response = http.request('GET', rss_url)

        filtered_output = []

        if response.status != 200:
            raise CantGetMediumFeed()

        xml_tree = ET.fromstring(response.data)

        for element in xml_tree.iter('item'):
            content_parser.feed(element.find('content:encoded', xml_namespaces).text)

            parsed_content = ' '.join(content_parser.HTMLDATA)
            header_img_src = content_parser.header_img_src
            content_parser.clean()

            categories = [item.text for item in element.findall('category')]
            filtered_categories = categories.copy()

            if 'english' in categories:
                filtered_categories.remove('english')

                filtered_element = {
                    'title': element.find('title').text,
                    'img': header_img_src,
                    'guid': element.find('guid').text,
                    'tags': filtered_categories,
                    'pubDate': element.find('pubDate').text,
                    'content': parsed_content
                }

                filtered_output.append(filtered_element)

        content_parser.close()

        return filtered_output
