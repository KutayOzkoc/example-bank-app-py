def sum(first,second):
    return first+second

def sub(first, second):
    if(first < second):
        print("First value bigger than second")
        return 0
    return second - first

def div(first, second):
    if(first == 0):
        print("First value is 0, that is impossible in math")
        return 0
    return first / second

def mpy(first, second):
    return first*second

def print_calc_menu():
    print("1 - Sum... \n" 
      +"2 - Subs... \n" 
      +"3 - Div... \n"
      +"4 - Mpy... \n" 
      +"5 - Exit")