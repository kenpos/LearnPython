#ディレクトリを歩く

import os


#現在のパスを絶対パスに変換し文字列として返す
abspath = os.path.abspath('../')
print(abspath)

tmp = ''
for foldername, subfolders, filenames in os.walk(abspath):
    
    for subfolder in subfolders:
        print(tmp + '|---' + subfolder)
            
    for filenames in filenames:
        print('*  ' + filenames)

    print ('')