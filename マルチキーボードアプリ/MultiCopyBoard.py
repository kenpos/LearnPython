#! python3
# クリップボードのテキストを保存，復元する
# How to Use
# clipboardを保存:  python MultiCopyBoard.py save <key>
# clipボードに呼び出し: python python MultiCopyBoard.py <key>
# list:  python MultiCopyBoard.py list  
# keyが被った場合は上書き保存する
import  pyperclip, sys, shelve

mcbshelves = shelve.open('mcb')

#クリップボードに保存
if len(sys.argv) == 4 and sys.argv[1].lower() == 'save':
    mcbshelves[sys.argv[2]] = sys.argv[3]
    tmptext = '[' + str(sys.argv[2]) +':' + str(sys.argv[3]) + ']\nを登録しました' 
    print(tmptext)
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbshelves[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    #キーワード一覧
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbshelves.keys())))
        tmptext = 'リスト：' + str(list(mcbshelves.keys()))
        print(tmptext)
    elif sys.argv[1] in mcbshelves:
        pyperclip.copy(mcbshelves[sys.argv[1]])
        tmptext = '[' + str(mcbshelves[sys.argv[1]]) + ']\nをコピーしました'
        print(tmptext)

        mcbshelves.close()
mcbshelves.close()