f1 = open("trainorig.txt","r")
f2 = open("train.txt","w")
a = f1.readline()
for i in range(146916):
    a = f1.readline()
    b = a.split(',')
    c1 = b[0].strip()
    c2 = b[1].strip()
    c3 = b[2].strip()
    f2.write(c1+'\t'+c3+'\t'+c2+'\n')