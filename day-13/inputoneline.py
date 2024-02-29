#taking input in oneline and sum of the

def sum(num):
    sum1=0
    for i in num:
        sum1=sum1+i
    return sum1


num=eval(input("Enter number : "))
print(sum(num))

#Write a program to remove the duplicates from the list
k=eval(input("Enter the length"))
m=[]
for i in range(k):
    s=int(input("Enter the elements : "))
    if s not in m:
        m.append(s)
print(m)

#implement the function list having a even number
m=[]
def even(n):
    for i in  n:
        if i%2==0:
            m.append(i)
    return m
  

s=eval(input("Enter the number"))
print(even(s))

#same words in alphabatical order   
w=str(input("Enter the word : ")).split()
w=sorted(w,key=lambda x: ord(x[0])) 
print(' '.join(w))


#take the list of number and find second largest number
f=eval(input("Enter the number"))
j=list(f)
j.sort()
print(j)
l=len(j)-2
print("Second largest number is",j[l])


#viowel starting
def only_vowles(inputString):
    splited=inputString.split(" ")
    vowles=["a","e","i","o","u"]
    ans=[]
    for i in splited:
        j=i.lower()
        if j[0] in vowles:
            ans.append(i)
    return ans
            
string=input("Enter the string: ")
print(only_vowles(string))


