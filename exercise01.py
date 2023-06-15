#!/usr/bin/python3

def main():
    """ Main entry point of the app """
    print("#This program will invite a list of users")
    print('\n')

    guest_list = ['Aman','Mark','Darren','Suzi']

    for name in guest_list:
        print(f'Hey {name}, I haven\'t seen you in a while, let\'s catch up over dinner at my place on Saturday at 7pm.')
        print('\n')

    not_coming = 'Suzi'
    new_member = 'Ron'
    guest_list.remove(not_coming)
    guest_list.append(new_member)
    print('[CHANGE IN PLAN]\n')
    print(f'Sorry there is a change in plan. {not_coming} can\'t make to the dinner.So I am inviting {new_member} to the party.\n')
    print('*** New Message ***\n')
    
    for name in guest_list:
        print(f'Hey {name}, I haven\'t seen you in a while, let\'s catch up over dinner at my place on Saturday at 7pm.')
        print('\n')


    print('I\'m excited to announce that I got a bigger table for dinner! This means I can now invite more people to my home for meals. I\'m looking forward to hosting more dinner parties and get-togethers.I am also inviting more members for the party.\n')

    print(f'Old list: {guest_list}')

    guest_list.insert(0, 'Tim')
    guest_list.insert(2, 'Alice')
    guest_list.append('John')

    print(f'New list: {guest_list}\n')
    print('******************* Alert ******************')

    for name in guest_list:
        print(f'Hey {name}, I haven\'t seen you in a while, let\'s catch up over dinner at my place on Sunday at 7pm.\n')

    ####################################################################################
    """ Shrinking A List """

    print(guest_list)
    print('I\'m so sorry, but I can only invite two people to my dinner party.\n')

    while len(guest_list) > 2:
        guest_to_remove = guest_list.pop()
        print(f"I'm so sorry, {guest_to_remove}, but I can't invite you to dinner this time.")

    print('\n')
    print(f"The two guests who will be joining me for dinner are {guest_list[0]} and {guest_list[1]}.")

    
    
if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
