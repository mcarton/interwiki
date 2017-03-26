from interwiki import StartsWithTranslator
from interwiki import translator
import re


@translator()
class OSM2GM(StartsWithTranslator):
    begin = 'www.openstreetmap.org/'

    def get_coords(url):
        m = re.search(r'map=([\d.]+)/([\d.]+)/([\d.]+)', url)
        return (m.group(1), m.group(2), m.group(3))

    def get_link(z, x, y):
        return 'https://www.google.com/maps/@%s,%s,%sz' % (x, y, z)

    def __call__(self, url):
        (z, x, y) = OSM2GM.get_coords(url)
        return OSM2GM.get_link(z, x, y)


@translator()
class GM2OSM(StartsWithTranslator):
    begin = 'www.google.com/maps'

    def get_coords(url):
        m = re.search(r'@([\d.]+),([\d.]+),([\d.]+)z', url)
        return (m.group(1), m.group(2), m.group(3))

    def get_link(z, x, y):
        return 'https://www.openstreetmap.org/#map=%s/%s/%s' % (z, x, y)

    def __call__(self, url):
        (x, y, z) = GM2OSM.get_coords(url)
        return GM2OSM.get_link(z, x, y)
