print("모든 구구단 출력_중첩 for문")
for i in range(2,10):
    for j in range(1,10):
        print(f"{i} * {j} = {i*j:>2}")
    # 9단 아래에는 나타나지 않도록 하기 위해 if문 설정
    if i <9:   
        print("--------------")
        
j = 4
# 공백도 for문을 넣으면 원하는 모양이 안나옴
# *만 for문을 넣고 공백을 j개 출력하는 변수는 따로 생성
for i in range(1,11,2):
    print(" " * j, end='')
    print('*' * i)
    j -= 1