from interwiki import RegExTranslator
from interwiki import translator
import re


@translator(r'https://www\.google\.[^\.]*/.*')
class Google(RegExTranslator):

    def __init__(self, re):
        self.re = re

    def __call__(self, url):
        m = re.search(r'https://www\.google\.[^/]*/(.*)', url)
        return 'https://www.google.com/{}'.format(m.group(1))
