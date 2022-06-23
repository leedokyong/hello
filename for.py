import random
for i in range(5):
    print(f'{i+1}. hello, world')
    # print(i)

    print('짜장면 or 짬뽕')
    a = input('먹고 싶은거 입력 : ')
    print(f'입력한 값 : {a}')

    menu = '짜장면' , '짬뽕'
    if a == '짜장면' or a == '짬뽕' :
        print('나오나')
        print('인공지능이 추천해주는 메뉴는?')
        m = random.choice(menu)
        print(f'{m} 먹어!!')
    else:
        print('짬짜면 먹엉')
