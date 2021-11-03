import random
spisok = ['Den','Stan','Bob','Jim','Bill','Din','Lola','Cola','Igor','Boris','Oleg','Peter',\
          'Petro','Elen','Helen','Omar','Uma','Tuma','Nina','Gila']
def F(spisok,N):
    output=[]
    for i in range(N):
        output.append(spisok[random.randint(0,len(spisok)-1)])
    return output
test = F(spisok,100)
print(test)

def most_frequent(listik):

    slovar={}
    for i in listik:
        if i not in slovar:
            slovar[i] = 1
        else:
            slovar[i] += 1
    # print(slovar,len(slovar))
    return sorted(slovar, key=slovar.get, reverse=True)[0]

    #
    # import pandas as pd
    # test2 = pd.DataFrame(listik)
    # return test2.value_counts().index[0]
print(most_frequent(test))

def less_freq_letter(listishe):
    slovar = {}
    for i in listishe:
        if i[0] not in slovar:
            slovar[i[0]] = 1
        else:
            slovar[i[0]] += 1
    # print(slovar)
    return sorted(slovar, key=slovar.get)[0]

print(less_freq_letter(test))