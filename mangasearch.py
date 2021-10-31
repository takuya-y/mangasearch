import lxml.html
import requests
import sys

# マンガ新刊情報のWebページURLを入力する
get_page = input("URL: ")
r = requests.get(get_page)

# ページ情報を取得する
#tree = lxml.html.parse(r.text)
tree = lxml.html.fromstring(r.content)

# 新巻一覧を作成する
#tree = lxml.html.parse('index.html')
#orghtml = sys.stdin.read()
#tree = lxml.html.parse(orghtml)
#html = tree.getroot()

# チェックする漫画のリスト
books = open("mangalist.txt", "r", encoding="utf-8").readlines()

# tbody要素の1番目のtr(発売日)と3番目のtr(タイトル)の要素を取得したい
for a in tree.cssselect('td a'):
#    print(a.get('href'), a.text)
#    print(a.text)
    for i in range(len(books)):
        if books[i].strip('\n') in a.text:
            print(a.text)
            continue