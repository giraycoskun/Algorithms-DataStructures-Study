# Unlock The Padlock
# KickStart 2022 Round B
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008caa74/0000000000acef55#analysis

def solve(i, j, k) -> int:
    if i > j:
        return 0
    if dp[i][j][k] != -1:
        return dp[i][j][k]

    current_val_i = (padlock[i] - k + D) % D
    current_val_j = (padlock[j] - k + D) % D

    current_operations = min(current_val_i, D - current_val_i)
    val_1 = current_operations + solve(i+1, j, (k+current_operations)%D)

    current_operations = min(current_val_j, D-current_val_j)
    val_2 = current_operations + solve(i, j-1, (k+current_operations)%D)

    dp[i][j][k] = min(val_1, val_2)
    return dp[i][j][k]


#test_count = int(input())
test_count = 1
for c in range(test_count):
    # test = list(map(int, input().split()))
    test = list(map(int, "6 10".split()))
    # padlock = list(map(int, input().split()))
    padlock = list(map(int, "1 1 9 9 1 1".split()))
    N = test[0]
    D = test[1]

    dp = []
    for i in range(N):
        temp = []
        for j in range(N):
            temp2 = []
            for k in range(D):
                temp2.append(-1)
            temp.append(temp2)
        dp.append(temp)

    answer = solve(0, N - 1, 0)

    print("Case #{case_no}: {answer}".format(case_no=c + 1, answer=answer))
