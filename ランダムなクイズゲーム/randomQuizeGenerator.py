import random

capitals ={ '北海道(ほっかいどう)':'札幌(さっぽろ)',
 '青森県(あおもり)':'青森(あおもり)',
 '岩手県(いわて)':'盛岡(もりおか)',
 '宮城県(みやぎ)':'仙台(せんだい)',
 '秋田県(あきた)':'秋田(あきた)',
 '山形県(やまがた)':'山形(やまがた)',
 '福島県(ふくしま)':'福島(ふくしま)',
 '茨城県(いばらき)':'水戸(みと)',
 '栃木県(とちぎ)':'宇都宮(うつのみや)',
 '群馬県(ぐんま)':'前橋(まえばし)',
 '埼玉県(さいたま)':'さいたま',
 '千葉県(ちば)':'千葉(ちば)',
 '東京都(とうきょう)':'東京(とうきょう)',
 '神奈川県(かながわ)':'横浜(よこはま)',
 '新潟県(にいがた)':'新潟(にいがた)',
 '富山県(とやま)':'富山(とやま)',
 '石川県(いしかわ)':'金沢(かなざわ)',
 '福井県(ふくい)':'福井(ふくい)',
 '山梨県(やまなし)':'甲府(こうふ)',
 '長野県(ながの)':'長野(ながの)',
 '岐阜県(ぎふ)':'岐阜(ぎふ)',
 '静岡県(しずおか)':'静岡(しずおか)',
 '愛知県(あいち)':'名古屋(なごや)',
 '三重県(みえ)':'津(つ)',
 '滋賀県(しが)':'大津(おおつ)',
 '京都府(きょうと)':'京都(きょうと)',
 '大阪府(おおさか)':'大阪(おおさか)',
 '兵庫県(ひょうご)':'神戸(こうべ)',
 '奈良県(なら)':'奈良(なら)',
 '和歌山県(わかやま)':'和歌山(わかやま)',
 '鳥取県(とっとり)':'鳥取(とっとり)',
 '島根県(しまね)':'松江(まつえ)',
 '岡山県(おかやま)':'岡山(おかやま)',
 '広島県(ひろしま)':'広島(ひろしま)',
 '山口県(やまぐち)':'山口(やまぐち)',
 '徳島県(とくしま)':'徳島(とくしま)',
 '香川県(かがわ)':'高松(たかまつ)',
 '愛媛県(えひめ)':'松山(まつやま)',
 '高知県(こうち)':'高知(こうち)',
 '福岡県(ふくおか)':'福岡(ふくおか)',
 '佐賀県(さが)':'佐賀(さが)',
 '長崎県(ながさき)':'長崎(ながさき)',
 '熊本県(くまもと)':'熊本(くまもと)',
 '大分県(おおいた)':'大分(おおいた)',
 '宮崎県(みやざき)':'宮崎(みやざき)',
 '鹿児島県(かごしま)':'鹿児島(かごしま)',
 '沖縄県(おきなわ)':'那覇(なは)'
 }

for quiz_num in range(1):
    #問題集と解答集のファイルを作成する
    quiz_file = open('capitalsquiz{}.txt'.format(quiz_num+1),'w')
    answer_key_file = open('capitalsquiz_answer{}.txt'.format(quiz_num+1),'w')

    #問題集にヘッダーを記入
    quiz_file.write('名前:\n\n 日付:\n\n')
    quiz_file.write((' ' * 20) + '都道府県庁所在地クイズ(問題番号{})'.format(quiz_num + 1))
    quiz_file.write(' \n\n')
    
    #都道府県の順番をシャッフルする
    prefectures = list(capitals.keys())
    random.shuffle(prefectures)
    
    #都道府県をループしてそれぞれの問題を作成する
    for question_num in range(len(prefectures)):
        #正解と誤答を取得
        correct_answer = capitals[prefectures[question_num]]
        wrong_answers = list(capitals.values())
        del wrong_answers[wrong_answers.index(correct_answer)]
        wrong_answers = random.sample(wrong_answers,3)
        answer_options = wrong_answers + [correct_answer]
        random.shuffle(answer_options)

        #問題と解答選択肢を問題ファイルに書き込む
        quiz_file.write('{}.{}の都道府県所在地は？\n'.format(question_num +1, prefectures[question_num]))
        for i in range(4):
            quiz_file.write('{}.{}\n'.format('ABCD'[i],answer_options[i]))
        
        quiz_file.write('\n')
        #答えの選択肢をファイルに書く
        answer_key_file.write('{}. {}\n'.format(question_num + 1, 'ABCD'[answer_options.index(correct_answer)]))

    quiz_file.close()
    answer_key_file.close()
    
    