#File Handling code

def readFile(fname):
    f=open(fname,'r')
    while True:
        str=f.readline()
        if str:
            print(str)
        else:
            print("end of file")
            break
    f.close()

def writeFile(fname):
    f=open(fname,'w')
    while True:
        str=input('enter text to write in file:(enter 0 to stop)')
        if str!='0':
            f.write(str)
            f.write('\n')
        else:
            break
    f.close()

writeFile('abc.txt')
readFile('abc.txt')