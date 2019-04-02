# Pythonによるスクレイピング

## 環境
* python3
* BeautifulSoup
 
    $ pip install beautifulsoup4

* urllib

IDEはvscodeを使った。

## サイトから任意の箇所を切り出して類語検索

`scraping.py`

複数の単語について類語を調べる必要があったので、とりあえずざっくり作った。

### 内容

[日本語シソーラス 連想類語辞典](https://renso-ruigo.com/)に対して調べたい単語を投げて、帰ってきた結果のHTMLの特定部分だけ切り出す。切り出しはBeautifulSoupを使用して、CSSセレクターで切り出す対象の場所を特定。

なお、CSSセレクターはGoogle Chromeで生成（[参考](https://qiita.com/Azunyan1111/items/b161b998790b1db2ff7a)）。

## サイトの任意の箇所からURLを取得

`geturl.py`

URLの一覧が欲しかったので、こっちもとりあえずざっくり作った。

### 内容

アクセスしたページの任意の場所に存在するURLを取得する。複数ある場合は、あっただけ全て取得する。「任意の場所」の指定はCSSセレクターで行う。こちらもCSSセレクターはChromeで生成。

## サイト全体からURLを取得

`geturl_selenium.py`

サイト全体のURLの一覧が欲しかった。

### 内容

アクセスしたページに存在する全ての`href`要素を抽出する。seleniumとChrome webdriverが必要。無限スクロールするようなサイトでは、10回を上限にスクロールして情報を取得する。
