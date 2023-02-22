String = input("Enter any string to remove all vowel for it")
if string=='x':
    exit();
else:
    newst = string;
    print("\n Remove vowels from the given string...");
    vowels = ('a','e','i','o','u');
    for x in string.lower():
        if x in vowels:
            newst = newstr.repalce(x,"");
        print("New string after successfully removed all the vowels:");
        print(newstr)
