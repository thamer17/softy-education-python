def is_palindrome(word):
    n = len(word)
    check_palyndrome = True
    for i in range(n // 2):
        if word[i] != word[n-i-1]:
            check_palyndrome = False
    if check_palyndrome == True:
        print(word, " is palyndrome")
    else:
        print(word, "isn't palyndrome")
is_palindrome("alaa")