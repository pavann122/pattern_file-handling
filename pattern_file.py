def printable():
    f=open('D:/aaa.txt','w')
    for i in range(5):
        f.writelines(str(i*'*'))
        f.write('\n')
    f.close()
printable()
