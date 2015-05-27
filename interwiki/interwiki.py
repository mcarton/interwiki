#!/usr/bin/env python


from interwiki.translators import translators
import interwiki.rules  # nopep8


def translate(url):
    for t in translators:
        if t.match(url):
            return t(url)


def main():
    translation = translate(input())
    if translation:
        print(translation)


if __name__ == '__main__':
    main()
