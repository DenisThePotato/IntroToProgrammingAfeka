def isPalindrome(string):
    if string == string[::-1]:
        return True
    else:
        return False
string = "is"
while not isPalindrome(string):
    string = input("input a string of your choice: ")
print(string)
