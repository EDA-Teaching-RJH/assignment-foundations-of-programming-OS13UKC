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

def add_member(names, ranks, divs, ids):
    print("Add new member")
    new_id = input("Enter new ID")
    
    if new_id in ids:
        print (new_id ,"already exists")
        return
        
    print ("Ranks: rank1, rank2, rank3, rank4 and rank5")
    new_rank = input("Enter rank")
    valid_ranks = ["rank1","rank2","rank3","rank4","rank5"]
    if new_rank not in valid_ranks:
        print("Invalid rank try again")
        return

    new_name = input("Enter name")
    new_div = input("Enter division")
    

    ids.append(new_id)
    ranks.append(new_rank)
    names.append(new_name)
    divs.append(new_div)
    print ("Crew member", new_name ,"added")

def main():
    names, ranks, divs, ids = init_database() 

    print("there are" ,len(names), "members of the crew")

    while True:
        menu = display_menu() 

        if menu == ("9"):
            break
        elif menu == "2":
            add_member(names, ranks, divs, ids)
        else:
            print ("invalid option")
main()