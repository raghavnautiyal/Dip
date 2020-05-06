import dreamscript

while True:
    print("\nDreamscript Version 0.1\n")
    print("Type in 'exit' to exit the prompt\n")
    raw_text = input("DreamScript>  ")
    result, error = dreamscript.run('<stdin>', raw_text)
    
    command = 'exit'

    if command == raw_text.lower():
        exit(0)

    if error: print(error.as_string())
    else: print(result)

    