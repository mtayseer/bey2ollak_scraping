import urllib, datetime, os

def fetch():
    url = 'http://www.bey2ollak.com/Traffic?action=getTraffic&target=4&city=0&lang=1'
    output = datetime.datetime.now().strftime('bey2ollak.%Y-%m-%d-%H-%M-%S.html')
    output = os.path.join(os.path.dirname(__file__), output)
    urllib.urlretrieve(url, output)
    print output

if __name__ == '__main__':
    fetch()
