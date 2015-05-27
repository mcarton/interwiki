import interwiki.translators


def translator(*args):
    def impl(clazz):
        interwiki.translators.append(clazz(*args))
        return clazz

    return impl
