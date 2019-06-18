#波括弧を用いて繰り返し回数を指定
import re

#(HaHaHa)
ha3_regex = re.compile(r'(Ha){3}')

#(HaHaHa|HaHaHaHa|HaHaHaHaHa)
ha3_5_regex = re.compile(r'(Ha){3,5}')

#設定した正規表現を使って抽出する
mo = ha3_regex.search('AmagasakiHaHaHa')
if mo:
    print("matchした")
    print(mo.group())
else:
    print("matchしてない")

#設定した正規表現を使って抽出する
mo1 = ha3_regex.search('AmagasakiHaHaHaHa')
if mo1:
    print("matchした")
    print(mo1.group())
else:
    print("matchしてない")

#正規表現でグループ
mo2 = ha3_5_regex.search('AmagasakiHaHaHaHa')
if mo2:
    print("matchした")
    print(mo2.group())
else:
    print("matchしてない")

#正規表現でグループ
mo3 = ha3_5_regex.search('AmagasakiHaHaHaHaHa')
if mo3:
    print("matchした")
    print(mo3.group())
else:
    print("matchしてない")

#正規表現でグループ
mo4 = ha3_5_regex.search('AmagasakiHaHaHaHaHaHa')
if mo4:
    print("matchした")
    print(mo4.group())
else:
    print("matchしてない")


#正規表現でグループ
mo5 = ha3_5_regex.search('AmagasakiHaHaHa')
if mo1:
    print("matchした")
    print(mo5.group())
else:
    print("matchしてない")

#正規表現でグループ
mo6 = ha3_5_regex.search('AmagasakiHaHa')
if mo6:
    print("matchした")
    print(mo6.group())
else:
    print("matchしてない")

#正規表現でグループ
mo7 = ha3_5_regex.search('AmagasakiHaHaHaHaHaHaHa')
if mo4:
    print("matchした")
    print(mo7.group())
else:
    print("matchしてない")
