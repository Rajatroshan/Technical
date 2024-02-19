def outer():
    name="hello"
    
    def inner():
        nonlocal name
        print(name)
        name="goo"
        return name
    
    name=inner()
    print(name)
 
outer()