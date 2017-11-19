while True:
    initialString = raw_input("\nEnter a word : ")
    loweredString = initialString.lower()
    def isPalindrome(initialString):
        if loweredString[::-1] == loweredString:
            return initialString + " is a palindrome word"
        else:
            return initialString + " isn't a palindrome word"
    print isPalindrome(initialString)
