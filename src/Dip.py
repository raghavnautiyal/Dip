# Source for the Dip programming language

from dreamscript import *
from parser import *

print("\nDip Version R \n")
print('\nType "help", "copyright", "credits" or "about" for more information.\n')

while True:
    raw_text = input("Dip>  ")
    if raw_text.strip() == "": continue

    if raw_text == "copyright":
        print("Copyright (c) Raghav Nautiyal. All Rights Reserved.")
        continue

    if raw_text == "help":
        print("Visit https://dip-lang.org/docs for help!")
        continue

    if raw_text == "credits":
        print("Thanks to Reddit, Youtube and other online sources for supporting Dip's development.  See www.dip-lang.org for more information.")
        continue

    if raw_text == "about":
        print(""" 
    Dip was created in 2020 by Raghav Nautiyal while he was a student in High School in India, 
    as a language similar to Python but aimed at beginners. (Hence the recursive name - Dip Isn't Python).  
    Raghav remains Dip's principal author, although it includes many contributions from others.
        """)
        continue

    if raw_text == "exit":
        print("Use exit() or Ctrl-C to exit")
        continue

    if raw_text == "exit()":
        exit()
        

        
    result, error = run('<stdin>', raw_text)
    
    bear ="""

            .-`-,\__
              ."`   `,
            .'_.  ._  `;.
        __ / `      `  `.\ .--.
       /--,| 0)   0)     )`_.-,)
      |    ;.-----.__ _-');   /
       '--./         `.`/  `"`
          :   '`      |.
          | \     /  //
           \ '---'  /'
            `------' \\
             _/       `--...

    """

    if error: 
        print(error.as_string())
        print(bear)
       
    elif result: 
        if len(result.elements) == 1:
            print(repr(result.elements[0]))
        else:
            for i in result.elements:
                print(repr(i))