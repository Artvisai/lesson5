def password(word):
    """Функция, принимающая строку-пароль. Функция проверяет подходит ли этот пароль условиям
    и возвращает True - если подходит; False - если не подходит.
    Условия:
    ◦ Должен быть не менее 6 символов;
    ◦ Должен содержать хотя бы одну цифру;
    ◦ Не должен состоять только из цифр;
    ◦ Не должен содержать слово “password” в любом регистре."""
    return not word.isdigit() and not word.isalpha() and word.isalnum() and \
           "password" not in word.lower() and len(word) > 5


wrd = input()
print(password(wrd))
