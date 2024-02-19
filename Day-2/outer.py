def outer():
    name="hello"
    
    def inner(name):
        print(name)
        name="goo"
        return name
    
    name=inner(name)
    print(name)
 
outer()