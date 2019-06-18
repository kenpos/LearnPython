#正規表現で電話番号を探す
import re

#正規表現を設定する
phone_num_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

#設定した正規表現を使って電話番号だけを抽出する
mo = phone_num_regex.search('私の電話番号は415-555-4242ですわよ．')

print('電話番号:'+ mo.group())

#正規表現でグループを
phone_num_group_regex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')

mo = phone_num_group_regex.search('私の電話番号は415-555-4242ですわよ．')

print('電話番号:'+ mo.group(0))
print('電話番号:'+ mo.group(1))
print('電話番号:'+ mo.group(2))
