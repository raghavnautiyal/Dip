import dreamscript

while True:
    raw_text = input("DreamScript>  ")
    result, error = dreamscript.run('<stdin>', raw_text)

    if error: print(error.as_string())
    else: print(result)