#If you use """" or ''' you can add multiple line comments
# You can escate a caracter from action with \ before, like if you want to use an ' in a string you can add a \ before => \' to still print it
art = """                                       ,.=,,==. ,,_
                      _ ,====, _    |I|`` ||  `|I `|
                     |`I|    || `==,|``   ^^   ``  |
                     | ``    ^^    ||_,===TT`==,,_ |
                     |,==Y``Y==,,__| \L=_-`'   +J/`
                      \|=_  ' -=#J/..-|=_-     =|
                       |=_   -;-='`. .|=_-     =|----T--,
                       |=/\  -|=_-. . |=_-/^\  =||-|-|::|____
                       |=||  -|=_-. . |=_-| |  =|-|-||::\____
                       |=LJ  -|=_-. . |=_-|_| =||-|-|:::::::
                       |=_   -|=_-_.  |=_-     =|-|-||:::::::
                       |=_   -|=//^\. |=_-     =||-|-|:::::::
                   ,   |/&_,_-|=||  | |=_-     =|-|-||:::::::
                ,--``8%,/    ',%||  | |=_-     =||-|-|%::::::
            ,---`_,888`  ,.'''''`-.,|,|/!,--,.&\|&\-,|&#:::::
           |;:;K`__,...;=\_____,=``           %%%&     %#,---
           |;::::::::::::|       `'.________+-------\   ``
          /8M%;:::;;:::::|                  |        `-------
          """
#print('Hey there! You\'re awesome')
print(art)
print("Welcome to Treasure Island.\nYour mission is to find the treasure.\nYou are at a cross road. Where do you want to go?")
action = ""
action = input("Type 'left' or 'right'\n").lower() #this ensures that the user isn't problem if adds Left or Right

if action == "left":
    print("You've come to a lake. There is an island in the middle of the lake.")
    action = input("Type 'wait' to wiat for a boat. Type 'swim' to swim across the lake. \n").lower()
    if action == "wait":
        print("You arrive at the island unharmed. There is a house with 3 doors.")
        action = input("One red, one yellow and one blue. Which colour do you choose?\n").lower()
        if action == "red":
            print("You have been burned by fire. Gameover.")
        elif action == "yellow":
            print("You have found the treasure. Congrats!")
        elif action == "blue":
            print("You have been eaten by a beast. Game over.")
        else:
            print("You have selected incorrect action. Game over")
    else:
        print("You have been attached by trout. Game over.")
else:
    print("You have fallen into a hole. Game over.")  


'''
You can also print multiple lines like this:
print('Hello.' 
      'What\'s up?')
''' 