# -*- Coding: utf-8 -*-
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

class UrlList:

    def getUrl(self, target_url):

        options = Options()
        # 必要な場合はChrome Canaryのフォルダを指定する
        # options.binary_location = "C:\\hoge\\Application\\chrome.exe"
        # ヘッドレスモードで実行する場合はこのオプションを設定する
        # options.add_argument("--headless")

        driver = webdriver.Chrome(chrome_options=options)

        # アクセスしてhref要素だけ取得する
        driver.get(target_url)
        first = driver.page_source

        # 上限10回とし最後までスクロールしてページを取得する
        for _ in range(10):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)
            next = driver.page_source
            if first == next:
                break
            else:
                first = next

        a_list = driver.find_elements_by_tag_name("a")

        result = []
        for href in a_list:
            if href.get_attribute("href"):
                result.append(href.get_attribute("href"))

        driver.quit()

        return result, next

sy = UrlList()

# 対象のアドレスを指定
urls, source = sy.getUrl("https://www.yahoo.co.jp/")

str = "\n".join(urls) + "\n" + source

# ファイル出力
path = "c:\\\\hoge\\"
file_name = "urls.txt"

with open(path + file_name, mode="wt", encoding="utf-8") as f:
    f.write(str)
