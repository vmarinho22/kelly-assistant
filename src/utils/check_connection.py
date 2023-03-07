from urllib.request import URLError, urlopen


def online():
    try:
        urlopen('http://google.com', timeout=50)
        return True
    except URLError as err: 
        return False