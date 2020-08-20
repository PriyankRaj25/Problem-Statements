'''
Q3. Size Matters
  tags:  amazon
Time Limit: 2200ms
Hardness Level: 6 out of 10
Question:

Guvi love's arrays, he planned to design a strong array. The array is considered to be strong if sum of any combination of the elements in the array results to the given weight. Help guvi to solve this problem write a program to check if the arrays is strong or not.
Input:
First Line Contains T number of test cases ranging from 1<=T<=10^5 Next T lines contain Length of array integer N N space separated integers Expected Sum
Output:
Output Strong or Not
Sample Testcase:
Input:

1
5
3 34 4 12 5 2
9

Output:

Strong

Explanation:
The array has 4 and 5 so it is Strong
Actual Testcases:
Testcase 1:
Input:

2
30
17 29 2 6 9 28 18 10 13 21 26 3 5 30 11 8 20 12 4 23 7 22 1 15 16 14 27 24 25 19
200
30
17 29 2 6 9 28 18 10 13 21 26 3 5 30 11 8 20 12 4 23 7 22 1 15 16 14 27 24 25 19
21

Output:

Strong
Strong

Testcase 2:
Input:

2
30
17 29 2 6 9 28 18 10 13 21 26 3 5 30 11 8 20 12 4 23 7 22 1 15 16 14 27 24 25 19
2000
30
17 29 2 6 9 28 18 10 13 21 26 3 5 30 11 8 20 12 4 23 7 22 1 15 16 14 27 24 25 19
1000

Output:

Not
Not

Testcase 3:
Input:

1
10
100 197 2002 20000 12345 1999 102 104 105 1090
122234

Output:

Not

Testcase 4:
Input:

1
10
100 197 2002 20000 12345 1999 102 104 105 1090
21287

Output:

Strong

Testcase 5:
Input:

1
10
100 197 2002 20000 12345 1999 102 104 105 1090
21289

Output:

Not
'''
def isSubsetSum(set, n, sum):
    subset =([[False for i in range(sum + 1)]  
            for i in range(n + 1)])
      
    for i in range(n + 1):
        subset[i][0] = True
          
    for i in range(1, sum + 1):
         subset[0][i]= False
              
    for i in range(1, n + 1):
        for j in range(1, sum + 1):
            if j<set[i-1]:
                subset[i][j] = subset[i-1][j]
            if j>= set[i-1]:
                subset[i][j] = (subset[i-1][j] or
                                subset[i - 1][j-set[i-1]])
      
    return subset[n][sum]
          
if __name__=='__main__':
    t=int(input())
    while(t>0):
        n=int(input())
        set = list(map(int,input().split()))
        sum = int(input())
        if (isSubsetSum(set, n, sum) == True):
            print("Strong")
        else:
            print("Not")
