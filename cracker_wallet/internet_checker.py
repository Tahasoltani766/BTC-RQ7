import requests

def check_internet_connection(url='http://www.google.com', timeout=5):
    try:
        response = requests.get(url, timeout=timeout)
        return True
    except requests.ConnectionError:
        return False


