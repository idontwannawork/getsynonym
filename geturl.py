# -*- Coding: utf-8 -*-
from urllib.request import urlopen
from urllib.error import URLError, HTTPError
from bs4 import BeautifulSoup

class UrlList:

    def getUrl(self, target_url, css_selector):

        try:
            # アクセスしてパース
            self.__html = urlopen(target_url)
            self.__soup = BeautifulSoup(self.__html, "lxml")

            result = []

            # 切り出したいCSS
            for self.__selected in self.__soup.select(css_selector):
                # その中のURLのみ抽出
                for a in self.__selected.find_all("a"):
                    result.append(a.get("href"))

            return result
        except HTTPError as e:
            print(e.reason)
        except URLError as e:
            print(e.reason)

sy = UrlList()

# 対象のアドレスと対象のCSSセレクターを指定
urls = sy.getUrl("https://renso-ruigo.com/", "#sideWrap > div.sidebar-box1")

for url in urls:
    print(url)
