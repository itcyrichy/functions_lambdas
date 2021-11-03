with open('C:\\Users\\Asus-pc\\PycharmProjects\\functions\\log') as f:
    lines = f.readlines()

print(lines,len(lines))
slovar={}

from datetime import datetime
for i in lines:
    slovar[i.replace('\n', '')] = datetime.strptime(i[:19], '%Y-%m-%d %H:%M:%S')

print(sorted(slovar,key=slovar.get)[-1],sorted(slovar,key=slovar.get)[-1][:19])

# print(sorted(slovar.values(),key=slovar.get))