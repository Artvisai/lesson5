def password(word):
    return not word.isdigit() and not word.isalpha() and word.isalnum() and \
           "password" not in word.lower() and len(word) > 5


wrd = input()
print(password(wrd))
