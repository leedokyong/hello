import random
print('hello,world!')
print('짜장면 or 짬뽕')
# 만약에 짜짱면과 짬뽕 둘중에 하나 추천
# 내가 짜장이나 짬뽕을 적으면 짜장이나 짬뽕중에 추천 
# 둘다 아니면 (짜짬면)
a = input('먹고 싶은거 입력 : ')
print(f'입력한 값 : {a}')
# print('입력한 값 :' , a)
# print('입력한 값 : %s' %a)
# print('입력한 값 : {0}' , format(a))
menu = '짜장면' , '짬뽕'
if a == '짜장면' or a == '짬뽕' :
    print('나오나') # 참일때만 여기 출력
    #여기에서 짜장과 짬뽕중에 인공지능이 추천해주는 결과는?
    print('인공지능이 추천해주는')
    m = random.choice(menu)
    print(f'{m} 먹어!!')

else:
    print('짬짜면 먹엉')