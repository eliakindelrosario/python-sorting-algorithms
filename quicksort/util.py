'''
With help of get_list_of_numbers(input), gets list of numbers numbers from users and verifies input is valid.
'''
def getInput():
     return(get_list_of_numbers(input("Enter a space separated list of numbers\nto be sorted.")))

def get_list_of_numbers(_input):
    numbers = _input.split()
    for i in numbers:
        if not i.isnumeric():
            print("Invalid input. Enter space separated numbers")
            return getInput()
    numbers = list((int(i) for i in numbers))
    return numbers

