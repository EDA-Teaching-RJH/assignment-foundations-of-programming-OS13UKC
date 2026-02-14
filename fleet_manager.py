def init_database():
    names = ["a","b","c","d","e"]
    ranks = ["rank1","rank2","rank3","rank4","rank5"]
    divs = ["div1","div2","div3","div4","div5"]
    ids = ["1","2","3","4","5"]
    return names, ranks, divs, ids

def display_menu():
    print("1. Display members")
    print("2. Add member")
    print("3. Remove member")
    print("4. Update ranks")
    print("5. Search crew")
    print("6. Filter by divs")
    print("7. Payroll report")
    print("8. Count officers")
    print("9. End")
    return input("Select option: ")

def main():
    names, ranks, divs, ids = init_database() 

    print("there are {len(names)} members of the crew")

    while True:
        menu = display_menu() 

        if menu == ("9"):
            break
        else:
            print ("invalid option")

def add_member(names, ranks, divs,ids):

    pass

main()