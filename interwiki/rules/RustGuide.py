from interwiki import StartsWithTranslator
from interwiki import translator
import re


@translator()
class Boost(StartsWithTranslator):
    begin = 'doc.rust-lang.org/guide-'

    def __call__(self, url):
        what = re.match('https://' + self.begin + r'(.*).html(#(.*))?', url)

        if what.group(2):
            return 'https://doc.rust-lang.org/book/{}.html#{}'.format(
                    what.group(1), what.group(2)
            )
        else:
            return 'https://doc.rust-lang.org/book/{}.html'.format(
                    what.group(1)
            )
