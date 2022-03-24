try:
    age=10
    if age<18:
        raise ValueError("Not eligible for vote")
    else:
        print("Eligible")
except ZeroDivisionError as e:
    print("Exception occured "+str(e))
except ValueError as e:
    print("Excetion"+str(e))
except:
    print("exception occured")
else:
    print("No exception")
finally:
    print("HARMAN Ltd")

