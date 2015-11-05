from interwiki import RegExTranslator
from interwiki import translator
import re


@translator('https://([^/]*).readthedocs.org/')
class Boost(RegExTranslator):

    def __init__(self, re):
        self.re = re

    def __call__(self, url):
        what = re.match(
            r'https://([^/]*).readthedocs.org/([^/]*)/[^/]*/(.*)',
            url
        )

        return 'https://{}.readthedocs.org/{}/latest/{}'.format(
                what.group(1), what.group(2), what.group(3)
        )
