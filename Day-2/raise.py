try:
    raise ArithmeticError("Error")
except ArithmeticError as e:
    print(e)