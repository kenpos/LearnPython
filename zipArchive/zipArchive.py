import zipfile, os


#現在のパスを絶対パスに変換し文字列として返す
abspath = os.path.abspath('./')
print(abspath)

os.chdir(abspath)

#zipファイルを作成したり，追加したり

#新規作成する場合はこちら
new_zip = zipfile.ZipFile('new.zip','w')

#追加する場合はこちら
#new_zip = zipfile.ZipFile('new.zip','a')

#圧縮 or 圧縮ファイルに追加
new_zip.write('zipArchive.py',compress_type=zipfile.ZIP_DEFLATED)
new_zip.close()


#zipファイルを読み込む
zipfile_test = zipfile.ZipFile('new.zip')

namelist = zipfile_test.namelist()
print(namelist)

#ファイルの詳細な情報を取得する
spam_info = zipfile_test.getinfo('zipArchive.py')
#展開後のファイルサイズ
tmp = '圧縮前:'+ str(spam_info.file_size)
print(tmp)
#圧縮時のファイルサイズ
tmp = '圧縮後:'+ str(spam_info.compress_size)
print(tmp)

tmp = '圧縮率{}'.format(round( spam_info.compress_size / spam_info.file_size, 2))
print(tmp)


#zipファイルを展開する
#zipfile_test.extractall()

#特定のファイルだけを展開する場合
#zipfile_test.extract('zipArchive.py')

#展開先を指定
zipfile_test.extract('zipArchive.py','./new')

zipfile_test.close()
