print('HelloWorld!')
print(2323)

#변수
print()
print('---- 변수 ----')

name = '송유진'
print(name)

twenty_three = 23
print(twenty_three)

#List
print()
print('---- list ----')

중고차 = ['k5', 'white', 5000]
print(중고차)
print(중고차[0])
print(중고차[1])
print(중고차[2])

중고차[1] = 'black'
print(중고차[1])

#Dictionary
print()
print('---- Dictionary ----')

중고차2 = {'brand' : 'bmw', 'model' : '520d'}
print(중고차2)
print(중고차2['brand'])
print(중고차2['model'])

#if 조건문
print()
print('---- if ----')

재고량 = 10
if 재고량 > 0 :
    print('주문가능합니다')

중고차재고 = ['k5', 'bmw', 'tico']
if 'k6' in 중고차재고 :
    print('주문가능합니다')
else :
    print("주문불가능합니다")

if 'k6' in 중고차재고 :
    print('주문가능합니다')
elif 'bmw' in 중고차재고 :
    print('bmw 주문가능합니다')
else :
    print("주문불가능합니다")

#for 반복문
print()
print('---- for ----')

for i in range(0, 10) :
    print('try i times')

print()

for i in range(0, 10) :
    print(f'try {i} times')

#def 함수
print()
print('---- def ----')

def hello() :
    print('hello, my name is yujin song. 22 years old')

hello()

def plus(i) :
    i += 1
    print(i)

plus(22)

#new theme
print()
print('---- test theme ----')

print('record this')

number = [2, 23 , 34, 55]

if 23 in number :
    print('23 is exist')
else :
    print('23 is not exist')