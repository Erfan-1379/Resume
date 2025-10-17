from decouple import config

DEBUG = config('DEBUG', cast=bool)

if DEBUG:
    from settings.dev import *
else:
    from settings.deploy import *
