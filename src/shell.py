from dreamscript import *
from parser import *

print("\nDreamscript Beta (Version 0.1)\n")
print("Type in 'exit' to exit the prompt\n")

while True:
    raw_text = input("Dreamscript>  ")
    if raw_text.strip() == "": continue
    result, error = run('<stdin>', raw_text)

    command = 'exit'

    bear = """\n .------.
(        )    ..
 `------'   .' /
      O    /  ;
        o i  OO
         C    `-.
         |    <-'
         (  ,--.
          \  \_)
           \  :
            `._\.
\n"""

    if command == raw_text.lower():
        exit()
        
    if error: 
        print(error.as_string())
        print(bear)
       
    elif result: 
        if len(result.elements) == 1:
            print(repr(result.elements[0]))
        else:
            print(repr(result))