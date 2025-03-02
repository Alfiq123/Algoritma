print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island. 👋")
print("Your mission is to find the treasure. 👑\n")

print("Decide which direction you want to go, left or right: ")
choice_a = input("Your Answer: ").lower()

if choice_a == "left":
    print("\nYou go to the left and you come to a lake, what will you do?, Swim or Wait: ")
    choice_b = input("Your Answer: ").lower()

    if choice_b == "wait":
        print("\nYou decide to wait, and a while later a ship passes by...")
        print("You join the ship, and soon you reach the location of the treasure...")
        print("Soon you find an ancient building, and three entrances, which door will you choose? ")
        print("Blue Door, Red Door, or Yellow Door? ")
        choice_c = input("Your Answer: ")

        if choice_c == "red":
            print(r"""
                           (  .      )
           )           (              )
                 .  '   .   '  .  '  .
        (    , )       (.   )  (   ',    )
         .' ) ( . )    ,  ( ,     )   ( .
      ). , ( .   (  ) ( , ')  .' (  ,    )
     (_,) . ), ) _) _,')  (, ) '. )  ,. (' )
 jgs^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    🔥 YOU BURNED TO THE DEATH - GAME OVER 🔥
            """)

        elif choice_c == "blue":
            print(r"""
                   (    )
                  ((((()))
                  |o\ /o)|
                  ( (  _')
                   (._.  /\__
                  ,\___,/ '  ')
    '.,_,,       (  .- .   .    )
     \   \\     ( '        )(    )
      \   \\    \.  _.__ ____( .  |
       \  /\\   .(   .'  /\  '.  )
        \(  \\.-' ( /    \/    \)
         '  ()) _'.-|/\/\/\/\/\|
             '\\ .( |\/\/\/\/\/|
               '((  \    /\    /
               ((((  '.__\/__.')
                ((,) /   ((()   )
                 "..-,  (()("   /
            pils  _//.   ((() ."
          _____ //,/" ___ ((( ', ___
                           ((  )
                            / /
                          _/,/'
                        /,/,"
  🚩 YOU ARE EATEN BY MONSTERS - GAME OVER 🚩
            """)

        elif choice_c == "yellow":
            print(r"""
                            _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'\U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-\U/.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
            jgs '-._'-.|| |' `_.-'
                    '-.||_/.-'
 👑 CONGRATULATIONS, YOU FOUND THE TREASURE - YOU WIN 👑
            """)

        else:
            print(r"""
                               ________________
                          ____/ (  (    )   )  \___
                         /( (  (  )   _    ))  )   )\
                       ((     (   )(    )  )   (   )  )
                     ((/  ( _(   )   (   _) ) (  () )  )
                    ( (  ( (_)   ((    (   )  .((_ ) .  )_
                   ( (  )    (      (  )    )   ) . ) (   )
                  (  (   (  (   ) (  _  ( _) ).  ) . ) ) ( )
                  ( (  (   ) (  )   (  ))     ) _)(   )  )  )
                 ( (  ( \ ) (    (_  ( ) ( )  )   ) )  )) ( )
                  (  (   (  (   (_ ( ) ( _    )  ) (  )  )   )
                 ( (  ( (  (  )     (_  )  ) )  _)   ) _( ( )
                  ((  (   )(    (     _    )   _) _(_ (  (_ )
                   (_((__(_(__(( ( ( |  ) ) ) )_))__))_)___)
                   ((__)        \\||lll|l||///          \_))
                            (   /(/ (  )  ) )\   )
                          (    ( ( ( | | ) ) )\   )
                           (   /(| / ( )) ) ) )) )
                         (     ( ((((_(|)_)))))     )
                          (      ||\(|(|)|/||     )
                        (        |(||(||)||||        )
                          (     //|/l|||)|\\ \     )
                        (/ / //  /|//||||\\  \ \  \ _)
-------------------------------------------------------------------------------
                      WHAT ARE YOU DOING ? - GAME OVER
            """)

    else:
        print(r"""
                          _.---._     .---.
            __...---' .---. `---'-.   `.
  ~ -~ -.-''__.--' _.'( | )`.  `.  `._ :
 -.~~ .'__-'_ .--'' ._`---'_.-.  `.   `-`.
  ~ ~_~-~-~_ ~ -._ -._``---. -.    `-._   `.
    ~- ~ ~ -_ -~ ~ -.._ _ _ _ ..-_ `.  `-._``--.._
     ~~-~ ~-_ _~ ~-~ ~ -~ _~~_-~ -._  `-.  -. `-._``--.._.--''. ~ -~_
         ~~ -~_-~ _~- _~~ _~-_~ ~-_~~ ~-.___    -._  `-.__   `. `. ~ -_~
       jgs   ~~ _~- ~~- -_~  ~- ~ - _~~- _~~ ~---...__ _    ._ .` `. ~-_~
                ~ ~- _~~- _-_~ ~-_ ~-~ ~_-~ _~- ~_~-_~  ~--.....--~ -~_ ~
                     ~ ~ - ~  ~ ~~ - ~~-  ~~- ~-  ~ -~ ~ ~ -~~-  ~- ~-~
                      🚨 YOU WERE EATEN BY A CROCODILE - GAME OVER 🚨
        """)

else:
    print(r"""
                             8a .
                               `.  _
    ___________  s,    _____     /_/   ____________________a:f____
               .Jktbc._       _ ./
              xft#kTJ:   _.  (_)/)  -._
             cf8#6C. ,  (   ( ,-'      )
           ` `"P:'.     '-._\_\___.---'
        ⚠️ YOU FELL INTO A HOLE - GAME OVER ⚠️
    """)
