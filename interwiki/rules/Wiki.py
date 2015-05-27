from interwiki import translator
from interwiki.rules import RegExTranslator
import json
import re
import requests


def get_only_in_map(map):
    return next(iter(map.values()))


def lang(from_lang):
    return 'fr' if from_lang == 'en' else 'en'


@translator(r'https?://..\.wikipedia.org/wiki/.*')
@translator(r'https?://..\.wiktionary.org/wiki/.*')
class Wiki(RegExTranslator):

    def __init__(self, re):
        self.re = re

    def get_article(url):
        m = re.search(r'https?://(..)\.(.*)\.org/wiki/([^#]*)(#.*)?', url)
        return (m.group(1), m.group(2), m.group(3))

    def get_link(from_lang, site, article):
        to_lang = lang(from_lang)
        url = (
           'https://%s.%s.org/w/api.php'
           '?action=query&continue&format=json'
           '&prop=langlinks&titles=%s&lllang=%s'
        ) % (from_lang, site, article, to_lang)

        j = json.loads(requests.get(url).text)

        n = get_only_in_map(j['query']['pages'])['langlinks'][0]['*']

        return 'https://%s.%s.org/wiki/%s' % (to_lang, site, n)

    def __call__(self, url):
        (from_lang, site, article) = Wiki.get_article(url)
        return Wiki.get_link(from_lang, site, article)
