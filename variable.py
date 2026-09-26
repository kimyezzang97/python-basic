animal = '강아지'
name = '연탄'
age = 4
hobby = '산책'
is_adult = age >= 3


print('우리집 ' + animal + '의 이름은' + name + '입니다.')
print(name + '는 ' + str(age) + '살 이며, ' + hobby + '을 아주 좋아해요')
print(name , '는 ' , age , '살 이며, ' , hobby + '을 아주 좋아해요') # ,로 이어 붙일시 str 메서드 제거 가능, 그러나 띄어쓰기 자동 추가

print(name + '는 어른일까요? ' + str(is_adult))