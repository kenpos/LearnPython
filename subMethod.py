#sub()メソッドを用いて文字列を置換する
import re

#文字を置換する
name_regex = re.compile(r'Agent \w+')
mo = name_regex.sub('CENSORED', 'Agent Alice gave the secret douments to Agent Bob.')
print(mo)