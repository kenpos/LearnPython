#大文字，小文字を無視したマッチング
#compileオプション「re.I」をつける
import re

#1つ以上の数字の次に空白文字があり，一つ以上文字，数字，下線
robocop_regex = re.compile(r'RoboCop',re.I)
mo = robocop_regex.search('RoboCop is part man,part machine,all cop.').group()
print(mo)

#検索し，パターンマッチした奴を全部抽出する
mo1 = robocop_regex.search('ROBOCOP is part man,part machine,all cop.').group()
print(mo1)

mo2 = robocop_regex.search('Al,whiy does your programming book talk about robocop so much????').group()
print(mo2)
