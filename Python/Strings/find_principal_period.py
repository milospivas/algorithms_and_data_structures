""" A beautiful piece of code that finds the principal period in a string.
"""

def principal_period(s):
    'Returns the principal period of the string s'

    if (len(s)==1):
        return s
    else:
        i = (s+s).find(s, 1, -1)
        return None if i == -1 else s[:i]


def main_program():
    stop_flag = False

    while not stop_flag:
        print("")
        s = input("Input the string or \"0\" to exit:\n")
        if s == "0":
            stop_flag = True
            print("Exiting...")
        else:
            period = principal_period(s)
            if period == None:
                print("String \""+s+"\" doesn't have a principal period")
            else:
                print("Principal period of string \""+s+"\" is \""+period+"\"")


main_program()