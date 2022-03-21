import requests


def SearchItem():
    headers = {
        'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    }
    item = 'LTC7000A'
    url = 'https://www.analog.com/cn/search.html?q=%s'%item
    r = requests.get(url)
    print(r.text)

def main():
    SearchItem()


if __name__ == '__main__':
    main()
