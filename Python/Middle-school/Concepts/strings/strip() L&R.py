'''The strip() string method will return a new string without any whitespace characters at the beginning or end.'''
spam = '    Hello World****************'
print(spam.strip())

print(spam.lstrip())

print(spam.rstrip())

spam = 'SpamSpamBaconSpamEggsSpamSpam'
print(spam.strip('ampS'))
'''Passing strip() the argument 'ampS' will tell it to strip occurences of a, m, p, and capital S from the ends of the string stored in spam.
The order of the characters in the string passed to strip() does not matter: strip('ampS') will do the same thing as strip('mapS') or strip('Spam').'''
