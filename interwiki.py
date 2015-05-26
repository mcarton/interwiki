#!/usr/bin/env python


from rules.Boost import Boost
from rules.GitHub import GitHub
from rules.Java import Java
from rules.Python import Python
from rules.Why3 import Why3
from rules.Wiki import Wiki
from rules.Xkcd import Xkcd


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


if __name__ == '__main__':
    translation = translate(input())
    if translation:
        print(translation)
