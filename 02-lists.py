#!/usr/bin/python3

def main():
    """ Main entry point of the app """
    print('LISTS:')
    print('A list is a collection of items in a particular order')
    list1 = ['mango',20,'peaches']
    print(f'list1: {list1}')
    print(f'list1[0]:{list1[0]}')
    print(f'list1[1]:{list1[1]}')
    print(f'list1[2]:{list1[2]}')
    print(type(list1))
    print('\n')

    #Modifying Elements in a List
    print('Updating values in a list:')
    print(f'Before: {list1}')
    list1[1] = 27
    print(f'After: {list1}')
    print('\n')
    #Adding Elements to a List
    print('Appending items in a list using append():')
    bikes = ['Yamaha','Royal Enfield','TVS']
    print(f'Before: {bikes}')

    #The simplest way to add a new element to a list is to 'append' the item to the list.
    # append() adds the item to the end of the list.
    bikes.append('Hero')
    print(f'After: {bikes}')
    print('\n')

    #You can add a new element at any position in your list by using the insert() method.
    print('Adding items in a list using insert():')
    fruits = ['banana','apple','lemon']
    print(f'Before: {fruits}')

    fruits.insert(1,'kiwi')
    print(f'After: {fruits}')
    print('\n')

    print('Removing Elements from a List:')
    animals = ['cat','dog','leopard','parrot']
    print(f'Before: {animals}')
    del animals[3]
    print(f'After: {animals}')
    print('\n')

    print('Removing an Item Using the pop() Method:')
    """ Sometimes you’ll want to use the value of an item after you remove it from a list. For example, you might want to get the x and y position of an alien that was just shot down, so you can draw an explosion at that position."""
    
    countries = ['India','Japan','America','China']
    print(f'Before: {countries}')

    popped_countries = countries.pop()
    print(f'After: {countries}')
    print(f'{popped_countries}')


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()

""" Changing, Adding, and Removing Elements
Most lists you create will be dynamic, meaning you’ll build a list and then add and remove elements from it as your program runs its course. For example, you might create a game in which a player has to shoot aliens out of the sky. You could store the initial set of aliens in a list and then remove an alien from the list each time one is shot down. Each time a new alien appears on the screen, you add it to the list. Your list of aliens will decrease and increase in length throughout the course of the game. """
