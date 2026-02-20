# Set DS
# It is collection of unique elements
# It is unordered collection of elements
# It is mutable collection of elements
'''
s2=set({2,3,4,5})
print(type(s2))
print(s2)

s3=list(s2)
print(type(s3))
print(s3)

print(s3[0])

s2.add("Good")
print(s2)

s2.update({10,"Joker"})
print(s2)

s2.update({"Pokemon",900})
print(s2)

s2.remove(900)
print(s2)

s2.discard(2)
print(s2)

s2.pop()
print(s2)

s2.clear()
print(s2)

del s2
print(s2)
'''
# Set Operation
#1. Union, 2. Intersection 3. Symmetric 4. Difference
a={1,2,3,4,5}
b={2,3,4,5,6}
# a_b=a.union(b)
# print(a_b)
# a_b=a.intersection(b) # a=a&b
# print(a_b)
# a_b=a.symmetric_difference(b)
# print(a_b)
# a_b=a.difference(b)
# print(a_b)

# a_b=a|b
# print(a_b)

# a_b=a&b
# print(a_b)


# a_b=a-b
# print(a_b)



# a_b=a^b
# print(a_b)

# s1=frozenset({1,2,3,4,5})
# print(type(s1))
# print(s1)
# It don't support add and remove but it support union and intersection


# WAP to read value of N and also read N numbers print the unique numbers

# data=[]
# values=input("Enter the values: ")
# values=values.split(" ")

# for i in values:
#     data.append(int(i))

# print(set(data))

# l=[]
# l=map(int,input("Enter the values: ").split(" "))
# print(set(l))

# Wap to read value of N and also read N numbers print the sum of numbers, avg and  multiplication

# l=[]
# l=map(int,input("Enter the values: ").split(" "))
# sum=0
# mult=1
# for i in l:
#     print(i)
#     sum=sum+i
#     mult=mult*i
# print("Sum of numbers: ",sum)
# print("Multiplication of numbers: ",mult)


# l=[]
# l=map(int,input("Enter the values: ").split(" "))

# key=int(input("Enter the key: "))

# cnt=0
# for i in l:
#     if i==key:
#         cnt=cnt+1
# print(cnt)

# WAP to read N integer print the sum of all even num and mult of all odd num

# l=[]
# l=map(int,input("Enter the values: ").split(" "))

# sum_Even=0
# mult_Odd=1
# for i in l:
#     if i%2==0:
#         sum_Even=sum_Even+i
#     else:
#         mult_Odd=mult_Odd*i
# print("Sum of even numbers: ",sum_Even)
# print("Multiplication of odd numbers: ",mult_Odd)

# WAP to read a number print yes of the number is pelindrome or not

n=int(input("Enter the number: "))
temp=n
rev=0
while(n>0):
    rem=n%10
    rev=rev*10+rem
    n=n//10

if temp==rev:
    print("Yes")
else:
    print("No")
