f = open('test.txt','r')
#print(f)
count = 0

for i in f:
    count = count +1
    i = i.replace('chinnu','aswini')
    i = i.strip()
    print(i)
#print(count)
