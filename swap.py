# a = int(input("enter a:"))
# b = int(input("enter b:"))


# d = a
# a = b
# b = d

# print('swap value of a',a)
# print('swap value of b',b)

#ANOTHER APPRROACH by using comma operator

a = int(input('enter a :'))
b = int(input('enter b  :'))

a,b = b,a

print('after swap a:',a)
print('after swap b:',b)