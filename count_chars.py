print("Please type a sentence")
sentence = input()
sentence = sentence.replace(" ", "")

###for i in range (len (sentence)):   
    ###repeatedletter = []

    ###for j in range ( len (sentence[i])):

        ###if sentence[i][j] not in repeatedletter:
            ###repeatedletter.append(sentence[i][j])
            ###print("letter: " + sentence[i][j] + ", count: " + str(sentence[i].count(sentence[i][j])))
dic = {}

repeatedletter = []

for letter in (sentence):
    numberoftimes = (sentence.count(letter))
    if letter not in repeatedletter:
        repeatedletter.append(letter)
        dic[letter] = numberoftimes
        
print(dic)