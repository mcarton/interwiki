import os

for module in os.listdir(os.path.dirname(__file__)):
    if module != '__init__.py' and module.endswith('.py'):
        __import__('interwiki.rules.' + module[:-3], locals(), globals())
