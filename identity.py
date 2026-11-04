x = 44
if (type(x) is float):
    print("true")
else:
    print("false")

x = 34.4
if type(x) is not float:
    print("true")
else:
    print("false")

y = 12
z = 12
if (y is z):
    print("True same identity")

y = 34
z = 35
if (y is not z):
    print("true different identity")
else:
    print("false same identity")