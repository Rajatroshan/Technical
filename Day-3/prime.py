# def prime(num):      #It is a function 
#     if num <= 1:      
#         return false
#     elif num <=3:        
#         return True
#     elif  num % 2 == 0 or num % 3 == 0:  
#         return False   
#     i=5
#     while i * i <= num:
#         if num % i == 0 or num % (i + 2) == 0 :
#             return False
#         i=i+6
#     return True

# #num=int(input("Enter a number"))

# # if  prime(num):
# #     print("It is a prime number")
# # else:
# #     print("Not a prime number")

# for i in range(10000):
#     if prime(i):
#         print(i,end=" ")
    
def prime(data):
    if data == 2:
        return "It is a prime & even number"
    
    for i in range(2,data):
        if data % i == 0:
            return "It is not a prime number"
    return "This is a prime number"

print(prime(5))