import requests
from utils.http import GetRequestHeader
import json


def SendInvetoryCheckRequest(inputProductListStr):
    url = 'https://www.analog.com/client/Product/PostSampleBuyData'
    headers = GetRequestHeader()
    # print(headers)
    payload = {
        'ProductIDList': inputProductListStr
    }
    r = requests.post(url=url, headers=headers, data=payload)
    productList = json.loads(r.text)['ModelList']
    print(productList)
    return productList


def CheckInventory(productList):
    placeOrderDic = {}
    for product in productList:
        placeOrderDic[product['ModelName']] = product['AnalogDevicesColumnInfo']['IsAddtoCart']
    print(placeOrderDic)
    return placeOrderDic


def main():
    inputProductListStr = 'LTC7000ARMSE#PBF,LTC7000ARMSE#TRPBF,LTC7000ARMSE#WPBF,LTC7000ARMSE#WTRPBF'
    productList = SendInvetoryCheckRequest(inputProductListStr)
    placeOrderDic = CheckInventory(productList)


if __name__ == '__main__':
    main()
