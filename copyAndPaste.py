import pyperclip

#clip boardにコピーする
pyperclip.copy("Hello world")

#clip boardの値を取得する
str = pyperclip.paste()
print(str)
