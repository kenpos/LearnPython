#正規表現で|を使うと先に一致した方を取得する
import re

#正規表現を設定する
hero_regex = re.compile(r'Batman|Tina Fey')

#設定した正規表現を使って抽出する
mo = hero_regex.search('Batman and Tina Fey Baaaatman')

print(mo.group())

#正規表現でグループを
mo = hero_regex.search('Tina Fey Batman and Baaaatman')
print(mo.group())

