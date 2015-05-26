from rules import StartsWithTranslator
import re


class Boost(StartsWithTranslator):
    begin = 'www.boost.org/doc/libs/'

    def __call__(self, url):
        what = re.match(r'http://www.boost.org/doc/libs/[\d_]*/(.*)', url)

        return 'http://www.boost.org/doc/libs/release/' + what.group(1)
