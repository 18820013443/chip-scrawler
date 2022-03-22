from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from settings import GetParams, CHROME_PORT, LOGIN_URL
import os


# browser = webdriver.Chrome()


def PlaceOrder():
    pass


def LaunchChrome():
    url = ''
    CHROME_PATH, USER_DATA_DIR = GetParams('Mac')
    os.system('%s --remote-debugging-port=%s --user-data-dir=%s' % (CHROME_PATH, CHROME_PORT, USER_DATA_DIR))
    options = Options()
    options.add_experimental_option('debuggerAddress', "127.0.0.1:%s" % CHROME_PORT)
    browser = webdriver.Chrome(options=options)
    browser.get(LOGIN_URL)
    return browser


def main():
    browser = LaunchChrome()
    print(browser)


if __name__ == '__main__':
    main()
