try:
    num1=100
    num2=0
    q=num1/num2
    print(q)
    li=[1,2,3,4]
    print(li[20])
except ZeroDivisionError:
    print("zero error")
except IndexError:
    print("index exceeded")