from interwiki import StartsWithTranslator
from interwiki import translator
import re
import sys


@translator()
class Archlinux(StartsWithTranslator):
    begin = 'www.archlinux.org/packages/'
    (major, minor) = sys.version_info[:2]

    def __call__(self, url):
        what = re.match(r'https?://www.archlinux.org/packages/\?q=(.*)', url)

        return'https://aur.archlinux.org/packages.php?K=%s' % what.group(1)
