"""
The list of odd numbers[1,3,5,7,9,11,13,15….] have been split into the following sets:
		{1},{3,5},{7,9,11},{13,15,17,19}.....
In general, the kth set has the k next odd numbers, starting from the first number in the kth set.
For example, at k=5, the set is {21,23,25,27,29}
 
Given the number k, find the sum of the kth set.

Input Format: A single number, K
Output Format: A single number, the sum of the Kth subset.
"""


n=int(input())
print(n**3)