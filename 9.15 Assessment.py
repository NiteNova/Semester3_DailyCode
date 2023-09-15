#python for loops question 4
for i in range(15, -21, -5):
    print(i)

print()

#advanced preview/review
def BiggestOfThree(a, b, c):
    g = 0
    if a > g:
        g = a
    if b > g:
        g = b
    if c > g:
        g = c
    return g

print("Biggest one:", BiggestOfThree(2, 1, 2))
print()

lol = []
for _ in range(10):
    user = int(input("Enter number: "))
    lol.append(user)
print("First List check:", lol)

bruh = []
for m in range(len(lol)):
    k = lol[m] * 2
    bruh.append(k)
print("Second List check:", bruh)
