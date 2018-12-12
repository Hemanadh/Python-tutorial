def divide(a,b):
    try:
       result=a/b;
       print("Result :",result)
    except ZeroDivisionError:
        print("Not Allowed")
    except TypeError:
        print("Unsupported Operand Type")
    finally:
        print("finally")

divide(1,2)
divide('a','b')
