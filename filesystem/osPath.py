import os 

#現在のパスを絶対パスに変換し文字列として返す
abspath = os.path.abspath('./filepath')
print(abspath)

#絶対パスならTrue
boolean = os.path.isabs(abspath)
print(boolean)

#相対パスに変換
relpath = os.path.relpath('/Users/kenpos',abspath)
print(relpath)

#ファイル名のみを返す
path = os.path.abspath('./filepath.py')
print(path)
basename = os.path.basename(path)
print(basename)

#ファイルのサイズを取得する
filesize = os.path.getsize(path)
print(filesize)

#lsみたいなもん
filels = os.listdir('./')
print(filels)

#ファイルのトータルサイズを知りたい時

total_size = 0 
paths = os.path.abspath('./')
for filename in os.listdir('./'):
    total_size = total_size + os.path.getsize(os.path.join(paths,filename))

print(total_size)