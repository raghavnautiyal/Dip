import dreamscript

print("\nDreamscript Beta (Version 0.1)\n")
print("Type in 'exit' to exit the prompt\n")

while True:
    raw_text = input("DreamScript>  ")
    result, error = dreamscript.run('<stdin>', raw_text)

    command = 'exit'

    if command == raw_text.lower():
        exit()

    if error: print(error.as_string())
    elif result: print(repr(result))