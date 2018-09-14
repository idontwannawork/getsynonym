# サイトから任意の箇所を切り出して類語検索

複数の単語について類語を調べる必要があったので、とりあえずざっくり作った。

## 環境
* python3
* BeautifulSoup
 
    $ pip install beautifulsoup4

* urllib

IDEはvscodeを使った。

## 内容

[日本語シソーラス 連想類語辞典](https://renso-ruigo.com/)に対して調べたい単語を投げて、帰ってきた結果のHTMLの特定部分だけ切り出す。切り出しはBeautifulSoupを使用して、CSSセレクターで切り出す対象の場所を特定。

なお、CSSセレクターはGoogle Chromeで生成（[参考](https://qiita.com/Azunyan1111/items/b161b998790b1db2ff7a)）。

ちなみに、まだ例外処理を全然していないので注意。アクセス先できなかったり、404なんかのエラーを返してきたりするとダメ。
