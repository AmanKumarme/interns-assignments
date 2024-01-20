def palindrome(s):
    
    # remove spaces and convert to lowercase for case-insensitive comparison
    cleaned_string = ''.join(s.split()).lower()
    
    # compare the original string with its reverse
    return cleaned_string == cleaned_string[::-1]

# prompt the user to enter a string
user_input = input("Enter a string: ")

# check if the entered string is a palindrome
if palindrome(user_input):
    print(f"The string '{user_input}' is a palindrome.")
else:
    print(f"The string '{user_input}' is not a palindrome.")
