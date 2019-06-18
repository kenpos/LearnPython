#sub()メソッドを用いて文字列を置換する
import re

#文字を置換する
name_regex = re.compile(r'Agent \w+')
mo = name_regex.sub('CENSORED', 'Agent Alice gave the secret douments to Agent Bob.')
print(mo)

#\1はグループ１にマッチした文字列
name_regex = re.compile(r'Agent (\w)\w*')
mo1 = name_regex.sub('\1****', 'Agent Alice told Agent carol that Agent Eve knew Agent Nob was a double agent gave the secret douments to Agent Bob.')
print(mo1)

