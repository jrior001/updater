import os

class Config(object):
    GERRIT_URL = os.environ.get('GERRIT_URL', 'https://review.lineageos.org')
    CACHE_DEFAULT_TIMEOUT = int(os.environ.get('CACHE_DEFAULT_TIMEOUT', '100'))
    CACHE_TYPE = os.environ.get('CACHE_TYPE', 'simple')
    CACHE_REDIS_HOST = os.environ.get('CACHE_REDIS_HOST', 'redis')
    CACHE_REDIS_DB = os.environ.get('CACHE_REDIS_DB', 4)
    WIKI_INSTALL_URL = os.environ.get('WIKI_INSTALL_URL', 'https://wiki.lineageos.org/devices/{device}/install')
    WIKI_INFO_URL = os.environ.get('WIKI_INFO_URL', 'https://wiki.lineageos.org/devices/{device}')

    UPSTREAM_URL = os.environ.get('UPSTREAM_URL', 'http://home.theflamingskull.com/builds.json')
    DOWNLOAD_BASE_URL = os.environ.get('DOWNLOAD_BASE_URL', 'http://home.theflamingskull.com/builds/')
    EXTRAS_BLOB = os.environ.get('EXTRAS_BLOB', 'extras.json')
