for i in range(0, 3, 1):
    print("안녕하세요? for 문을 공부 중입니다.^^")

for i in range(1, 100, 2):
    print("%d " % i, end="")

for i in range(2, 100, 2):
    print("%d " % i, end="")

i, hap = 0,0

for i in range(1, 11, 1):
    hap = hap+i

print("1에서 10까지의 합계 : %d" % hap)

i, hap = 0,0

for i in range(1, 101, 2):
    hap = hap+i

print("1에서 100까지의 합계 : %d" % hap)

i, hap = 0,0

for i in range(2, 101, 2):
    hap = hap+i

print("2에서 100까지의 합계 : %d" % hap)

i, dan = 0, 0

dan = int(input("단을 입력하세요: "))
for i in range(1, 10, 1):
    print("%d * %d = %2d" % (dan, i, dan*i))

for i in range(0, 3, 1):
    for k in range(0, 2, 1):
        print("파이썬은 꿀잼입니다.^^ (i값 : %d, k값 : %d)" % (i, k))

for i in range(2, 10, 1):       
    print(f" {i}단 ")
    for k in range(1, 10, 1):
        print("%d * %d = %2d" % (i, k, i * k))
    print()

i=0
while i < 3:
    print("안녕하세요? while 문을 공부 중입니다.^^")
    i =  i + 1

i, hap = 0, 0

i = i
while i < 11:
    hap = hap + i
    i = i + 1
print("1에서 10까지의 합계 : %d" % hap)

##while True:
##    print("ㅋ",end="")

for i in range(1,100):
    print("for 문을 %d만 반복합니다." % i)
    break 

hap = 0
a, b = 0, 0

##while True:
    a=int(input("더할 첫 번째 수를 입력하세요: "))
    if a==0:
        break
    b=int(input("더할 두 번째 수를 입력하세요: "))
    hap = a + b 
    print("%d + %d = %d" % (a, b, hap))

print("0을 입력해 반복문을 탈출했습니다.")

hap = 0
for i in range(1, 101):
    if i % 2 == 0:
        continue

    hap += i

print("1~100의 합계(3의 배수 제외) : %d" % hap)

for k in range(9, 0, -1):          
    for i in range(9, 1, -1):    
        print("%d * %d = %2d" % (i, k, i * k), end="\t")
    print()                        




for k in range(1, 10):          
    for i in range(2, 10):     
        print("%d * %d = %2d" % (i, k, i * k), end="\t")
    print()                  



for i in range(1, 51):
    print("*" * i)

 
print("\n\n\n")


for i in range(50, 0, -2):
    spaces = " " * ((50 - i) // 2)
    stars = "*" * i
    print(spaces + stars)


for i in range(4, 51, 2):
    spaces = " " * ((50 - i) // 2)
    stars = "*" * i
    print(spaces + stars) 