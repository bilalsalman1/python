def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation += "W"
            else:
                translation += "w"
        else:
            translation += letter
    return translation

print(translate(input("Enter a phrase: ")))