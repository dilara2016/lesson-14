#define calculations to cube
def cube(number):
    return number*number*number

#define a function witch wil execute cube function if user enterd number
#is divisble by 3
def by_3(number):
    if number %3 == 0:
        return cube (number)
    else:
        return False
    #display result
print(by_3(9))
print(by_3(4))
