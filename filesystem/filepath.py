import os

os.path.join('usr','bin','spam')

my_file = ['accounts.txt','datailes.csv','invite.docx']

#ファイルパスを作る．
for filename in my_file:
    print(os.path.join('/Users/kenpos/src/python/CopyAndPaste/filesystem',filename))

#Get current directory
os_path = os.getcwd()

os.chdir(os_path)
print(os_path)


#mkdir
#現在のディレクトリに./hello/worldというフォルダ構成でフォルダを作る
os.makedirs(os_path + '//hello//world')