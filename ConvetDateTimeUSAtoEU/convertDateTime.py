import shutil, os, re

#米国式日付のファイル名にマッチする正規表現
date_pattern = re.compile(r"""^(.*?)
                          ((0|1)?\d)-
                          ((0|1|3)?\d)-
                          ((19|20)\d\d)
                          (.*?)$
                          """,re.VERBOSE)

# カレントディレクトリの全ファイルをループする
for amer_filename in os.listdir('.'):
    mo = date_pattern.search(amer_filename)
    
    # 日付のないファイルをスキップ
    if mo == None:
        continue
    
    #ファイル名を部分分解する
    before_part = mo.group(1)
    month_part = mo.group(2)
    day_part = mo.group(4)
    year_part = mo.group(6)
    after_part = mo.group(8)

    
    #欧米式の日付のファイル名を作成
    euro_filename = before_part + day_part + '-' + month_part + '-' + year_part + after_part 
    
    #ファイル名を変更する
    print('Renaming "{}" to "{}"...'.format(amer_filename,euro_filename))
    shutil.move(amer_filename, euro_filename)
