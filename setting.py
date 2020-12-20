#Beatwalls関数名リスト
func_name = {\

#ひらがな
#例：「あ」　->　関数名：hira_A
'hira' : ['A', 'I', 'U', 'E', 'O', 'KA', 'KI', 'KU', 'KE', 'KO', 'SA', 'SHI', 'SU', 'SE', 'SO', \
        'TA', 'CHI', 'TSU', 'TE', 'TO', 'NA', 'NI', 'NU', 'NE', 'NO', 'HA', 'HI', 'FU', 'HE', 'HO', \
        'MA', 'MI', 'MU', 'ME', 'MO', 'YA', 'YU', 'YO', 'RA', 'RI', 'RU', 'RE', 'RO', \
        'WA', 'WI', 'WE', 'WO', 'N', 'GA', 'GI', 'GU', 'GE', 'GO', 'ZA', 'ZI', 'ZU', 'ZE', 'ZO', \
        'DA', 'DI', 'DU', 'DE', 'DO', 'BA', 'BI', 'BU', 'BE', 'BO', 'PA', 'PI', 'PU', 'PE', 'PO', \
        'VU', 'LA', 'LI', 'LU', 'LE', 'LO', 'LTSU', 'LYA', 'LYU', 'LYO', 'LWA'],\

#カタカナ
#例：「ア」　->　関数名：kata_A
'kata' : ['A', 'I', 'U', 'E', 'O', 'KA', 'KI', 'KU', 'KE', 'KO', 'SA', 'SHI', 'SU', 'SE', 'SO', \
        'TA', 'CHI', 'TSU', 'TE', 'TO', 'NA', 'NI', 'NU', 'NE', 'NO', 'HA', 'HI', 'FU', 'HE', 'HO', \
        'MA', 'MI', 'MU', 'ME', 'MO', 'YA', 'YU', 'YO', 'RA', 'RI', 'RU', 'RE', 'RO', \
        'WA', 'WI', 'WE', 'WO', 'N', 'GA', 'GI', 'GU', 'GE', 'GO', 'ZA', 'ZI', 'ZU', 'ZE', 'ZO', \
        'DA', 'DI', 'DU', 'DE', 'DO', 'BA', 'BI', 'BU', 'BE', 'BO', 'PA', 'PI', 'PU', 'PE', 'PO', \
        'VU', 'LA', 'LI', 'LU', 'LE', 'LO', 'LTSU', 'LYA', 'LYU', 'LYO', 'LWA', 'LKA', 'LKE'],\

#英語アルファベット
#例：「A」　->　関数名：eng_A
'eng' : ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',\
       'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',\
       'LA', 'LB', 'LC', 'LD', 'LE', 'LF', 'LG', 'LH', 'LI', 'LJ', 'LK', 'LL', 'LM',\
       'LN', 'LO', 'LP', 'LQ', 'LR', 'LS', 'LT', 'LU', 'LV', 'LW', 'LX', 'LY', 'LZ'],\

#数字・記号
#例：「?」　->　関数名：mark_Question
'mark' : ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'Plus', 'Minus', 'Multi', 'Div', 'Equal',\
        'jpComma', 'jpPeriod', 'Comma', 'Period', 'Apostrophe', 'Hat', 'Colon', 'SemiColon',\
        'jpLongSound', 'WaveDash', 'Exclamation', 'Question', 'Sharp', 'Dollar', 'Percent', 'And',\
        'Yen', 'Postal', 'QuarterNote', 'At', 'Asterisk', 'VerticalBar', 'Underscore', 'Slash',\
        'BackSlash', 'jpAsterisk', 'Star', 'Heart', 'Square', 'Triangle', 'Circle', 'DoubleCircle',\
        'UpArrow', 'DownArrow', 'LeftArrow', 'RightArrow', 'AngleBracket0', 'AngleBracket1',\
        'Parentheses0', 'Parentheses1', 'CornerBracket0', 'CornerBracket1', 'Braces0', 'Braces1',\
        'BoxBrackets0', 'BoxBrackets1', 'LenticularBracket0', 'LenticularBracket1', \
        'WhiteCornerBracket0', 'WhiteCornerBracket1'],\
}


#画像ピクセル数
letter_width = 76 #1文字画像幅
letter_hight = 76 #1文字画像高
letter_space = 0.8 #文字間
line_space = 16 #行間

#素材画像中の文字数
n_row = 6 #行数
n_column = 15 #列数

#フォント構成ドット
n_dot_x = 16 #フォント幅
n_dot_y = 16 #フォント高
dot_width = (letter_width+letter_space)/n_dot_x #1ドットのピクセル幅
dot_hight = (letter_hight+letter_space)/n_dot_y #1ドットのピクセル高

#Beatwalls座標系に対する1ドットのスケール
scale = 0.25