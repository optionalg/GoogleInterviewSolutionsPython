def solution(A, B):
    # write your code in Python 2.7
    a = A.split(" ")
    b = B.split(" ")
    arr1 = []
    arrC =[]
    arr = []
    for i in range(len(a)):
      minA = min(a[i])
      arr.append(a[i].count(minA))
    for i in range(len(b)):
      minB = min(b[i])
      arrC.append(b[i].count(minB))
    arr.sort()
    arrC
    for each in arrC:
      arr1.append(sum(j < each for j in arr))
    return arr1
