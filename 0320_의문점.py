print("행렬 곱셈")
a = [[1,0,1],[0,2,0],[1,2,1]]
b = [[2,3,1],[0,1,1],[1,1,1]]
c = []
# # 00*00+01*10   00*01+01*11     00*02+01*12
# # 10*00+11*10   10*01+11*11     10*02+11*12

tmp = []
for i in range(len(a)):
    row = []
    for j in range(len(b[0])):
        sum = 0
        for n in range(len(a[0])):
            sum += a[i][n] * b[n][j]
        row.append(sum) # 원소 하나 (더해진 값)
    tmp.append(row)   # 행 한 줄
# tmp.append(row)   # 일차원 배열로 저장
print(tmp)