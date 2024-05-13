
def case1():
    return 5+5

def case2():
    return 5-2

def case3():
    return 5*3

def default_case():
    return"Salir" 

def  switch_case(argument):
    switcher = {
        1:case1,
        2:case2,
        3:case3
    }
    func = switcher.get(argument,default_case)
    return func()

uno = input()
dos = int(uno)
print(switch_case(dos))