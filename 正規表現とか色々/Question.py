#疑問符を用いた任意のマッチ
#()の後ろに?があると，()の中の文字がある時と無い時にヒットする
import re

#正規表現を設定する
bat_regex = re.compile(r'Bat(wo)?man')

#設定した正規表現を使って抽出する
mo = bat_regex.search('The Adventures of Batman')

print(mo.group())

#正規表現でグループを
mo1 = bat_regex.search('The Adventures of Batwoman')
print(mo1.group())
