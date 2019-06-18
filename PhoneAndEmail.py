#phone NumberとEmail取得する
import re,pyperclip

#電話番号と内線番号を取得する
phone_regex = re.compile(r'''(
(\d{1,4}|\(\d{1,4}\))          #市外局番()付いていても良い
(\s|-)                         #区切り(スペースかハイフン)
(\d{1,4}|\(\d{1,4}\))          #市内局番
(\s|-)                         #区切り
(\d{3,4})                      #４桁の番号
(\s*(ext|x|ext.)\s*(\d{2,5}))? #内線番号
)''', re.VERBOSE)

mo = phone_regex.findall(r'津波観測情報緊急連絡先(072)-658-7119(2567),090-1433-2098,aaa080-(183)-1133')
print('findall')
print(mo[0][0])
print(mo[1][0])
print(mo[2][0])

#電子メール
email_regex = re.compile(r'''(
([a-zA-Z0-9._%+-]+)#ユーザー名
@                  #@
([a-zA-Z0-9.-]+)   #ドメイン
(\.[a-zA-Z]{2,4})  #ドットなんたら
)''', re.VERBOSE)

mo1 = email_regex.findall(r'私のメアドは kenpos13@gmail.com と your.mailaddress@donson-injonson.comとyahoo@gmail.co.jpです')
print('findall')
print(mo1[0][0])
print(mo1[1][0])
print(mo1[2][0])