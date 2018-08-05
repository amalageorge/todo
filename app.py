def prompt_user_input():
    print "1. Add entry"
    print "2. Check entry"
    print "3. Delete entry"
    print "4. List entries"
    print "5. Exit"
    print "Enter your input"

    return raw_input()

input = prompt_user_input()

while input != '5':
    input = prompt_user_input()
