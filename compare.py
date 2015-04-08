Iju800=open('Iju800.txt').readlines()
Janice800=open('Janice800.txt').readlines()
for i in range(len(Iju800)):
    if Janice800[i]!=Iju800[i]:print Janice800[i].strip(),Iju800[i].strip()
    else:print
