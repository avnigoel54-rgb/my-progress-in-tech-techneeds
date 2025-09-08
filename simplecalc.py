def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    if y==0:
        return "division by zero is undefined"
    return x/y
op={'+':add,'-':subtract,'*':multiply,'/':divide}
a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))
o=input("Enter the operator:")
print(a,o,b,'=',op[o](a,b))
