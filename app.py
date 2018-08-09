def prompt_user_input():
    print "1. Add entry"
    print "2. Check entry"
    print "3. Delete entry"
    print "4. List entries"
    print "5. Exit"
    print "Enter your input"

    return raw_input()

input = prompt_user_input()

entries = []

def add_entry():
    print "Enter the item"
    entry = raw_input()
    entries.append(entry)

def delete_entry():
    print "Enter the element to be deleted"
    to_delete = int(raw_input()) -1
    del entries[to_delete]

def check_entries():
    y = 0
    for x in entries:
        print "Whether %s is done?" %(x)
        flag = raw_input()
        if flag == 'yes':
            new = "%s : done" %(x)
            entries[y] = new
            y +=1
        else:
            new = "%s : not done" %(x)
            entries[y] = new
            y += 1

def to_print():
    for i in range(len(entries)):
        print "%d" %(i+1),entries[i]

while input != '5':

    if input == '1':
        add_entry()
        to_print()

    elif input == '2':
        check_entries()
        to_print()

    elif input == '3':
        delete_entry()
        to_print()

    elif input == '4':
        to_print()

    input = prompt_user_input()


