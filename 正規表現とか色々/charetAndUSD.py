#キャレット文字^で先頭マッチ
#$で文末にマッチ
#^$を組み合わせると文字列全体がマッチ

import re

#冒頭にあるHelloにマッチする
begin_regix = re.compile(r'^Hello')

#検索し，パターンマッチした奴を全部抽出する
mo1 = begin_regix.search('HelloWorld')
if mo1:
    print(mo1.group())
else:
    print("matchしてない")

mo1 = begin_regix.search('He said Hello World')
#設定した正規表現を使って抽出する
if mo1:
    print(mo1.group())
else:
    print("matchしてない")

#行末にある数字にマッチする
endNumber_regix = re.compile(r'\d$')

#検索し，パターンマッチした奴を全部抽出する
mo1 = endNumber_regix.search('Your Number is 42')
if mo1:
    print(mo1.group())
else:
    print("matchしてない")
    

endNumber_match_regix = re.compile(r'\d*$')
#検索し，パターンマッチした奴を全部抽出する
mo1 = endNumber_match_regix.search('11 Your Number is 42')
if mo1:
    print(mo1.group())
else:
    print("matchしてない")
    