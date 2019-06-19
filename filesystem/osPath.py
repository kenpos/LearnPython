import os 

#現在のパスを絶対パスに変換し文字列として返す
path = os.path.abspath('./filepath')
print(path)

#絶対パスならTrue
boolean = os.path.isabs(path)
print(boolean)

#相対パスに変換
relpath = os.path.relpath('/Users/kenpos',path)
print(relpath)

#ファイル名のみを返す
path = os.path.abspath('./filepath.py')
print(path)
basename = os.path.basename(path)
print(basename)


