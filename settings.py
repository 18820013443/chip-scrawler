from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

# CHROME_PATH = r'/Applications/Google Chrome.app'
# CHROME_PATH = "/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome"
# USER_DATA_DIR = '/Users/kaitang/Code-Projects/chip-scrawler/ChromeConfig'
CHROME_PORT = '9527'

LOGIN_URL = 'https://analogb2c.b2clogin.com/analogb2c.onmicrosoft.com/b2c_1a_adi_signuporsigninsocial/oauth2/v2.0' \
            '/authorize?client_id=8064ba55-8edd-4ffb-81b7-fb252ed39815&response_mode=form_post&response_type=id_token' \
            '&scope=openid&state=OpenIdConnect.AuthenticationProperties%3DLNpt6w1mQvd5fGHs7afZg85UflvVfaRDR' \
            '-NMy4eSo9w1TD-Ec1uMgSVbYjvkzGdFD1wh3CPSqb6k4gilY_q-xYdo0J4Md9QsAyEq6HxHrBokTmLgblkwJJ3Kxian9qQ' \
            '-4nyPyq74hKyeu8vd5AHcE24pYlqaYBqQk3UohbOAzxyEi938MP4GoBZ9x_CsNjMQ&nonce=637835351195683907' \
            '.NTlkM2FhZDAtNWJhYi00NTZhLTkyNzMtNGE0NTNlM2E2NGQ2NTk5NjZiNGMtZmQyYy00MzhkLWI0YTItNDVmOWYxN2RiODJm' \
            '&ui_locales=zh-hans&loginContext=shoppingcart&requestLocale=zh&startUrl=https%3A%2F%2Fshoppingcart' \
            '.analog.com%2FShoppingCartPage.aspx%3Flocale%3Dzh&redirect_uri=https%3A%2F%2Fshoppingcart.analog.com' \
            '%2Foidc&post_logout_redirect_uri=https%3A%2F%2Fshoppingcart.analog.com&x-client-SKU=ID_NET451&x-client' \
            '-ver=5.2.1.0 '
USERNAME = 'sanniuguoji@163.com'
PASSWORD = 'yy11YY99,'


def GetParams(osType):
    CHROME_PATH, USER_DATA_DIR = '', ''
    if osType == 'Win':
        CHROME_PATH = "kk"
        USER_DATA_DIR = 'kk'
    elif osType == 'Mac':
        CHROME_PATH = "/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome"
        USER_DATA_DIR = '/Users/kaitang/Code-Projects/chip-scrawler/ChromeConfig'
    return CHROME_PATH, USER_DATA_DIR


if __name__ == '__main__':
    GetParams('Win')
