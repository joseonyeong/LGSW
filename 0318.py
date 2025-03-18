print("로그인 로직")
passwd = 1111
inputpasswd = int(input("패스워드 입력: "))
if passwd == inputpasswd:
    print("로그인 성공")
else:
    print("비번이 틀렸습니다.")

print("BMI 계산기_등급출력")
weight = float(input("몸무게 입력: "))
height = float(input("키 입력: "))
bmi = weight / height**2
if bmi < 18.5:
    print("저체중입니다.")
elif bmi >= 18.5 or bmi < 23:
    print("정상입니다.") 
elif bmi >= 23 or bmi < 25:
    print("과체중입니다.")
else:
    print("비만입니다.")

print("while문으로 반복 번수 출력")
num = int(input("숫자를 입력하세요: "))
while num > 0: #조건은 해당 코드가 돌 수 있는 조건
    print(num)
    num -= 1

print("3의 배수 출력")
for i in range (1,101):
    print(i*3, end=' ')

print("구구단 출력_사용자에게 숫자 받기")
dan = int(input("단수를 입력하세요: "))
for i in range(1,11):
    print(f"{dan} * {i} = {dan*i}")

# 무한루프로 돌리되, 0을 누르면 끝내게 만들어보자    
while True:
    dan2 = int(input("단수를 입력하세요(끝내려면 0을 누르세요.): "))
    if dan2==0:
        break
    for i in range(1,11):
        print(f"{dan2} * {i} = {dan2*i}")

