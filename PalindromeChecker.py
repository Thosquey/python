while True:
    initialString = raw_input("Entrez un mot : ")
    reversedString = initialString.lower()
    def isPalindrome(reversedString):
        if reversedString[::-1] == reversedString:
            return initialString + " est un mot palindrome"
        else:
            return initialString +  " n'est pas un mot palindrome (l'inverser donne : " + initialString[::-1] + " ce qui n'est pas pareil que " + initialString + ")"
    print isPalindrome(reversedString) + "\n"
