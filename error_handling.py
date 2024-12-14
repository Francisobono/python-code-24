
try:
    print(a)
except NameError:
    print("Error: variable a not define")
else:
    print("no Error")
finally:
    print("Always")