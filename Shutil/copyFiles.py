#Copyとdelのやり方を

import shutil,os

#現在のパスを絶対パスに変換し文字列として返す
abspath = os.path.abspath('./')
print(abspath)

#cd相当
os.chdir(abspath)

#tmpフォルダを作る
createdir = abspath + '/tmp'
#Nullチェック
os.makedirs(createdir, exist_ok=True)

#コピーする
shutil.copy('copy.txt',createdir)

#バックアップとしてフォルダごとコピーする
backpathdir = abspath + '/tmp_backup'
if not os.path.exists(backpathdir):
    shutil.copytree('tmp',backpathdir)

movepathdir = abspath + '/move.txt'
#フォルダ移動(ファイルを移動したり，名前を変えたりできる)
shutil.move(backpathdir+'/copy.txt', movepathdir)

#パス指定したファイルを削除
#os.unlink(path)

#パスに指定したフォルダを削除(空のやつオンリー)
#os.rmdir(path)

#確認用
for filename in os.listdir():
    if filename.endwith('.pdf'):
        #os.unlink(filename)
        print(filename)
