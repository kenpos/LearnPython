#clipボードにコピーした内容の各行に点を打つ
#markdown支援

import pyperclip
text = pyperclip.paste()

#行を分割して、”*”を追加する
#各行を分割する
lines = text.split('\n')

for i in range(len(lines)):
    lines[i] = '* ' + lines[i] #各行に「*」を追加する
text = '\n'.join(lines) #変更した行を結合する

pyperclip.copy(text)
print(text)