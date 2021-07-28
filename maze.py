from os import system
def createmark(mark):
    f=open("test.txt","r")
    temp=[]
    for i in f:
        j=0
        while(True):
            if(i[j]=="\n"):
                mark.append(temp)
                temp=[]
                break
            temp.append(0)
            j+=1
    f.close()

def createbazi(bazi):
    f=open("test.txt","r")
    temp=[]
    for i in f:
         j=0
         while(True):
            if(i[j]=="\n"):
                bazi.append(temp)
                temp=[]
                break
            temp.append(int(i[j]))
            j+=1
    f.close()
def printt():
    k=0
    for i in range(len(bazi)):
        for j in range(len(bazi[0])):
            if(mark[i][j]==1):
                print("*",end=' ')
                k+=1
                if(k%len(bazi[0])==0):
                    print("\r")
            else:
                print(bazi[i][j],end=' ')
                k+=1
                if(k%len(bazi[0])==0):
                    print("\r")


mark=[]
createmark(mark)
bazi=[]
createbazi(bazi)
system("clear")
printt()
input()
system("clear")

class Mosh:
    row=0
    col=0
    dire=0
    def __init__(self,row,col,dire):
        self.row=row
        self.col=col
        self.dire=dire
        
class direction:
    vert=0
    horiz=0

move=[]
for i in range(8):
    move.append(direction())
move[0].vert=-1
move[0].horiz=0
move[1].vert=-1
move[1].horiz=1
move[2].vert=0
move[2].horiz=1
move[3].vert=1
move[3].horiz=1
move[4].vert=1
move[4].horiz=0
move[5].vert=1
move[5].horiz=-1
move[6].vert=0
move[6].horiz=-1
move[7].vert=-1
move[7].horiz=-1
class Bazikon:
    mosh=Mosh(1,1,0)
    stack=[]
    def push(self):
        self.stack.append(self.mosh)
        mark[self.mosh.row][self.mosh.col] = 1
        printt()
        input()
        system("clear")
    def pop(self):
        if(self.stack == []):
            return None
        else:
            obj = self.stack[-1]
            del self.stack[-1]
            return obj
    def search(self,bazi,move):
        if(bazi[self.mosh.row+move[self.mosh.dire].vert][self.mosh.col+move[self.mosh.dire].horiz]==0 and  mark[self.mosh.row+move[self.mosh.dire].vert][self.mosh.col+move[self.mosh.dire].horiz] ==0):
            return True
        else:
            return False
    def harekat(self,bazi,move):
        if(self.search(bazi,move)==True):
            mosh = self.mosh
            self.mosh = Mosh(0, 0, 0)
            self.mosh.row = mosh.row + move[mosh.dire].vert
            self.mosh.col = mosh.col + move[mosh.dire].horiz
            self.mosh.dire= 0
            self.push()
        else:
            self.mosh.dire+=1
            if(self.mosh.dire > 7):
                if self.stack != []:
                    mark[self.mosh.row][self.mosh.col]=2
                    self.pop()
                    while self.stack != []:
                        printt()
                        input()
                        system("clear")
                        temp = self.pop()
                        if(temp.dire < 7):
                            break
                        mark[temp.row][temp.col]=2
                    if self.stack == []:
                        printt()
                        print("bazi javab nadarad!")
                        exit()
                    self.stack.append(temp)
                    self.mosh=temp
                    self.mosh.dire+=1        

class Bazi:
    bazikon=Bazikon()
    bazikon.push()
    def play(self):
        while(True):
            self.bazikon.harekat(bazi,move)
            if(self.bazikon.mosh.row==(len(bazi)-2) and self.bazikon.mosh.col==(len(bazi[1])-2)):
                mark[len(bazi)-2][len(bazi[1])-2] = 1
                printt()
                break
b=Bazi()
b.play()