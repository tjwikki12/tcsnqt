"""An intelligence agency has received reports about some threats. The reports consist of numbers in a mysterious method. There is a number “N” and another number “R”. Those numbers are studied thoroughly and it is concluded that all digits of the number ‘N’ are summed up and this action is performed ‘R’ number of times. The resultant is also a single digit that is yet to be deciphered. The task here is to find the single-digit sum of the given number ‘N’ by repeating the action ‘R’ number of times.

If the value of ‘R’ is 0, print the output as ‘0’.

Example 1:

Input :

99 -> Value of N

3  -> Value of R

Output :

9  -> Possible ways to fill the cistern.

Explanation:

Here, the number N=99

Sum of the digits N: 9+9 = 18
Repeat step 2 ‘R’ times i.e. 3 tims  (9+9)+(9+9)+(9+9) = 18+18+18 =54
Add digits of 54 as we need a single digit 5+4
Hence , the output is 9."""



s=input()
n=int(input())
sum=0
for i in s:
    sum+=int(i)
sum*=n
s=str(sum)
while len(s)>1:
    sum=0
    for i in s:
        sum+=int(i)
    s=str(sum)

print(s)
