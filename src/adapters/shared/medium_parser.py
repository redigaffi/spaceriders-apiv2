from html.parser import HTMLParser
from core.shared.ports import MediumContentParserPort


class MediumContentParser(MediumContentParserPort, HTMLParser):
    header_img_src = ""
    subtitle = ""
    start_tags_to_space = []
    end_tags_to_space = ['h1', 'h2', 'h3', 'h5', 'h6', 'p', 'blockquote', 'li']
    tags_to_avoid = ['h4']

    def __init__(self):
        HTMLParser.__init__(self)
        self.HTMLDATA = []

    def handle_starttag(self, tag, attrs):
        if tag == 'img':
            attrs_map = dict((key, value) for key, value in attrs)

            if attrs_map['alt'].lower() == 'header':
                self.header_img_src = attrs_map['src']
            else:
                if self.header_img_src == '':
                    self.header_img_src = attrs_map['src']

        if tag in self.start_tags_to_space:
            self.HTMLDATA.append(' ')

    def handle_endtag(self, tag):
        if tag in self.end_tags_to_space:
            self.HTMLDATA.append(' ')

        if tag in self.tags_to_avoid:
            deleted_data = self.HTMLDATA.pop()
            if tag == "h4":
                self.subtitle = deleted_data

    def handle_data(self, data):
        self.HTMLDATA.append(data)

    def clean(self):
        self.HTMLDATA = []
