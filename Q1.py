def solution(A, B):
    # write your code in Python 2.7
    a = A.split(" ")
    b = B.split(" ")
    arr1 = []
    arrC =[]
    arr = []
    minA = min(a)
    minB = min(b)
    for i in range(len(a)):
      arr.append(a.count(minA))
    for i in range(len(b)):
      arrC.append(b.count(minB))
    arr.sort()
    arrC.sort()
    for each in b:
      arr1.append(sum(i > each for i in a))
    return arr1
