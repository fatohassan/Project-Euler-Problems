# The sum of all the multiples of 3 or 5 below 1000
# First the last number less than 1000 that can be divided by 3 is 999 so "999/3=333" so the range of the first for loop betwwen (0,334)
# Second // // // by 5 is 995 so "995/5=199" so the range of the second for loop between (0, 200)

Multiple_of_3 = []
for i in range(0, 334):
    z = 3
    z = z * i
    Multiple_of_3.append(z)

Multiple_of_5 = []
for j in range(0, 200):
    x = 5
    x = x * j
    Multiple_of_5.append(x)

# Put the multiples of 3 and 5 in sets
set1 = set(Multiple_of_3)
set2 = set(Multiple_of_5)

# Take the union of sets to avoid duplicate multiples
union = list(set1.union(set2))

# The final answer
print(sum(union))

