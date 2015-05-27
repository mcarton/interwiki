from interwiki import translator
from interwiki.rules import RegExTranslator
import re


@translator()
class Java(RegExTranslator):
    re = r'https?://docs.oracle.com/javase/.*/docs/api/.*'

    def __call__(self, url):
        what = re.match(
            r'https?://docs.oracle.com/javase/.*/docs/api/(.*)', url
        )

        return 'https://docs.oracle.com/javase/8/docs/api/' + what.group(1)
