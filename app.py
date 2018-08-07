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

count = len(entries)

def delete_entry():
    print "Enter the element to be deleted"
    to_delete = raw_input()
    entries.remove(to_delete)

while input != '5':

    if input == '1':
        add_entry()
        print (entries)

    elif input == '3':
        delete_entry()
        print (entries)

    elif input == '4':
        print (entries)

    input = prompt_user_input()


