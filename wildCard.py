#.で特定の一文字を置き換えた文字で一致確認
import re

#特定の文字マッチング
vowelMatch_regex = re.compile(r'.at')

#検索し，パターンマッチした奴を全部抽出する
mo1 = vowelMatch_regex.findall('The cat in the Hat sat on the flat mat.')
print(mo1)

