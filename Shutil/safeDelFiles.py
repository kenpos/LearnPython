#外部モジュールを使うと削除するときも安全に
#サーバー上のファイルでやったらどうなるんだろう．多分普通に完全に削除されるのかなと

import send2trash

becon_file = open('becon.txt','a')  #ファイルを作成する
becon_file.write('Becon is not a vegetable.') 

becon_file.close()

#ゴミ箱に削除する
send2trash.send2trash('becon.txt')