# The sum of all the multiples of 3 or 5 below 1000
# First: the last number less than 1000 that can be divided by 3 is 999 so "999/3=333" so the range of the first for loop between (1,333)
# Second: // // // by 5 is 995 so "995/5=199" so the range of the second for loop between (1, 199)

Multiple_of_3 = []
for i in range(334):
    z = 3 * i
    Multiple_of_3.append(z)

Multiple_of_5 = []
for j in range(200):
    x = 5 * j
    if x % 3 == 0:
        continue
    else:
        Multiple_of_5.append(x)

# The final answer
print(sum(Multiple_of_3) + sum(Multiple_of_5))

