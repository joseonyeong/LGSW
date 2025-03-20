# print("성적_선생님.ver")
# scores = [[90,85,93],
#           [78,92,89]]
# total_by_student = [0,0]
# total_by_subject = [0,0,0]
# for st in range(len(scores)):
#     for sb in range(len(scores[0])):
#         total_by_student[st] += scores[st][sb]
#         total_by_subject[sb] += scores[st][sb]
# print(total_by_student)
# print(total_by_subject)

# print()
# a = [[1,0,1],[0,2,0],[1,2,1]]
# b = [[2,3,1],[0,1,1],[1,1,1]]        
# z = []
# for w in range(len(a)):
#     for h in range(len(a[0])):
#         z[w][h] = a[w][h] + b[w][h]
# print(z)       

# print("모든 원소에 곱하기 2")
# aa = [[1,2,3],[4,5,6],[7,8,9]]
# for w in range(len(aa)):
#     for h in range(len(aa[0])):
#         aa[w][h] *= 2
# print(aa) 
        
# print("행렬 덧셈")
# a = [[1,0,1],[0,2,0],[1,2,1]]
# b = [[2,3,1],[0,1,1],[1,1,1]]
# c = []
# if len(a) == len(b):
#     for i in range(len(a)):
#         row = []    # 똑같이 다차원으로 받기 위해선 행을 따로 지정해야함
#         if len(a[i]) == len(b[i]):
#             for j in range(len(a[i])):
#                 row.append(a[i][j] + b[i][j])
#             c.append(row)
#         else:
#             c = []  # 초기화
#             print("두 행렬의 열의 개수가 일치하지 않습니다.")
# else:
#     print("두 행렬의 행의 개수가 일치하지 않습니다.")
# print(c)     

# a = [1,2,3,4]
# b = [1,2,3,4]
# c = []
# num = 0
# for i in range(len(a)):
#     for j in range(len(b)):
#         num += a[i] * b[j]
#     c.append(num)
#     num = 0
# print(c)


# print("행렬 곱셈")
# a = [[1,0,1],[0,2,0],[1,2,1]]
# b = [[2,3,1],[0,1,1],[1,1,1]]
# c = []
# # num = 0

# # if len(a)>len(b):
# #     wc = len(a)
# # else:
# #     wc = len(b)
# # if len(a[0])>len(b[0]):
# #     hc = len(a[0])
# # else:
# #     hc = len(b[0])

# # # 00*00+01*10   00*01+01*11     00*02+01*12
# # # 10*00+11*10   10*01+11*11     10*02+11*12
# # for i in range(wc):
# #     for j in range(hc):
# #         num += a[i][j]*b[j][i]
# #         c.append(num)
# # print(c)
# tmp = []
# for i in range(len(a)):
#     row = []
#     for j in range(len(b[0])):
#         sum = 0
#         for n in range(len(a[0])):
#             sum += a[i][n] * b[n][j]
#         row.append(sum) # 원소 하나 (더해진 값)
#     tmp.append(row)   # 행 한 줄
# # tmp.append(row)   # 일차원 배열로 저장
# print(tmp) 

