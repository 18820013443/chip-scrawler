from utils.http import GetRequestHeader
from utils.tools import WriteTextToFile
import requests


def SearchItem():
    headers = GetRequestHeader()
    item = 'LTC7000A'
    # url = 'https://www.analog.com/cn/search.html?q=%s' % item
    # url = 'https://www.analog.com/cn/products/%s.html#product-samplebuy' % str.lower(item)
    url = 'https://www.analog.com/client/Product/PostSampleBuyData'
    # url = 'https://shoppingcart.analog.com/AddModel.aspx?locale=zh&ACTION=BUY_BUNDLES&modelNbr=LTC7000ARMSE%23PBF'
    # print(url)
    r = requests.get(url)
    WriteTextToFile('test.html', r.text)
    # print(r.text)


def main():
    SearchItem()


if __name__ == '__main__':
    main()
