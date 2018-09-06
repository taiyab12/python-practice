def fibo(number):
    a, b, c = 0, 1, 0
    while c < number:
        print(a)
        a, b, c = b, a+b, c+1


n= int(input("enter how much term you want in series"))
fibo(n)