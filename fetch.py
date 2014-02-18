import requests, datetime

def fetch():
    url = 'http://www.bey2ollak.com/Traffic?action=getTraffic&target=4&city=0&lang=1'
    content = requests.get(url).content
    output_file_name = datetime.datetime.now().strftime('bey2ollak.%Y-%m-%d-%H-%M-%S.html')
    open(output_file_name, 'w').write(content)
    print output_file_name

if __name__ == '__main__':
    fetch()