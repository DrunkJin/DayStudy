# 약수의 합
def solution(n):
    answer = 0
    # for i in range(1,n+1):
    #     if n%i == 0:
    #         answer+=i
    answer = sum([x for x in range(1,n+1) if n%x==0]) 
    return answer

# 테스트 1 〉	통과 (0.00ms, 10.1MB)
# 테스트 2 〉	통과 (0.01ms, 10.2MB)
# 테스트 3 〉	통과 (0.04ms, 9.94MB)
# 테스트 4 〉	통과 (0.03ms, 10.1MB)
# 테스트 5 〉	통과 (0.10ms, 9.97MB)
# 테스트 6 〉	통과 (0.06ms, 10.2MB)
# 테스트 7 〉	통과 (0.15ms, 10.1MB)
# 테스트 8 〉	통과 (0.03ms, 10MB)
# 테스트 9 〉	통과 (0.14ms, 10.1MB)
# 테스트 10 〉	통과 (0.28ms, 9.98MB)
# 테스트 11 〉	통과 (0.16ms, 10.1MB)
# 테스트 12 〉	통과 (0.11ms, 10.2MB)
# 테스트 13 〉	통과 (0.02ms, 10.1MB)
# 테스트 14 〉	통과 (0.10ms, 10.2MB)
# 테스트 15 〉	통과 (0.16ms, 10.2MB)
# 테스트 16 〉	통과 (0.00ms, 10.3MB)
# 테스트 17 〉	통과 (0.27ms, 10MB)