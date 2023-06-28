from urllib.request import urlopen
from urllib.error import URLError


def online():
    try:
        urlopen('http://google.com', timeout=50)
        return True
    except URLError as err: 
        return False