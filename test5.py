a = int(input('enter number '))
b = int(input('enter another number here '))
c = a + b
d = a - b
e = a * b 
f = a / b
print(a,b,c,d,e,f)
col_width = 5
tableLength = len(f"{'a':>{col_width}}|{'b':>{col_width}}|{'c=a+b':>{col_width}}|{'d=a-b':>{col_width}}|{'e=a*b':>{col_width}}|{'f=a/b':>{col_width}}")
print(f"{'a':>{col_width}}|{'b':>{col_width}}|{'c=a+b':>{col_width}}|{'d=a-b':>{col_width}}|{'e=a*b':>{col_width}}|{'f=a/b':>{col_width}}")
print('-'*tableLength)
print(f"{a:<{col_width}}|{b:<{col_width}}|{c:<{col_width}}|{d:<{col_width}}|{e:<{col_width}}|{f:<{col_width}}")