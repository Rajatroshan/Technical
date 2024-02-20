def check(ans1,ans2):
    if(ans1.lower()=='yes') or (ans2.lower()=='yes'):   
        return True
    elif(ans1.lower()=='no') and (ans2.lower()=='no'):
        return  False

print("Hey User")
ans1=input("is it raining Yes or no? :")
ans2=input("is it snowing Yes or no? :")
print(check(ans1,ans2))