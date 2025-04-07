def print_simple_welcome(name):
    msg1 = f"Hello, {name}!"
    msg2 = "Welcome to Seoul"

    
    nstr = len(msg1) if len(msg1) > len(msg2) else len(msg2)

    
    print("-" * (nstr + 4))
    print(msg1)
    print(msg2)
    print("-" * (nstr + 4))


name = input("Enter the English name of your friend: ")
print_simple_welcome(name)
