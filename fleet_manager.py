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

def remove_member(names, ranks, divs, ids):
    print("Remove member")
    target_id = input("Enter ID to remove: ")
    
    if target_id in ids:
        index = ids.index(target_id)
        
        names.pop(index)
        ranks.pop(index)
        divs.pop(index)
        ids.pop(index)
        print("Crew member removed")
    else:
        print("ID not found")

def display_members(names, ranks, divs, ids):
    print("Display members")
    print("ID", "Name", "Rank", "Division")
    
    for x in range(len(names)):
        print(ids[x], names[x], ranks[x], divs[x])

def update_rank(names, ranks, ids):
    print("Update ranks")
    target_id = input("Enter ID to update: ")
    
    if target_id in ids:
        index = ids.index(target_id)
        
        print("Current rank for", names[index], "is", ranks[index])
        
        new_rank = input("Enter new rank: ")
        
        ranks[index] = new_rank
        print("Rank updated")
    else:
        print("ID not found")

def search_crew(names, ranks, divs, ids):
    print("Search crew")
    term = input("Enter search term: ")

    found = False
    for x in range(len(names)):
        if term in names[x]:
            print(ids[x], names[x], ranks[x], divs[x])
            found = True

    if found == False:
        print("No matches")

def filter_by_division(names, divs):
    print("Filter by division")
    target_div = input("Enter division: ")
    
    print("Members in", target_div)
    found = False
    
    for x in range(len(names)):
        if divs[x] == target_div:
             print(names[x])
             found = True
             
    if found == False:
        print("No members found in this division")

def calculate_payroll(ranks):
    total = 0
    for rank in ranks:
        if rank == "rank1" or rank == "Rank1":
            total = total + 1000
        elif rank == "rank2" or rank == "Rank2":
            total = total + 800
        elif rank == "rank3" or rank == "Rank3":
            total = total + 600
        elif rank == "rank4" or rank == "Rank4":
            total = total + 400
        elif rank == "rank5" or rank == "Rank5":
            total = total + 200
        else:
            total = total + 100
            
    print("Total payroll cost:", total)

def count_officers(ranks):
    count = 0
    for rank in ranks:
        if rank == "rank1" or rank == "Rank1" or rank == "rank2" or rank == "Rank2":
            count = count + 1
    
    print("High ranking officers:", count)

def main():
    names, ranks, divs, ids = init_database() 

    print("there are" ,len(names), "members of the crew")

    while True:
        menu = display_menu() 

        if menu == ("9"):
            break
        elif menu == "1":
            display_members(names, ranks, divs, ids)
        elif menu == "2":
            add_member(names, ranks, divs, ids)
        elif menu == "3":
            remove_member(names, ranks, divs, ids)
        elif menu == "4":
            update_rank(names, ranks, ids)
        elif menu == "5":
            search_crew(names, ranks, divs, ids)
        elif menu == "6":
            filter_by_division(names, divs)
        elif menu == "7":
            calculate_payroll(ranks)
        elif menu == "8":
            count_officers(ranks)
        else:
            print ("invalid option")
main()