# Question 1
# def maximize(a,b,c):
#     if a>b and a>c:
#         print("A is greatest")
#     elif b>c:
#         print("B is greatest")
#     else:
#         print("C is greatest")
# maximize(2,3,4)

# Question 2
# def celsius(c):

#     f=((c*9)/5)+32
#     return f

# print(celsius(45))

# question 3
sum=0
def natural(n):
    while n>0:
        sum=n+natural(n-1)

        
    return sum

print(natural(3))
