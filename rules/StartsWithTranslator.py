class StartsWithTranslator:
    def match(self, url):
        if url.startswith('http://'):
            url = url[len('http://'):]
        elif url.startswith('https://'):
            url = url[len('https://'):]

        return url.startswith(self.begin)
