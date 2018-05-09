'''ask the user for a string and work out if its a palindrome'''

print('This is a palindrome checker')
a = input('Please enter a string: ')

if a == a[::-1]:
    print('This is a palindrome')

else:
    print('This is NOT a palindrome')
