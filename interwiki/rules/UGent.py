from interwiki import translator
from interwiki.rules import RegExTranslator


@translator(r'https?://(.*\.)?ugent.be/.*')
class UGent(RegExTranslator):

    def __init__(self, re):
        self.re = re

    def __call__(self, url):
        url = url.split('/')

        if url[-2] != 'en':
            url[-1:-1] = ('en',)
        else:
            del url[-2]

        return '/'.join(url)
