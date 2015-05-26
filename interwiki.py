#!/usr/bin/env python

import codecs
import json
import re
import urllib.request
import sys


class RegExTranslator:
    def match(self, url):
        return re.search(self.re, url)


class StartsWithTranslator:
    def match(self, url):
        if url.startswith('http://'):
            url = url[len('http://'):]
        elif url.startswith('https://'):
            url = url[len('https://'):]

        return url.startswith(self.begin)


class Wiki(RegExTranslator):

    def __init__(self, re):
        self.re = re

    def get_only_in_map(map):
        return next(iter(map.values()))

    def get_article(url):
        m = re.search(r'https?://(..)\.(.*)\.org/wiki/([^#]*)(#.*)?', url)
        return (m.group(1), m.group(2), m.group(3))

    def lang(from_lang):
        return 'fr' if from_lang == 'en' else 'en'

    def get_link(from_lang, site, article):
        to_lang = Wiki.lang(from_lang)
        url = (
           'https://%s.%s.org/w/api.php'
           '?action=query&continue&format=json'
           '&prop=langlinks&titles=%s&lllang=%s'
        ) % (from_lang, site, article, to_lang)

        h = urllib.request.urlopen(url)
        utf8reader = codecs.getreader("utf-8")
        j = json.load(utf8reader(h))

        n = Wiki.get_only_in_map(j['query']['pages'])['langlinks'][0]['*']

        return 'https://%s.%s.org/wiki/%s' % (to_lang, site, n)

    def __call__(self, url):
        (from_lang, site, article) = Wiki.get_article(url)
        return Wiki.get_link(from_lang, site, article)


class Xkcd(StartsWithTranslator):
    begin = 'xkcd.com/'

    def __call__(self, url):
        number = re.search(r'https?://xkcd.com/(.*)/', url)

        if number:
            return 'http://explainxkcd.com/%s/' % (number.group(1))
        else:
            return 'http://explainxkcd.com/'


class Boost(StartsWithTranslator):
    begin = 'www.boost.org/doc/libs/'

    def __call__(self, url):
        what = re.match(r'http://www.boost.org/doc/libs/[\d_]*/(.*)', url)

        return 'http://www.boost.org/doc/libs/release/' + what.group(1)


class Java(RegExTranslator):
    re = r'https?://docs.oracle.com/javase/.*/docs/api/.*'

    def __call__(self, url):
        what = re.match(
            r'https?://docs.oracle.com/javase/.*/docs/api/(.*)', url
        )

        return 'https://docs.oracle.com/javase/8/docs/api/' + what.group(1)


class Why3(RegExTranslator):
    re = r'https?://why3.lri.fr/(doc|stdlib)-.*'

    def __call__(self, url):
        what = re.match(
            r'http(s?)://why3.lri.fr/(doc|stdlib)-[^/]*/(.*)', url
        )

        return 'http{}://why3.lri.fr/{}-0.85/{}'.format(
            what.group(1), what.group(2), what.group(3)
        )


class Python(StartsWithTranslator):
    begin = 'docs.python.org/'
    (major, minor) = sys.version_info[:2]

    def __call__(self, url):
        what = re.match(r'https?://docs.python.org/[\d.]*/(.*)', url)

        return 'https://docs.python.org/%s.%s/%s' \
            % (self.major, self.minor, what.group(1))


class GitHub(StartsWithTranslator):
    begin = 'github.com/'

    def __call__(self, url):
        what = re.match(r'https?://github.com/([^/]*)/([^/]*)', url)

        api_url = 'https://api.github.com/repos/{}/{}'.format(
            what.group(1), what.group(2)
        )
        api_request = urllib.request.Request(api_url, headers={
            'Accept': 'application/vnd.github.v3+json'
        })
        api_result = urllib.request.urlopen(api_request)
        utf8reader = codecs.getreader("utf-8")

        return json.load(utf8reader(api_result))['parent']['html_url']


def translate(url):
    translators = (
        Boost(),
        Java(),
        GitHub(),
        Python(),
        Why3(),
        Wiki(r'https?://..\.wikipedia.org/wiki/.*'),
        Wiki(r'https?://..\.wiktionary.org/wiki/.*'),
        Xkcd(),
    )

    for t in translators:
        if t.match(url):
            return t(url)


if __name__ == '__main__':
    translation = translate(input())
    if translation:
        print(translation)
