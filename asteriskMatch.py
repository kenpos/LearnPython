import re

#*を用いた0回以上のマッチ
bat_regex = re.compile(r'Bat(wo)*man')

#設定した正規表現を使って抽出する
mo = bat_regex.search('The Adventures of Batman')

print(mo.group())

#正規表現でグループ
mo1 = bat_regex.search('The Adventures of Batwoman')
if mo1:
    print("matchした")
    print(mo1.group())
else:
    print("matchしてない")

#正規表現でグループ
mo2 = bat_regex.search('The Adventures of Batwowoman')
if mo2:
    print("matchした")
    print(mo2.group())
else:
    print("matchしてない")

#正規表現でグループ
mo3 = bat_regex.search('The Adventures of Batwowowowowowowowowowoman')
if mo3:
    print("matchした")
    print(mo3.group())
else:
    print("matchしてない")

#正規表現でグループ
mo4 = bat_regex.search('The Adventures of Batwoooooooooooman')
if mo4:
    print("matchした")
    print(mo4.group())
else:
    print("matchしてない")