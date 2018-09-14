# -*- Coding: utf-8 -*-
import urllib.request, urllib.error, urllib.parse
from bs4 import BeautifulSoup

class Synonym:

    def getSy(self, word):

        # 参照先のURL
        # 今回は「日本語シソーラス 連想類語辞典」を使用
        self.__target_url = "https://renso-ruigo.com/word/"

        # アクセスするURLに日本語が含まれているのでエンコード
        self.__url = self.__target_url + urllib.parse.quote_plus(word, encoding='utf-8')

        # アクセスしてパース
        self.__html = urllib.request.urlopen(self.__url)
        self.__soup = BeautifulSoup(self.__html, "lxml")

        # 切り出したい場所のCSSセレクター
        self.__selector = "#content > div.word_t_field > div"

        result = self.__soup.select_one(self.__selector).text

        return result

sy = Synonym()

# 検索したい文字列
list = ['給与', '採用', '退職', '定年']

for item in list:
    print(sy.getSy(item))
