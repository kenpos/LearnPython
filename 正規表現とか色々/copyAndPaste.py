import pyperclip

#clip boardにコピーする
pyperclip.copy("Hello world")

#clip boardの値を取得する
str = pyperclip.paste()
#確認用
print(str)
