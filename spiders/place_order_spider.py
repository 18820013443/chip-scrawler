import sys, os
# sys.path.append("../..")
sys.path.append(os.path.abspath('./'))
# sys.path.append(os.path.abspath(os.path.join(os.getcwd())))
# print(os.path.abspath('./'))

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from settings import GetParams, CHROME_PORT, LOGIN_URL
# import settings


# browser = webdriver.Chrome()


def PlaceOrder():
    pass


def LaunchChrome(osType):
    CHROME_PATH, USER_DATA_DIR = GetParams(osType)
    if osType == 'Win':
        os.system('cd %s & start chrome.exe --remote-debugging-port=%s --user-data-dir=%s' % (CHROME_PATH, CHROME_PORT, USER_DATA_DIR))
    elif osType == 'Mac':
        os.system('%s --remote-debugging-port=%s --user-data-dir=%s' % (CHROME_PATH, CHROME_PORT, USER_DATA_DIR))
    options = Options()
    options.add_experimental_option('debuggerAddress', "127.0.0.1:%s" % CHROME_PORT)
    browser = webdriver.Chrome(options=options)
    browser.get(LOGIN_URL)
    return browser


def main():
    browser = LaunchChrome('Win')
    browser.get('https://www.bilibili.com/')
    print(browser.title)


if __name__ == '__main__':
    main()
