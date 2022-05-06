S = input("Please type a word: ")
if len(S) < 50:
    print(str.isalnum(S))
    print(str.isalpha(S))
    print(str.isdigit(S))
    print(str.islower(S))
    print(str.isupper(S))
    
else:
    
    print("Input has to be less than 50 characters long.")
    