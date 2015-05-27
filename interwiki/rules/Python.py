from interwiki import translator
from interwiki.rules import StartsWithTranslator
import re
import sys


@translator()
class Python(StartsWithTranslator):
    begin = 'docs.python.org/'
    (major, minor) = sys.version_info[:2]

    def __call__(self, url):
        what = re.match(r'https?://docs.python.org/[\d.]*/(.*)', url)

        return 'https://docs.python.org/%s.%s/%s' \
            % (self.major, self.minor, what.group(1))
