'''
Q2. Maximize the chocolates
  tags:  amazon  dynamic programming  companies
Time Limit: 0ms
Hardness Level: 9 out of 10
Question:

Guvi loves chocolates, so little guvi goes to caffeteria to get chocolates, The chocolates are arranged in trays and the trays are arranged in different racks, each tray has different number of chocolates. So little guvi can remove N number of  trays present in S number of racks . The number of trays in each rack are similar. Help guvi to remove N number of trays so that the sum of the chocolates on the trays are maximum after removal.
Input:
First line contains Number of Racks R 1 <=R <=10^5. Second Line contains the number of trays S present in each rack 1<=S<=10^5. Third Line contains Number of trays to remove(N). Next R line contains S space separated integers.
Output:
Output an integer containing number of chocolates
Sample Testcase:
Input:

2
4
2
2 6 4 5
1 6 15 10 

Output:

17

Explanation:
Current sum of the no of chocolates at the top = 2 + 1 = 3. removing 1 from top of the second tray only makes the sum 8 (5 + 2 = 8) removing 2 from the top of the second tray only makes the sum 7 (6 + 1). removing both 1 and 2 from the top of each tray makes the sum 12 (6 + 6). removing 2 and 6 from the first tray makes the sum 5 (4 + 1). removing 1 and 6 from the second tray leaves 15 as the element at the top. Hence, the sum of no of chocolates at the top of the two trays is maximized (15 + 2 = 17).
Actual Testcases:
Testcase 1:
Input:

2
4
3
2 6 4 5
1 6 15 10 

Output:

21

Testcase 2:
Input:

2
20
2
1 2 3 4 5 6 7 8 9 1 1 1 1 1 3 4 5 6 7 87
78 7 6 5 4 3 1 1 1 1 1 9 8 7 6 5 4 3 2 1

Output:

81

Testcase 3:
Input:

2
20
10
1 2 3 4 5 6 7 8 9 1 1 1 1 1 3 4 5 6 7 87
78 7 6 5 4 3 1 1 1 1 1 9 8 7 6 5 4 3 2 1

Output:

87

Testcase 4:
Input:

4
30
15
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30
17 29 2 6 9 28 18 10 13 21 26 3 5 30 11 8 20 12 4 23 7 22 1 15 16 14 27 24 25 19
2 30 3 10 13 5 20 4 25 8 9 17 29 18 22 12 15 26 16 14 23 24 19 28 7 21 6 27 11 1
29 30 15 21 22 19 6 26 12 28 20 25 3 4 27 14 13 1 8 16 7 17 23 5 24 11 18 2 9 10

Output:

102

Testcase 5:
Input:

4
30
28
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30
17 29 2 6 9 28 18 10 13 21 26 3 5 30 11 8 20 12 4 23 7 22 1 15 16 14 27 24 25 19
2 30 3 10 13 5 20 4 25 8 9 17 29 18 22 12 15 26 16 14 23 24 19 28 7 21 6 27 11 1
29 30 15 21 22 19 6 26 12 28 20 25 3 4 27 14 13 1 8 16 7 17 23 5 24 11 18 2 9 10

Output:

115
'''
def maximumSum(S, M, N, stacks): 
  
    # Constructing a dp matrix 
    # of dimensions (S+1) x (N+1) 
    dp = [[0 for x in range(N + 1)]  
             for y in range(S + 1)] 
  
    # Loop over all i stacks 
    for i in range(S): 
        for j in range(N + 1): 
            for k in range(min(j, M) + 1): 
                dp[i + 1][j] = max(dp[i + 1][j],  
                                   stacks[i][k] + 
                                   dp[i][j - k]) 
  
    result = -sys.maxsize - 1
    for i in range(N + 1): 
        result = max(result, dp[S][i]) 
  
    return result 
  

if __name__ == "__main__": 
    
    R=int(input())
    S=int(input())
    N=int(input())
    stacks=[]
    for _ in range(0,R):
        stacks.append(list(map(int,input().split())))
    print(maximumSum(R, S, N, stacks)) 
