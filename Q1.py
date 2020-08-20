'''
Q1. Peter Vs John
  tags:  basic io math  basics
Time Limit: 1000ms
Hardness Level: 2 out of 10
Question:

There is a boxing match between peter and john peter has a unique way of fighting he does not attack, but he tries to defend himsef and make john  tire himself out.

John has a initial power of P. He keeps attacking peter. Every time John hits, Peter's health decreases by the current power of the John (by P points), and afterwards, Johns power P decreases to P/2.

If the attack power becomes 0 before Peter's health becomes 0 or less, John dies. Otherwise, Peter dies. You are given Peter's initial health H and John's initial attack power P.If both the powers get zero at same time its a Tie. Guess who will win the match if John wins output the Number of attacks made by him if Peter wins output the health left
Input:
The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows. The first and only line of each test case contains two space-separated integers H and P. 1≤T≤10^5 1≤P≤10^5 1≤H≤10^6
Output:
For each test case, print a single line containing the integer Number of attacks if John wins and Health Remaining if Peter Wins and Print "Tie" if it is a tie
Sample Testcase:
Input:

1
10 4

Output:

3

Explanation:
T=1 , H=10, P=4 For the first attack by John health of Peter becomes 6 and power becomes 2 for the second attack health of Peter Becomes 4 and power of John becomes 1 and so on. So Peter wins the match the remaining health of peter is 3
Actual Testcases:
Testcase 1:
Input:

1
8 4

Output:

1

Testcase 2:
Input:

2
2 4
4 3

Output:

1
Tie

Testcase 3:
Input:

1
12 10

Output:

2

Testcase 4:
Input:

5
11 4
12 6
1 2
10 10
10 6

Output:

4
2
1
2
Tie

Testcase 5:
Input:

1
100000000 25000000

Output:

50000012
'''
t= int(input())
while t>0:
    t=t-1
    n=0
    a,b = map(int,input().split())
    sum=0
    while b!=0:
        sum=sum+b
        b=b//2
        n=n+1
        if sum>a:
            break
    if sum>a:
        print(n)
    elif sum==a:
        print("Tie")
    else:
        print(a-sum)
