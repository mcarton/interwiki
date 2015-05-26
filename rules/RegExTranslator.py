import re


class RegExTranslator:
    def match(self, url):
        return re.search(self.re, url)
