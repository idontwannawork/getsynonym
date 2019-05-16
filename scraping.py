from urllib.request import urlopen
from urllib.parse import quote_plus
from urllib.error import URLError, HTTPError
from bs4 import BeautifulSoup

class Synonym:

    def getSy(self, word, target_url, css_selector):

        try:
            # アクセスするURLに日本語が含まれているのでエンコード
            self.__url = target_url + quote_plus(word, encoding='utf-8')

            # アクセスしてパース
            self.__html = urlopen(self.__url)
            self.__soup = BeautifulSoup(self.__html, "lxml")

            result = self.__soup.select_one(css_selector).text

            return result
        except HTTPError as e:
            print(e.reason)
        except URLError as e:
            print(e.reason)
            
sy = Synonym()

# 検索したい文字列
list = ['戦車', '南極', 'エスペラント']

# 検索する先は「日本語シソーラス 連想類語辞典」を使用
target = "https://renso-ruigo.com/word/"
selector = "#content > div.word_t_field > div"

for item in list:
    print(sy.getSy(item,target,selector))
