def printable():
    f=open('D:/aaa.txt','w')
    for i in range(5):
        x=input('ean')
        f.writelines(str(i*'*'))
        f.write('\n')
    f.close()
printable()
