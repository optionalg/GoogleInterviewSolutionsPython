def solution(A,K):
    ma = [0]*K
    for i in range(len(A)-K+1):
        if(ma<A[i:i+K]):
            ma = A[i:i+K]
    return ma
