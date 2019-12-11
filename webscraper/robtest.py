def initialLetters(wordList):
    dict ={}

    for word in wordList:
        if not word[0] in dict:
            dict[word[0]] = [word]

        elif word not in dict[word[0]]:
                dict[word[0]].append(word)
    return dict

#horton = ['I', 'say', 'what', 'I', 'mean', 'and', 'I', 'mean', 'what', 'I', 'say']

#print(initialLetters(horton))

test1 = ['this', 'list', 'is', 'a', 'test', 'of', 'a', 'function']

print(initialLetters(test1))

#test2 = ['this', 'test', 'is', 'one', 'of', 'many']

#print(initialLetters(test2))

#test3 = ['a', 'apple', 'ant', 'ardvark', 'Acadia', 'adventure']

#print(initialLetters(test3))