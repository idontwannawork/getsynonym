# -*- Coding: utf-8 -*-
from urllib.request import urlopen
from urllib.parse import quote, unquote
from urllib.error import URLError, HTTPError
from urllib.request import Request
from bs4 import BeautifulSoup

class UrlList:

    def getUrl(self, target_url, css_selector):

        try:
            # アクセスしてパース
            self.__decoded = quote(target_url, safe=":/")
            self.__headers = {
                "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0",
            }
            request = Request(url=self.__decoded, headers=self.__headers)
            self.__html = urlopen(request)
            # self.__html = urlopen(url=self.__decoded, headers=self.__headers)
            self.__soup = BeautifulSoup(self.__html, "lxml")

            result = []

            # 切り出したいCSS
            for self.__selected in self.__soup.select(css_selector):
                # その中のURLのみ抽出
                for a in self.__selected.find_all("a"):
                    result.append(unquote(a.get("href")))

            return result
        except HTTPError as e:
            return "HTTP error " + e.reason
        except URLError as e:
            return "URL error" + e.reason

sy = UrlList()

# 対象のアドレスと対象のCSSセレクターを指定
urls = sy.getUrl("https://renso-ruigo.com/", "#sideWrap > div.sidebar-box1")

for url in urls:
    print(url)
