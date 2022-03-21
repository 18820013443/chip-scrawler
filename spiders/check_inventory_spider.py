import requests
from utils.http import GetRequestHeader


def SendInvetoryCheckRequest():
    url = 'https://www.analog.com/client/Product/PostSampleBuyData'
    headers = GetRequestHeader()
    # print(headers)
    payload = {
        'ProductIDList': 'LTC7000ARMSE#PBF, LTC7000ARMSE#TRPBF, LTC7000ARMSE#WPBF, LTC7000ARMSE#WTRPBF'
    }
    r = requests.post(url=url, headers=headers, data=payload)
    print(r.text)


def CheckInventory():
    pass


def main():
    SendInvetoryCheckRequest()


if __name__ == '__main__':
    main()
