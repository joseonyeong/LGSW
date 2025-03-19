# print("모든 구구단 출력_중첩 for문")
# for i in range(2,10):
#     for j in range(1,10):
#         print(f"{i} * {j} = {i*j:>2}")
#     # 9단 아래에는 나타나지 않도록 하기 위해 if문 설정
#     if i <9:   
#         print("--------------")

# print("반쪽 별")
# for i in range(1,6):
#     print('*' * i)

# print('중첩 for문으로 반쪽 별')
# for j in range(5):
#     for i in range(j+1):
#         print('*', end='')
#     print()
    
# print("거꾸로 반쪽 별")
# for i in range(5,0,-1):
#     print('*' * i)
    
# for j in range(5,0,-1):
#     for i in range(j):
#         print('*', end='')
#     print()

# # print('별')
# # 공백 j개 i 공백 4개
# # 공백 j-1개 i+2 공백 3개
# # 공백 2개 ***** 공백 2개
# # 공백 1개  공백 1개
# # 공백 0개  공백 0개
# j = 4
# # 공백도 for문을 넣으면 원하는 모양이 안나옴
# # *만 for문을 넣고 공백을 j개 출력하는 변수는 따로 생성
# for i in range(1,11,2):
#     print(" " * j, end='')
#     print('*' * i)
#     j -= 1

# print('f-string 사용해서 별 찍기')
# n = int(input('별 개수: '))
# for i in range(1,n+1,2):
#     star = '*' * i
#     print(f"{star:^{n}}")

# # 2단 == 3개 차이 1개
# # 3단 == 5개 차이 2개
# # 4단 == 7개 차이 3개
# # 5단 == 9개 차이 4개
# print('f-string 사용해서 별 찍기')
# n = int(input('원하는 층수: '))
# i = 0
# for dan in range(1,n+1,1):
#     star = '*' * (dan+i)
#     # 입력받은 dan과 마지막 별 개수 차이는 단수 2배 - 1 규칙성을 가짐
#     print(f"{star:^{n*2-1}}")
#     i += 1


