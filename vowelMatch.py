#[]で特定の文字集合のみをマッチさせる
import re

#特定の文字マッチング
vowelMatch_regex = re.compile(r'[aeiueoAEIOU]')

#検索し，パターンマッチした奴を全部抽出する
mo1 = vowelMatch_regex.findall('RoboCop feed eats baby food. BABY FOOD')
print(mo1)
print()

#特定の文字以外マッチング
vowelMatch_regex = re.compile(r'[^aeiueoAEIOU]')

#検索し，パターンマッチした奴を全部抽出する
mo1 = vowelMatch_regex.findall('RoboCop feed eats baby food. BABY FOOD')
print(mo1)

