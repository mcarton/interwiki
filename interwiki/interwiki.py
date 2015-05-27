#!/usr/bin/env python


from interwiki.rules.Boost import Boost
from interwiki.rules.GitHub import GitHub
from interwiki.rules.Java import Java
from interwiki.rules.Python import Python
from interwiki.rules.Why3 import Why3
from interwiki.rules.Wiki import Wiki
from interwiki.rules.Xkcd import Xkcd


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


def main():
    translation = translate(input())
    if translation:
        print(translation)


if __name__ == '__main__':
    main()
