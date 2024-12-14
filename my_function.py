b = "today"  # global
def hello():
    a = 'monday'  # local
    print("hello")

def display_name(name):
    print(f"hello {name}")
    #print(a)
    print(b)
def addition(a,b):
    sum = a + b
    print(sum)
def addition1(a,b):
    sum = a + b
    return sum
        
def command(cmd):
    import os
    os.system(cmd)
    
def main():
    my_value = addition1(2,7)
    print(my_value)
        
if __name__=='__main__':
    main()