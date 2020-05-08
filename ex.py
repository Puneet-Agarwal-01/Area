a = input("Enter the name of your file:")
e = a[-2:]
if e == 'py':
    print("Python")
elif e == '.c':
    print("C")
elif e == 'pp':
    print("C++")
elif e == 'av':
    print("Java")
elif e == 'js':
    print("Javascript")
else:
    print("Invalid Input")
