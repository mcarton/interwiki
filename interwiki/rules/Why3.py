from interwiki.rules import RegExTranslator
import re


class Why3(RegExTranslator):
    re = r'https?://why3.lri.fr/(doc|stdlib)-.*'

    def __call__(self, url):
        what = re.match(
            r'http(s?)://why3.lri.fr/(doc|stdlib)-[^/]*/(.*)', url
        )

        return 'http{}://why3.lri.fr/{}-0.85/{}'.format(
            what.group(1), what.group(2), what.group(3)
        )
