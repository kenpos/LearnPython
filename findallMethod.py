#正規表現で電話番号を探す
import re

#正規表現を設定する
phone_num_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

#設定した正規表現を使って電話番号だけを抽出する
mo = phone_num_regex.search('私の電話番号は415-555-4242ですわよ.Cell 421-223-1234')

print('search')
print(mo.group())

#検索し，パターンマッチした奴を全部抽出する
mo1 = phone_num_regex.findall('私の電話番号は415-555-4242ですわよ.Cell 421-223-1234')

print('findall')
print(mo1)
print(mo1[0])
print(mo1[1])