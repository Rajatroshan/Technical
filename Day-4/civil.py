def surface(x, y):
    surfaceori=x*y
    x1=x-1
    y1=y-1
    newsurface=x1*y1
    return newsurface,surfaceori


len1=int(input("Enter the width"))
len2=int(input("Enter the length"))
n1,n2=surface(len1,len2)
border=n2-n1

print(f"The new surface area is {n1}")
print(f"The extra border added to the original surface area is {border}")