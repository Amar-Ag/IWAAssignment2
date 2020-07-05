def changeCase(rawString, *args, **kwargs):
    """
    10. Write a function that takes camel-cased strings (i.e.
    ThisIsCamelCased), and converts them to snake case (i.e.
    this_is_camel_cased). Modify the function by adding an argument,
    separator, so it will also convert to the kebab case
    (i.e.this-is-camel-case) as well.
    """
    snakeCaseString = ""
    for letter in rawString:
        if letter.isupper():
            if not snakeCaseString:
                snakeCaseString = snakeCaseString + letter.lower()
            else:
                snakeCaseString = snakeCaseString + "_" + letter.lower()
        else:
            snakeCaseString = snakeCaseString + letter

    # Check if args exists and if it exists convert to the case as requested.
    if args:
        argumentNewString = ""
        for letter in rawString:
            if letter.isupper():
                if not argumentNewString:
                    argumentNewString = argumentNewString + letter.lower()
                else:
                    argumentNewString = argumentNewString + str(args[0]) + letter.lower()
            else:
                argumentNewString = argumentNewString + letter
        return snakeCaseString, argumentNewString

    return snakeCaseString


inputString = str(input("Enter a camel cased string:")) or "ThisIsCamelCased"
userChoice = input("Choose if you want a separator (Y/N):")
if userChoice.upper() == "Y":
    separator = input("Enter the separator that you want:")
    print(changeCase(inputString, separator))
else:
    print(changeCase(inputString))
