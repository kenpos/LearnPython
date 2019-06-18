#文字集合
#\d:0~9の数字
#\D:0~9の数字以外
#\w:文字，数字，下線
#\W:文字，数字，下線以外
#\s:スペース，タブ，改行(空白のspace)
#\S:スペース，タブ，改行以外

import re

#1つ以上の数字の次に空白文字があり，一つ以上文字，数字，下線
xmas_regex = re.compile(r'\d+\s\w+')

#検索し，パターンマッチした奴を全部抽出する
mo1 = xmas_regex.findall('12 drummers,11 pipers,10 lords,9 ladies,8 maids,7 swans,6 geese,5 rings,4 birds,3 hens,2 doves,1 patridge')
print(mo1)

print()
mo2 = xmas_regex.findall('12drummers,11pipers__,10lords,9ladies, maids,swans,6geese,5ings,4 birds,3 hens,2_doves,1_patridge')
print(mo2)