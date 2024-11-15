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

for i in (sentence):
    repeatedletter = []

    for k in i:
        j = (sentence.count(k))
        if k not in repeatedletter:
            repeatedletter.append(k)
            dic[k] = j
        
print(dic)