from interwiki.rules import StartsWithTranslator
import json
import re
import requests


class GitHub(StartsWithTranslator):
    begin = 'github.com/'

    def __call__(self, url):
        what = re.match(r'https?://github.com/([^/]*)/([^/]*)', url)

        api_url = 'https://api.github.com/repos/{}/{}'.format(
            what.group(1), what.group(2)
        )

        j = json.loads(requests.get(api_url).text)

        return j['parent']['html_url']
