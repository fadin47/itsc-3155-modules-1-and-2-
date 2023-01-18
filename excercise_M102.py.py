userInput = input('Enter a word: ')
case = [i for i in userInput if i.islower()]
case.extend([i for i in userInput if i.issupper()])
print(' '.join(caseList))



