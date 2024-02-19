def outer():
    name="hello"
    
    # def inner(name):
    #     print(name)
    #     name="goo"
    #     return name
    
    # name=inner(name)

    def inner():
        nonlocal name
        print(name)
        name="goo"
        return name
    
    name=inner()
    print(name)
 
outer()