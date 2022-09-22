#################################################
# tp3.py
#
# Your name:Xuan Tang
# Your andrew id:xuantang
# Your mentor:Grace
#################################################



from cmu_112_graphics import *
import math,random

class FirstScreen(Mode):
    def appStarted(mode):
        # CITATION: I got the image from 
        # https://plantsvszombies.fandom.com/wiki/Plants_vs._Zombies
        mode.image=mode.loadImage("Plantsvs.ZombiesLoadingScreen.png")
    
    def mousePressed(mode,event):
        if (246<event.x<548 and 543<event.y<575):
            mode.app.setActiveMode(mode.app.ChooseMode)
    
    def redrawAll(mode,canvas):
        canvas.create_image(mode.width/2,mode.height/2,
                            image=ImageTk.PhotoImage(mode.image))

class ChooseMode(Mode):
    def appStarted(mode):
        # CITATION: I got the image from 
        # https://kudarokoi.wordpress.com/2014/12/12/
        # difficultybalance-in-god-hand-and-video-games/
        mode.image=mode.loadImage("difficulty.jpg")
        imageWidth,imageHeight=mode.image.size
        mode.image=mode.scaleImage(mode.image,800/imageWidth)

    def mousePressed(mode,event):
        if (15<event.x<785 and 166<event.y<266):
            mode.app.setActiveMode(mode.app.EasyMode)
        if (15<event.x<785 and 298<event.y<398):
            mode.app.setActiveMode(mode.app.MediumMode)
        if (15<event.x<785 and 430<event.y<530):
            mode.app.setActiveMode(mode.app.HardMode)

    def redrawAll(mode,canvas):
        canvas.create_image(mode.width/2,mode.height/2,
                            image=ImageTk.PhotoImage(mode.image))

class Sun():
    def __init__(self,row,col):
        self.row=row
        self.col=col
        self.time=0

class Pea():
    def __init__(self,x,y):
        self.x=x
        self.y=y

class PeaShooters():
    def __init__(self,row,col):
        self.row=row
        self.col=col
        self.time=1.08
        self.life=60

class SunFlowers():
    def __init__(self,row,col):
        self.row=row
        self.col=col
        self.time=0
        self.life=60

class SnowPea():
    def __init__(self,x,y):
        self.x=x
        self.y=y

class SnowPeaShooters():
    def __init__(self,row,col):
        self.row=row
        self.col=col
        self.time=1.08
        self.life=60

class commonZombies():
    count=10
    def __init__(self,x,y,row):
        self.x=x
        self.y=y
        self.row=row
        self.life=110
        self.isMove=True
        commonZombies.count-=1

class commonZombies2():
    count=20
    def __init__(self,x,y,row):
        self.x=x
        self.y=y
        self.row=row
        self.life=110
        self.isMove=True
        self.isFrozen=False
        self.frozenTime=0
        commonZombies2.count-=1

class commonZombies1():
    count=30
    def __init__(self,x,y,row):
        self.x=x
        self.y=y
        self.row=row
        self.life=110
        self.isMove=True
        self.isChange=False
        self.isEat=False
        self.changeTimes=0
        commonZombies1.count-=1

class EasyMode(Mode):
    def sunSpriteSheets(mode):
        # CITATION: I got an animated sunflower gif from 
        # https://plantsvszombies.fandom.com/wiki/Sunflower/Gallery
        # and I use Ulead Gif Animator to extract certain snapshots of the gif,
        # and use TexturePackerGUI to make the spritesheet.
        path='sunflower.png'
        mode.sunSheet=mode.loadImage(path)
        mode.sunSheet=mode.scaleImage(mode.sunSheet,1/2)
        sheetWidth,sheetHeight=mode.sunSheet.size
        stripWidth=sheetWidth/4.8
        stripHeight=sheetHeight/1.9
        mode.sunSheets=[]
        for i in range(2):
            for j in range(5):
                image=mode.sunSheet.crop((stripWidth*j,stripHeight*i,
                                            stripWidth*(j+1),stripHeight*(i+1)))
                mode.sunSheets.append(image)
        mode.sunSheetCounter=0

    def peaSpriteSheets(mode):
        # CITATION: I got an animated peashooter gif from 
        # https://plantsvszombies.fandom.com/wiki/Peashooter/Gallery
        # and I use Ulead Gif Animator to extract certain snapshots of the gif,
        # and use TexturePackerGUI to make the spritesheet.
        path='peashooter.png'
        mode.peaSheet=mode.loadImage(path)
        sheetWidth,sheetHeight=mode.peaSheet.size
        stripWidth=sheetWidth/8
        mode.peaSheets=[None]*8
        mode.peaSheets[0]=mode.peaSheet.crop((45,0,175,sheetHeight))
        mode.peaSheets[1]=mode.peaSheet.crop((190,0,320,sheetHeight))
        mode.peaSheets[2]=mode.peaSheet.crop((330,0,460,sheetHeight))
        mode.peaSheets[3]=mode.peaSheet.crop((475,0,605,sheetHeight))
        mode.peaSheets[4]=mode.peaSheet.crop((606,0,736,sheetHeight))
        mode.peaSheets[5]=mode.peaSheet.crop((743,0,873,sheetHeight))
        mode.peaSheets[6]=mode.peaSheet.crop((885,0,1015,sheetHeight))
        mode.peaSheets[7]=mode.peaSheet.crop((1025,0,1155,sheetHeight))
        for i in range (8):
            mode.peaSheets[i]=mode.scaleImage(mode.peaSheets[i],1/2)
        mode.peaSheetCounter=0
    
    def initializePea(mode):
        # CITATION: I got the image from 
        # https://www.macworld.com/article/1140405/plantsvszombies.html
        # and extract the pea from it
        path='pea.png'
        mode.peaImage=mode.loadImage(path)

    def commonZombieSpriteSheets(mode):
        # CITATION: I got an animated sunflower gif from 
        # https://plantsvszombies.fandom.com/wiki/Browncoat_Zombie/Gallery#Basic_Zombie
        # and I use Ulead Gif Animator to extract certain snapshots of the gif,
        # and use TexturePackerGUI to make the spritesheet.
        path='commonZombies.png'
        mode.commonZombieSheet=mode.loadImage(path)
        mode.commonZombieSheet=mode.scaleImage(mode.commonZombieSheet,4/5)
        sheetWidth,sheetHeight=mode.commonZombieSheet.size
        stripWidth=sheetWidth/7
        stripHeight=sheetHeight/2
        mode.commonZombiesSheets=[]
        for i in range(2):
            for j in range(7):
                image=mode.commonZombieSheet.crop((4+stripWidth*j,stripHeight*i,
                                                   stripWidth*(j+1),stripHeight*(i+1)))
                mode.commonZombiesSheets.append(image)
        mode.commonZombieSheetCounter=0

    def eatingZombieSpriteSheets(mode):
        # CITATION: I got an animated sunflower gif from 
        # https://plantsvszombies.fandom.com/wiki/Zombie_(PvZ)
        # and I use Ulead Gif Animator to extract certain snapshots of the gif,
        # and use TexturePackerGUI to make the spritesheet.
        path='EatingZombies.png'
        mode.eatingZombieSheet=mode.loadImage(path)
        sheetWidth,sheetHeight=mode.eatingZombieSheet.size
        stripWidth=sheetWidth/8
        mode.eatingZombiesSheets=[None]*8
        mode.eatingZombiesSheets[0]=mode.eatingZombieSheet.crop((0,0,64,sheetHeight))
        mode.eatingZombiesSheets[1]=mode.eatingZombieSheet.crop((65,0,120,sheetHeight))
        mode.eatingZombiesSheets[2]=mode.eatingZombieSheet.crop((120,0,176,sheetHeight))
        mode.eatingZombiesSheets[3]=mode.eatingZombieSheet.crop((176,0,228,sheetHeight))
        mode.eatingZombiesSheets[4]=mode.eatingZombieSheet.crop((228,0,278,sheetHeight))
        mode.eatingZombiesSheets[5]=mode.eatingZombieSheet.crop((278,0,325,sheetHeight))
        mode.eatingZombiesSheets[6]=mode.eatingZombieSheet.crop((325,0,370,sheetHeight))
        mode.eatingZombiesSheets[7]=mode.eatingZombieSheet.crop((372,0,425,sheetHeight))
        mode.eatingZombieSheetCounter=0

    def appStarted(mode):
        # CITATION: I got the image from 
        # https://www.desktopbackground.org/wallpaper/
        # plants-vs-zombies-wiki-battles-day-vs-night-plants-vs-zombies-896091
        mode.background=mode.loadImage("lawn.jpg")
        # CITATION: I got the full image from 
        # https://plantsvszombies.fandom.com/wiki/Plants_vs._Zombies
        # and crop the menu button from it
        mode.menuButton=mode.loadImage('menu.png')
        # CITATION: I got the full image from 
        # https://gaming.stackexchange.com/questions/17001/
        # how-can-i-run-plant-vs-zombies-in-a-resizable-window-mode
        # and crop the partial image from it
        mode.pauseScreen=mode.loadImage('pauseScreen.png')
        # CITATION: I got the full image from 
        # https://plantsvszombies.fandom.com/wiki/Level_1-2/Gallery
        # and crop the plant board from it
        mode.plantBoard=mode.loadImage('plantBoard.png')
        mode.sunImage=mode.loadImage('sun.png')
        mode.isPause=False
        mode.loadPause=False
        mode.cellWidth=740/9
        mode.cellHeight=101
        mode.xMargin=30
        mode.yMargin=75
        mode.sunSpriteSheets()
        mode.peaSpriteSheets()
        mode.commonZombieSpriteSheets()
        mode.eatingZombieSpriteSheets()
        mode.initializePea()

        mode.dropSuns=[]
        mode.producedSuns=[]

        mode.sunFlowers=[]
        mode.plantSun=False
        mode.sunCD=0
        mode.sunCD1=7
        mode.peaShooters=[]
        mode.plantPea=False
        mode.peaCD=0
        mode.peaCD1=8
        mode.peas=[]

        mode.commonZombies=[]

        mode.plantList=[([None]*9) for i in range(5)]
        mode.hasDropSun=[([False]*9) for i in range(5)]
        mode.hasProducedSun=[([False]*9) for i in range(5)]
        mode.sunCounter=50
        mode.dropSunTime=0
        mode.zombieTime=0
        mode.produceZombiesRate=18

        # CITATION: I got the image from 
        # https://www.uhi.ac.uk/en/educational-development-unit/
        # remote-teaching/hints-and-tips-for-remote-teaching/
        mode.bulb=mode.loadImage("hint.png")
        mode.bulb=mode.scaleImage(mode.bulb,1/2)
        # CITATION: I got the image from 
        # https://pixabay.com/vectors/mark-check-tick-red-correct-38217/
        mode.correct=mode.loadImage('correct.png')
        mode.correct=mode.scaleImage(mode.correct,1/15)
        mode.showHint=False
        mode.isHint=[([None]*9) for i in range(5)]

        # CITATION: I got the full image from 
        # https://plantsvszombies.fandom.com/wiki/Plants_vs._Zombies
        # and crop the menu button from it
        # https://www.youtube.com/watch?v=VZhaETT4zNs
        # and crop the zombie's head from it
        mode.zombieHead=mode.loadImage('zombieHead.png')
        mode.zombieHead=mode.scaleImage(mode.zombieHead,3/4)

        # CITATION: I got the full image from 
        # https://plantsvszombies.fandom.com/wiki/Plants_vs._Zombies?file=0000008156.jpg
        # and crop the shovel from it
        mode.shovel=mode.loadImage('shovel.jpg')
        mode.useShovel=False

    def getCell(mode,cx,cy):
        if (cx<mode.xMargin or cx>mode.xMargin+9*mode.cellWidth 
            or cy<mode.yMargin or cy>mode.yMargin+5*mode.cellHeight):
            return (-1,-1)
        row=int((cy-mode.yMargin)/mode.cellHeight)
        col=int((cx-mode.xMargin)/mode.cellWidth)
        return (row, col)

    def getCellBounds(mode,row,col):
        x0=mode.xMargin+col*mode.cellWidth
        x1=mode.xMargin+(col+1)*mode.cellWidth
        y0=mode.yMargin+row*mode.cellHeight
        y1=mode.yMargin+(row+1)*mode.cellHeight
        return (x0,y0,x1,y1)

    # CITATION: I got the function from 
    # https://www.cs.cmu.edu/~112/notes/notes-variables-and-
    # functions.html#RecommendedFunctions
    def almostEqual(mode,d1,d2,epsilon=10**-7):
        return (abs(d2-d1)<epsilon)

    def dropSun(mode):
        mode.dropSunTime+=0.12
        if (mode.almostEqual(mode.dropSunTime,7.8)):
            mode.dropSunTime=0
            currSun=[]
            for sun in mode.dropSuns:
                (row,col)=(sun.row,sun.col)
                currSun.append((row,col))
            while True:
                ranRow=random.randint(0,4)
                ranCol=random.randint(0,8)
                if (not isinstance(mode.plantList[ranRow][ranCol],SunFlowers)):
                    sunInstance=Sun(ranRow,ranCol)
                    mode.dropSuns.append(sunInstance)
                    mode.hasDropSun[ranRow][ranCol]=True
                    return 
    
    def produceSun(mode):
        for sun in mode.sunFlowers:
            sun.time+=0.12
            if (mode.almostEqual(sun.time,10.8)):
                sun.time=0
                sunInstance=Sun(sun.row,sun.col)
                mode.producedSuns.append(sunInstance)
                mode.hasProducedSun[sun.row][sun.col]=True

    def eliminateSun(mode):
        index=0
        while (index<len(mode.dropSuns)):
            mode.dropSuns[index].time+=0.12
            sunTime=mode.dropSuns[index].time
            if (sunTime>6):
                mode.hasDropSun[mode.dropSuns[index].row][mode.dropSuns[index].col]=False
                mode.dropSuns.pop(index)
            else:
                index+=1
        index=0
        while (index<len(mode.producedSuns)):
            mode.producedSuns[index].time+=0.12
            sunTime=mode.producedSuns[index].time
            if (sunTime>6):
                mode.hasProducedSun[mode.producedSuns[index].row][mode.producedSuns[index].col]=False
                mode.producedSuns.pop(index)
            else:
                index+=1

    def produceZombies(mode):
        mode.zombieTime+=0.12
        if (mode.zombieTime>=mode.produceZombiesRate and commonZombies.count>0):
            mode.zombieTime=0
            ranRow=random.randint(0,4)
            x=801
            y=mode.yMargin+(ranRow+0.5)*mode.cellHeight
            commonZombieInstance=commonZombies(x,y,ranRow)
            mode.commonZombies.append(commonZombieInstance)

    def isAttack(mode,plant):
        (x0,y0,x1,y1)=mode.getCellBounds(plant.row,plant.col)
        cx=(x0+x1)/2
        cy=(y0+y1)/2
        for zombie in mode.commonZombies:
            (x,y)=(zombie.x,zombie.y)
            if (cx<x<=800 and mode.almostEqual(y,cy)):
                return True
        return False

    def attackZombies(mode):
        for i in range(5):
            for j in range (9):
                plant=mode.plantList[i][j]
                if (isinstance(plant,PeaShooters)):
                    if (mode.isAttack(plant)):
                        if (mode.almostEqual(plant.time,1.08)):
                            (x0,y0,x1,y1)=mode.getCellBounds(plant.row,plant.col)
                            cx=(x0+x1)/2
                            cy=(y0+y1)/2
                            peaInstance=Pea(cx,cy)
                            mode.peas.append(peaInstance)
                            plant.time-=0.12
                        else:
                            plant.time-=0.12
                            if (plant.time<=0):
                                plant.time=1.08

    def isHit(mode,pea):
        hitZombie=None
        (cx,cy)=pea.x,pea.y
        for zombie in mode.commonZombies:
            (x,y)=zombie.x,zombie.y
            if (cx>x and mode.almostEqual(cy,y)):
                if (hitZombie==None or zombie.x<hitZombie.x):
                    hitZombie=zombie
        return hitZombie

    def hitZombies(mode):
        index=0
        while (index<len(mode.peas)):
            if (mode.isHit(mode.peas[index])!=None):
                zombie=mode.isHit(mode.peas[index])
                zombie.life-=10
                mode.peas.pop(index)
            else:
                index+=1
    
    def isEat(mode,zombie):
        (row,col)=mode.getCell(zombie.x,zombie.y)
        if (row<0 or row>4 or col<0 or col>8):
            return False
        else:
            if (mode.plantList[row][col]!=None):
                return True
            else:
                return False

    def eatPlants(mode):
        for zombie in mode.commonZombies:
            if (mode.isEat(zombie)):
                (row,col)=mode.getCell(zombie.x,zombie.y)
                zombie.isMove=False
                mode.plantList[row][col].life-=2
            else:
                zombie.isMove=True
    
    def removeSunFlowers(mode):
        index=0
        while (index<len(mode.sunFlowers)):
            sunFlower=mode.sunFlowers[index]
            if (sunFlower.life<=0):
                mode.plantList[sunFlower.row][sunFlower.col]=None
                mode.sunFlowers.pop(index)
            else:
                index+=1

    def removePeaShooters(mode):
        index=0
        while (index<len(mode.peaShooters)):
            peaShooter=mode.peaShooters[index]
            if (peaShooter.life<=0):
                mode.plantList[peaShooter.row][peaShooter.col]=None
                mode.peaShooters.pop(index)
            else:
                index+=1

    def removeCommonZombies(mode):
        index=0
        while (index<len(mode.commonZombies)):
            if (mode.commonZombies[index].life<=0):
                mode.commonZombies.pop(index)
            else:
                index+=1

    def sunFlowertimerFired(mode):
        mode.sunSheetCounter=(1+mode.sunSheetCounter)%len(mode.sunSheets)

    def sunFlowerCD(mode):
        if (mode.sunCD!=0):
            mode.sunCD-=0.12
            if (mode.sunCD<=0):
                mode.sunCD=0

    def peaShootertimerFired(mode):
        mode.peaSheetCounter=(1+mode.peaSheetCounter)%len(mode.peaSheets)

    def peaShooterCD(mode):
        if (mode.peaCD!=0):
            mode.peaCD-=0.12
            if (mode.peaCD<=0):
                mode.peaCD=0

    def peatimerFired(mode):
        for pea in mode.peas:
            pea.x+=50

    def commonZombietimerFired(mode):
        mode.commonZombieSheetCounter=(1+mode.commonZombieSheetCounter)%len(mode.commonZombiesSheets)
        mode.eatingZombieSheetCounter=(1+mode.eatingZombieSheetCounter)%len(mode.eatingZombiesSheets)
        for zombie in mode.commonZombies:
            if (zombie.isMove):
                zombie.x-=2

    def checkLose(mode):
        for zombie in mode.commonZombies:
            if (zombie.x<0):
                mode.appStarted()
                commonZombies.count=10
                mode.app.setActiveMode(mode.app.LoseScreen)
    
    def checkWin(mode):
        if (commonZombies.count==0 and mode.commonZombies==[]):
            mode.appStarted()
            commonZombies.count=10
            mode.app.setActiveMode(mode.app.WinScreen)

    def timerFired(mode):
        if (mode.isPause): 
            return 
        if (mode.sunFlowers!=[]):
            mode.sunFlowertimerFired()
            mode.produceSun()
        if (mode.peaShooters!=[]):
            mode.peaShootertimerFired()
        if (mode.commonZombies!=[]):
            mode.commonZombietimerFired()
        if (mode.peas!=[]):
            mode.peatimerFired()
        if (mode.showHint):
            mode.giveHints()
        mode.checkWin()
        mode.checkLose()
        mode.dropSun()
        mode.eliminateSun()
        mode.sunFlowerCD()
        mode.peaShooterCD()
        mode.produceZombies()
        mode.attackZombies()
        mode.hitZombies()
        mode.eatPlants()
        mode.removeSunFlowers()
        mode.removePeaShooters()
        mode.removeCommonZombies()
    
    def checkSun(mode,row,col):
        for i in range(len(mode.dropSuns)):
            (currRow,currCol)=(mode.dropSuns[i].row,mode.dropSuns[i].col)
            if (row==currRow and col==currCol):
                return i
        return None
    
    def checkSun2(mode,row,col):
        for i in range(len(mode.producedSuns)):
            (currRow,currCol)=(mode.producedSuns[i].row,mode.producedSuns[i].col)
            if (row==currRow and col==currCol):
                return i
        return None

    def keyPressed(mode,event):
        if (mode.isPause):
            return 
        if (event.key=='s'):
            mode.sunCounter=2000
        elif (event.key=='z'):
            mode.produceZombiesRate=3
        elif (event.key=='f'):
            mode.sunCD1=1.2
        elif (event.key=='p'):
            mode.peaCD1=1.2

    def mousePressed(mode,event):
        if (mode.isPause):
            if (235<event.x<570 and 310<event.y<390):
                mode.isPause=False
                mode.loadPause=False
            elif (300<event.x<513 and 245<event.y<282):
                mode.appStarted()
                commonZombies.count=10
                mode.app.setActiveMode(mode.app.FirstScreen)
            elif(300<event.x<513 and 200<event.y<240):
                mode.appStarted()
                commonZombies.count=10
            return

        if (mode.width-145<event.x<mode.width and 0<event.y<35):
            mode.isPause=True
            mode.loadPause=True

        elif (557<event.x<613 and 0<event.y<62):
            mode.showHint=not mode.showHint

        elif (150<event.x<200 and 8<event.y<75):
            if (mode.plantSun):
                mode.plantSun=False
            elif (mode.sunCounter>=50 and mode.sunCD==0):
                mode.plantSun=True
                return 

        elif (88<event.x<138 and 8<event.y<75):
            if (mode.plantPea):
                mode.plantPea=False
            elif (mode.sunCounter>=100 and mode.peaCD==0):
                mode.plantPea=True
                return 
        
        elif (460<event.x<545 and 0<event.y<88):
            mode.useShovel=not mode.useShovel
    
        (row,col)=mode.getCell(event.x,event.y)
        if (row<0 or row>4 or col<0 or col>8):
            return

        if (mode.plantSun and mode.plantList[row][col]==None):
            sunFlowerInstance=SunFlowers(row,col)
            mode.sunFlowers.append(sunFlowerInstance)
            mode.plantList[row][col]=sunFlowerInstance
            mode.sunCounter-=50
            mode.plantSun=False
            mode.sunCD=mode.sunCD1

        elif (mode.plantPea and mode.plantList[row][col]==None):
            peaShooterInstance=PeaShooters(row,col)
            mode.peaShooters.append(peaShooterInstance)
            mode.plantList[row][col]=peaShooterInstance
            mode.sunCounter-=100
            mode.plantPea=False
            mode.peaCD=mode.peaCD1
        
        elif (mode.useShovel and mode.plantList[row][col]!=None):
            plant=mode.plantList[row][col]
            if (isinstance(plant,SunFlowers)):
                mode.sunFlowers.remove(plant)
            elif (isinstance(plant,PeaShooters)):
                mode.peaShooters.remove(plant)
            mode.plantList[row][col]=None
            mode.useShovel=False

        elif (mode.hasDropSun[row][col]):
            mode.sunCounter+=25
            index=mode.checkSun(row,col)
            mode.dropSuns.pop(index)
            mode.hasDropSun[row][col]=False

        elif (mode.hasProducedSun[row][col]):
            mode.sunCounter+=25
            index=mode.checkSun2(row,col)
            mode.producedSuns.pop(index)
            mode.hasProducedSun[row][col]=False
    
    def countZombies(mode,row):
        total=0
        for zombies in mode.commonZombies:
            if (zombies.row==row):
                total+=1
        return total

    def countPeaShooters(mode,row):
        total=0
        for peaShooter in mode.peaShooters:
            if (peaShooter.row==row):
                total+=1
        return total

    def getNearestZombie(mode,i):
        minCol=None
        for zombie in mode.commonZombies:
            if (zombie.row==i):
                (row,col)=mode.getCell(zombie.x,zombie.y)
                if (minCol==None or col<minCol):
                    minCol=col
        return minCol

    def getFurthestPea(mode,i):
        maxCol=None
        for peaShooter in mode.peaShooters:
            if (peaShooter.row==i):
                if (maxCol==None or peaShooter.col>maxCol):
                    maxCol=peaShooter.col
        return maxCol

    def getShortestDistance(mode,i):
        zombieCol=mode.getNearestZombie(i)
        peaCol=mode.getFurthestPea(i)
        return zombieCol-peaCol

    def checkPeaShooters(mode,row,col):
        for j in range(col+1,9):
            if (isinstance(mode.plantList[row][j],PeaShooters)):
                return True
        return False

    def placeSunFlowers(mode,row):
        for j in range(3):
            if (mode.plantList[row][j]==None):
                mode.isHint[row][j]=True

    def placeSunFlowers1(mode,row,peaShootersCount):
        for j in range(3):
            if (mode.plantList[row][j]==None):
                if (mode.checkPeaShooters(row,j)):
                    mode.isHint[row][j]=True
                else:
                    if (peaShootersCount==2):
                        if (isinstance(mode.plantList[row][0],PeaShooters) and 
                            isinstance(mode.plantList[row][1],PeaShooters) and 
                            mode.sunCounter<=200):
                            mode.isHint[row][2]=True
                    elif (peaShootersCount==1 and mode.sunCounter<=200):
                        if (isinstance(mode.plantList[row][0],PeaShooters)):
                            mode.isHint[row][1]=True
                        elif (isinstance(mode.plantList[row][1],PeaShooters)):
                            mode.isHint[row][2]=True

    def giveHints(mode):
        mode.isHint=[([None]*9) for i in range(5)]
        for i in range(5):
            zombiesCount=mode.countZombies(i)
            peaShootersCount=mode.countPeaShooters(i)
            if (zombiesCount>peaShootersCount):
                continue
            elif (zombiesCount==0):
                mode.placeSunFlowers(i)
            else:
                distance=mode.getShortestDistance(i)
                zombiesTime=4*distance
                peaHit=peaShootersCount*zombiesTime
                if (distance<=0 or peaHit<11*zombiesCount):
                    continue
                else:
                    mode.placeSunFlowers1(i,peaShootersCount)

    def drawHints(mode,canvas):
        for i in range(5):
            for j in range(9):
                if (mode.isHint[i][j]):
                    (x0,y0,x1,y1)=mode.getCellBounds(i,j)
                    cx=(x0+x1)/2
                    cy=(y0+y1)/2
                    canvas.create_image(cx,cy,image=ImageTk.PhotoImage(mode.correct))

    def drawSun(mode,canvas):
        for sun in mode.dropSuns:
            (x0,y0,x1,y1)=mode.getCellBounds(sun.row,sun.col)
            cx=(x0+x1)/2
            cy=(y0+y1)/2
            canvas.create_image(cx,cy,image=ImageTk.PhotoImage(mode.sunImage))
        for sun in mode.producedSuns:
            (x0,y0,x1,y1)=mode.getCellBounds(sun.row,sun.col)
            cx=(x0+x1)/2
            cy=(y0+y1)/2
            canvas.create_image(cx,cy,image=ImageTk.PhotoImage(mode.sunImage))

    def drawsunFlower(mode,canvas):
        image=mode.sunSheets[mode.sunSheetCounter]
        for sun in mode.sunFlowers:
            (x0,y0,x1,y1)=mode.getCellBounds(sun.row,sun.col)
            cx=(x0+x1)/2
            cy=(y0+y1)/2
            canvas.create_image(cx,cy,image=ImageTk.PhotoImage(image))
    
    def drawpeaShooters(mode,canvas):
        image=mode.peaSheets[mode.peaSheetCounter]
        for pea in mode.peaShooters:
            (x0,y0,x1,y1)=mode.getCellBounds(pea.row,pea.col)
            cx=(x0+x1)/2
            cy=(y0+y1)/2
            canvas.create_image(cx,cy,image=ImageTk.PhotoImage(image))

    def drawPeas(mode,canvas):
        for pea in mode.peas:
            canvas.create_image(pea.x,pea.y,image=ImageTk.PhotoImage(mode.peaImage))

    def drawPlantBoard(mode,canvas):
        canvas.create_image(0,0,image=ImageTk.PhotoImage(mode.plantBoard),
                            anchor='nw')
        # CITATION: I got the color name from 
        # https://matplotlib.org/3.1.0/gallery/color/named_colors.html
        canvas.create_rectangle(9,60,71,85,fill='palegoldenrod',width=0)
        canvas.create_text(40,72.5,font='Arial 20 bold',text=str(mode.sunCounter))

    def drawCommonZombies(mode,canvas):
        for zombie in mode.commonZombies:
            if (zombie.isMove):
                image=mode.commonZombiesSheets[mode.commonZombieSheetCounter]
            else:
                image=mode.eatingZombiesSheets[mode.eatingZombieSheetCounter]
            canvas.create_image(zombie.x,zombie.y,
                                image=ImageTk.PhotoImage(image))

    def drawProcess(mode,canvas):
        ratio=(10-commonZombies.count)/10
        if (ratio>0):
            # CITATION: I got the color name from 
            # https://matplotlib.org/3.1.0/gallery/color/named_colors.html
            canvas.create_text(520,585,text='Easy Level',font='Arial 14 bold',fill='peru')
            canvas.create_rectangle(585,578,735,592,outline='steelblue',width=5)
            canvas.create_rectangle(587,580,735-(735-585)*ratio,590,fill='black',width=0)
            canvas.create_rectangle(735-(735-585)*ratio,580,733,590,fill='greenyellow',width=0)
            canvas.create_image(735-(735-585)*ratio,(578+592)/2,
                                image=ImageTk.PhotoImage(mode.zombieHead))
        else:
            # CITATION: I got the color name from 
            # https://matplotlib.org/3.1.0/gallery/color/named_colors.html
            canvas.create_text(580,585,text='Easy Level',font='Arial 14 bold',fill='peru')

    def redrawAll(mode,canvas):
        canvas.create_image(mode.width/2,mode.height/2,
                            image=ImageTk.PhotoImage(mode.background))
        canvas.create_image(mode.width,0,
                            image=ImageTk.PhotoImage(mode.menuButton),anchor='ne')
        canvas.create_image(585,30,image=ImageTk.PhotoImage(mode.bulb))
        mode.drawPlantBoard(canvas)
        canvas.create_image(502,44,image=ImageTk.PhotoImage(mode.shovel))
        mode.drawProcess(canvas)
        if (mode.sunFlowers!=[]):
            mode.drawsunFlower(canvas)
        if (mode.peaShooters!=[]):
            mode.drawpeaShooters(canvas)
        if (mode.dropSuns!=[] or mode.producedSuns!=[]):
            mode.drawSun(canvas)
        if (mode.commonZombies!=[]):
            mode.drawCommonZombies(canvas)
        if (mode.peas!=[]):
            mode.drawPeas(canvas)
        if (mode.loadPause):
            canvas.create_image(mode.width/2,mode.height/2,
                                image=ImageTk.PhotoImage(mode.pauseScreen))
        if (mode.plantSun):
            canvas.create_rectangle(150,8,200,75,outline='red')
        if (mode.sunCD!=0):
            canvas.create_text(175,41.5,text=str(math.ceil(mode.sunCD)),
                               font='Arial 20 bold',fill='red')
        if (mode.plantPea):
            canvas.create_rectangle(88,8,138,75,outline='blue')
        if (mode.peaCD!=0):
            canvas.create_text(113,41.5,text=str(math.ceil(mode.peaCD)),
                               font='Arial 20 bold',fill='blue')
        if (mode.useShovel):
            canvas.create_rectangle(460,0,545,88,outline='yellow')
        if (mode.showHint):
            mode.drawHints(canvas)

class MediumMode(EasyMode):
    def snowpeaSpriteSheets(mode):
        # CITATION: I got an animated snow-peashooter gif from 
        # https://plantsvszombies.fandom.com/wiki/Snow_Pea/Gallery
        # and I use Ulead Gif Animator to extract certain snapshots of the gif,
        # and use TexturePackerGUI to make the spritesheet.
        path='snowPeashooters.png'
        mode.snowpeaSheet=mode.loadImage(path)
        mode.snowpeaSheet=mode.scaleImage(mode.snowpeaSheet,1/2.2)
        sheetWidth,sheetHeight=mode.snowpeaSheet.size
        stripWidth=sheetWidth/6
        stripHeight=sheetHeight/2
        mode.snowpeaSheets=[]
        for i in range(2):
            for j in range(6):
                image=mode.snowpeaSheet.crop((3+stripWidth*j,stripHeight*i,
                                                   stripWidth*(j+1),stripHeight*(i+1)))
                mode.snowpeaSheets.append(image)
        mode.snowpeaSheetCounter=0

    def initializesnowPea(mode):
        # CITATION: I got the image from 
        # https://plantsvszombies.fandom.com/wiki/Snow_Pea/Gallery
        path='snowpea.png'
        mode.snowpeaImage=mode.loadImage(path)

    def frozenZombieImage(mode):
        mode.frozenZombieImages1=[]
        mode.frozenZombieImages2=[]
        for image in mode.commonZombiesSheets:
        # CITATION: I got the following code from 
        # https://www.cs.cmu.edu/~112/notes/notes-animations-part3.html#getAndPutPixels
        # and edit them to meet with my code's requirements
            mode.image1=image 
            mode.image1=mode.image1.convert('RGB')
            mode.image2=Image.new(mode='RGB',size=mode.image1.size)
            for x in range(mode.image2.width):
                for y in range(mode.image2.height):
                    r,g,b=mode.image1.getpixel((x,y))
                    mode.image2.putpixel((x,y),(0,0,b))
            # CITATION: I got the following code from 
            # https://stackoverflow.com/questions/765736/how-to-use-pil-to-make-all
            # -white-pixels-transparent
            # and edit them to meet with my code's requirements
            mode.image2=mode.image2.convert('RGBA')
            datas=mode.image2.getdata()
            newData=[]
            for item in datas:
                if (item[0]==0 and item[1]==0 and item[2]==0):
                    newData.append((255,255,255,0))
                else:
                    newData.append(item)
            mode.image2.putdata(newData)
            mode.frozenZombieImages1.append(mode.image2)
        mode.frozenZombieImagesCounter1=0
        for image in mode.eatingZombiesSheets:
        # CITATION: I got the following code from 
        # https://www.cs.cmu.edu/~112/notes/notes-animations-part3.html#getAndPutPixels
        # and edit them to meet with my code's requirements
            mode.image1=image 
            mode.image1=mode.image1.convert('RGB')
            mode.image2=Image.new(mode='RGB',size=mode.image1.size)
            for x in range(mode.image2.width):
                for y in range(mode.image2.height):
                    r,g,b=mode.image1.getpixel((x,y))
                    mode.image2.putpixel((x,y),(0,0,b))
            # CITATION: I got the following code from 
            # https://stackoverflow.com/questions/765736/how-to-use-pil-to-make-all
            # -white-pixels-transparent
            # and edit them to meet with my code's requirements
            mode.image2=mode.image2.convert('RGBA')
            datas=mode.image2.getdata()
            newData=[]
            for item in datas:
                if (item[0]==0 and item[1]==0 and item[2]==0):
                    newData.append((255,255,255,0))
                else:
                    newData.append(item)
            mode.image2.putdata(newData)
            mode.frozenZombieImages2.append(mode.image2)
        mode.frozenZombieImagesCounter2=0

    def appStarted(mode):
        super().appStarted()
        mode.snowpeaSpriteSheets()
        mode.initializesnowPea()
        mode.frozenZombieImage()
        mode.snowpeaShooters=[]
        mode.plantsnowPea=False
        mode.snowpeaCD=0
        mode.snowpeaCD1=8
        mode.snowpeas=[]
        # CITATION: I got the image from 
        # https://plantsvszombies.fandom.com/wiki/Snow_Pea/Gallery
        mode.snowpeaBoard=mode.loadImage('snowpeaboard.png')
        mode.snowpeaBoard=mode.scaleImage(mode.snowpeaBoard,5.2/5)

    def produceZombies(mode):
        mode.zombieTime+=0.12
        if (mode.zombieTime>=mode.produceZombiesRate and commonZombies2.count>0):
            mode.zombieTime=0
            ranRow=random.randint(0,4)
            x=801
            y=mode.yMargin+(ranRow+0.5)*mode.cellHeight
            commonZombieInstance=commonZombies2(x,y,ranRow)
            mode.commonZombies.append(commonZombieInstance)
    
    def eatPlants(mode):
        for zombie in mode.commonZombies:
            if (mode.isEat(zombie)):
                (row,col)=mode.getCell(zombie.x,zombie.y)
                zombie.isMove=False
                if (zombie.isFrozen):
                    mode.plantList[row][col].life-=1
                else:
                    mode.plantList[row][col].life-=2
            else:
                zombie.isMove=True

    def checkLose(mode):
        for zombie in mode.commonZombies:
            if (zombie.x<0):
                mode.appStarted()
                commonZombies2.count=20
                mode.app.setActiveMode(mode.app.LoseScreen)

    def checkWin(mode):
        if (commonZombies2.count==0 and mode.commonZombies==[]):
            mode.appStarted()
            commonZombies2.count=20
            mode.app.setActiveMode(mode.app.WinScreen)

    def keyPressed(mode,event):
        super().keyPressed(event)
        if (event.key=='n'):
            mode.snowpeaCD1=1.2

    def mousePressed(mode,event):
        if (mode.isPause):
            if (235<event.x<570 and 310<event.y<390):
                mode.isPause=False
                mode.loadPause=False
            elif (300<event.x<513 and 245<event.y<282):
                mode.appStarted()
                commonZombies2.count=20
                mode.app.setActiveMode(mode.app.FirstScreen)
            elif(300<event.x<513 and 200<event.y<240):
                mode.appStarted()
                commonZombies2.count=20
            return

        if (mode.width-145<event.x<mode.width and 0<event.y<35):
            mode.isPause=True
            mode.loadPause=True

        elif (150<event.x<200 and 8<event.y<75):
            if (mode.plantSun):
                mode.plantSun=False
            elif (mode.sunCounter>=50 and mode.sunCD==0):
                mode.plantSun=True
                return 

        elif (88<event.x<138 and 8<event.y<75):
            if (mode.plantPea):
                mode.plantPea=False
            elif (mode.sunCounter>=100 and mode.peaCD==0):
                mode.plantPea=True
                return 

        elif (212<event.x<262 and 7<event.y<78):
            if (mode.plantsnowPea):
                mode.plantsnowPea=False
            elif (mode.sunCounter>=175 and mode.snowpeaCD==0):
                mode.plantsnowPea=True
                return 

        elif (460<event.x<545 and 0<event.y<88):
            mode.useShovel=not mode.useShovel
    
        (row,col)=mode.getCell(event.x,event.y)
        if (row<0 or row>4 or col<0 or col>8):
            return

        if (mode.plantSun and mode.plantList[row][col]==None):
            sunFlowerInstance=SunFlowers(row,col)
            mode.sunFlowers.append(sunFlowerInstance)
            mode.plantList[row][col]=sunFlowerInstance
            mode.sunCounter-=50
            mode.plantSun=False
            mode.sunCD=7

        elif (mode.plantPea and mode.plantList[row][col]==None):
            peaShooterInstance=PeaShooters(row,col)
            mode.peaShooters.append(peaShooterInstance)
            mode.plantList[row][col]=peaShooterInstance
            mode.sunCounter-=100
            mode.plantPea=False
            mode.peaCD=8
        
        elif (mode.plantsnowPea and mode.plantList[row][col]==None):
            snowpeaShooterInstance=SnowPeaShooters(row,col)
            mode.snowpeaShooters.append(snowpeaShooterInstance)
            mode.plantList[row][col]=snowpeaShooterInstance
            mode.sunCounter-=175
            mode.plantsnowPea=False
            mode.snowpeaCD=mode.snowpeaCD1

        elif (mode.useShovel and mode.plantList[row][col]!=None):
            plant=mode.plantList[row][col]
            if (isinstance(plant,SunFlowers)):
                mode.sunFlowers.remove(plant)
            elif (isinstance(plant,PeaShooters)):
                mode.peaShooters.remove(plant)
            elif (isinstance(plant,SnowPeaShooters)):
                mode.snowpeaShooters.remove(plant)
            mode.plantList[row][col]=None
            mode.useShovel=False

        elif (mode.hasDropSun[row][col]):
            mode.sunCounter+=25
            index=mode.checkSun(row,col)
            mode.dropSuns.pop(index)
            mode.hasDropSun[row][col]=False

        elif (mode.hasProducedSun[row][col]):
            mode.sunCounter+=25
            index=mode.checkSun2(row,col)
            mode.producedSuns.pop(index)
            mode.hasProducedSun[row][col]=False
    
    def snowpeaShootertimerFired(mode):
        mode.snowpeaSheetCounter=(1+mode.snowpeaSheetCounter)%len(mode.snowpeaSheets)

    def snowpeaShooterCD(mode):
        if (mode.snowpeaCD!=0):
            mode.snowpeaCD-=0.12
            if (mode.snowpeaCD<=0):
                mode.snowpeaCD=0

    def snowpeatimerFired(mode):
        for snowpea in mode.snowpeas:
            snowpea.x+=50

    def removesnowPeaShooters(mode):
        index=0
        while (index<len(mode.snowpeaShooters)):
            snowpeaShooter=mode.snowpeaShooters[index]
            if (snowpeaShooter.life<=0):
                mode.plantList[snowpeaShooter.row][snowpeaShooter.col]=None
                mode.snowpeaShooters.pop(index)
            else:
                index+=1

    def commonZombietimerFired(mode):
        mode.commonZombieSheetCounter=(1+mode.commonZombieSheetCounter)%len(mode.commonZombiesSheets)
        mode.eatingZombieSheetCounter=(1+mode.eatingZombieSheetCounter)%len(mode.eatingZombiesSheets)
        mode.frozenZombieImagesCounter1=(1+mode.frozenZombieImagesCounter1)%len(mode.frozenZombieImages1)
        mode.frozenZombieImagesCounter2=(1+mode.frozenZombieImagesCounter2)%len(mode.frozenZombieImages2)
        for zombie in mode.commonZombies:
            if (zombie.isMove):
                if not (zombie.isFrozen):
                    zombie.x-=3
                else:
                    zombie.x-=1.5

    def attackZombies(mode):
        for i in range(5):
            for j in range (9):
                plant=mode.plantList[i][j]
                if (isinstance(plant,PeaShooters)):
                    if (mode.isAttack(plant)):
                        if (mode.almostEqual(plant.time,1.08)):
                            (x0,y0,x1,y1)=mode.getCellBounds(plant.row,plant.col)
                            cx=(x0+x1)/2
                            cy=(y0+y1)/2
                            peaInstance=Pea(cx,cy)
                            mode.peas.append(peaInstance)
                            plant.time-=0.12
                        else:
                            plant.time-=0.12
                            if (plant.time<=0):
                                plant.time=1.08
                elif (isinstance(plant,SnowPeaShooters)):
                    if (mode.isAttack(plant)):
                        if (mode.almostEqual(plant.time,1.08)):
                            (x0,y0,x1,y1)=mode.getCellBounds(plant.row,plant.col)
                            cx=(x0+x1)/2
                            cy=(y0+y1)/2
                            snowpeaInstance=SnowPea(cx,cy)
                            mode.snowpeas.append(snowpeaInstance)
                            plant.time-=0.12
                        else:
                            plant.time-=0.12
                            if (plant.time<=0):
                                plant.time=1.08

    def hitZombies(mode):
        index=0
        while (index<len(mode.peas)):
            if (mode.isHit(mode.peas[index])!=None):
                zombie=mode.isHit(mode.peas[index])
                zombie.life-=10
                mode.peas.pop(index)
            else:
                index+=1
        while (index<len(mode.snowpeas)):
            if (mode.isHit(mode.snowpeas[index])!=None):
                zombie=mode.isHit(mode.snowpeas[index])
                zombie.life-=10
                zombie.isFrozen=True
                zombie.frozenTime=8
                mode.snowpeas.pop(index)
            else:
                index+=1

    def disFrozen(mode):
        for zombie in mode.commonZombies:
            zombie.frozenTime-=0.12
            if (zombie.frozenTime<=0):
                zombie.isFrozen=False
                zombie.frozenTime=0

    def timerFired(mode):
        if (mode.isPause): 
            return 
        if (mode.sunFlowers!=[]):
            mode.sunFlowertimerFired()
            mode.produceSun()
        if (mode.peaShooters!=[]):
            mode.peaShootertimerFired()
        if (mode.snowpeaShooters!=[]):
            mode.snowpeaShootertimerFired()
        if (mode.commonZombies!=[]):
            mode.commonZombietimerFired()
        if (mode.peas!=[]):
            mode.peatimerFired()
        if (mode.snowpeas!=[]):
            mode.snowpeatimerFired()
        mode.checkWin()
        mode.checkLose()
        mode.dropSun()
        mode.eliminateSun()
        mode.sunFlowerCD()
        mode.peaShooterCD()
        mode.snowpeaShooterCD()
        mode.produceZombies()
        mode.attackZombies()
        mode.hitZombies()
        mode.disFrozen()
        mode.eatPlants()
        mode.removeSunFlowers()
        mode.removePeaShooters()
        mode.removesnowPeaShooters()
        mode.removeCommonZombies()
    
    def drawsnowpeaShooters(mode,canvas):
        image=mode.snowpeaSheets[mode.snowpeaSheetCounter]
        for snowpea in mode.snowpeaShooters:
            (x0,y0,x1,y1)=mode.getCellBounds(snowpea.row,snowpea.col)
            cx=(x0+x1)/2
            cy=(y0+y1)/2
            canvas.create_image(cx,cy,image=ImageTk.PhotoImage(image))

    def drawsnowPeas(mode,canvas):
        for snowpea in mode.snowpeas:
            canvas.create_image(snowpea.x,snowpea.y,image=ImageTk.PhotoImage(mode.snowpeaImage))

    def drawCommonZombies(mode,canvas):
        for zombie in mode.commonZombies:
            if (zombie.isMove):
                if (zombie.isFrozen):
                    image=mode.frozenZombieImages1[mode.frozenZombieImagesCounter1]
                else:
                    image=mode.commonZombiesSheets[mode.commonZombieSheetCounter]
            else:
                if (zombie.isFrozen):
                    image=mode.frozenZombieImages2[mode.frozenZombieImagesCounter2]
                else:
                    image=mode.eatingZombiesSheets[mode.eatingZombieSheetCounter]
            canvas.create_image(zombie.x,zombie.y,
                                image=ImageTk.PhotoImage(image))

    def drawProcess(mode,canvas):
        ratio=(20-commonZombies2.count)/20
        if (ratio>0):
            # CITATION: I got the color name from 
            # https://matplotlib.org/3.1.0/gallery/color/named_colors.html
            canvas.create_text(500,585,text='Medium Level',font='Arial 14 bold',fill='peru')
            canvas.create_rectangle(585,578,735,592,outline='steelblue',width=5)
            canvas.create_rectangle(587,580,735-(735-585)*ratio,590,fill='black',width=0)
            canvas.create_rectangle(735-(735-585)*ratio,580,733,590,fill='greenyellow',width=0)
            canvas.create_image(735-(735-585)*ratio,(578+592)/2,
                                image=ImageTk.PhotoImage(mode.zombieHead))
        else:
            # CITATION: I got the color name from 
            # https://matplotlib.org/3.1.0/gallery/color/named_colors.html
            canvas.create_text(560,585,text='Medium Level',font='Arial 14 bold',fill='peru')

    def redrawAll(mode,canvas):
        canvas.create_image(mode.width/2,mode.height/2,
                            image=ImageTk.PhotoImage(mode.background))
        canvas.create_image(mode.width,0,
                            image=ImageTk.PhotoImage(mode.menuButton),anchor='ne')
        mode.drawPlantBoard(canvas)
        canvas.create_image(502,44,image=ImageTk.PhotoImage(mode.shovel))
        canvas.create_image((212+262)/2,(7+78)/2,image=ImageTk.PhotoImage(mode.snowpeaBoard))
        mode.drawProcess(canvas)
        if (mode.sunFlowers!=[]):
            mode.drawsunFlower(canvas)
        if (mode.peaShooters!=[]):
            mode.drawpeaShooters(canvas)
        if (mode.snowpeaShooters!=[]):
            mode.drawsnowpeaShooters(canvas)
        if (mode.dropSuns!=[] or mode.producedSuns!=[]):
            mode.drawSun(canvas)
        if (mode.commonZombies!=[]):
            mode.drawCommonZombies(canvas)
        if (mode.peas!=[]):
            mode.drawPeas(canvas)
        if (mode.snowpeas!=[]):
            mode.drawsnowPeas(canvas)
        if (mode.loadPause):
            canvas.create_image(mode.width/2,mode.height/2,
                                image=ImageTk.PhotoImage(mode.pauseScreen))
        if (mode.plantSun):
            canvas.create_rectangle(150,8,200,75,outline='red')
        if (mode.sunCD!=0):
            canvas.create_text(175,41.5,text=str(math.ceil(mode.sunCD)),
                               font='Arial 20 bold',fill='red')
        if (mode.plantPea):
            canvas.create_rectangle(88,8,138,75,outline='blue')
        if (mode.peaCD!=0):
            canvas.create_text(113,41.5,text=str(math.ceil(mode.peaCD)),
                               font='Arial 20 bold',fill='blue')
        if (mode.plantsnowPea):
            canvas.create_rectangle(212,7,262,78,outline='orange')
        if (mode.snowpeaCD!=0):
            canvas.create_text(237,42.5,text=str(math.ceil(mode.snowpeaCD)),
                               font='Arial 20 bold',fill='orange')
        if (mode.useShovel):
            canvas.create_rectangle(460,0,545,88,outline='yellow')

class HardMode(EasyMode):
    def appStarted(mode):
        super().appStarted()
        mode.sunCounter=100
        mode.sunCD1=5.7
        mode.peaCD1=6.6

    def produceZombies(mode):
        mode.zombieTime+=0.12
        if (mode.zombieTime>=mode.produceZombiesRate and commonZombies1.count>0):
            mode.zombieTime=0
            ranRow=random.randint(0,4)
            x=801
            y=mode.yMargin+(ranRow+0.5)*mode.cellHeight
            commonZombieInstance=commonZombies1(x,y,ranRow)
            mode.commonZombies.append(commonZombieInstance)

    def checkLose(mode):
        for zombie in mode.commonZombies:
            if (zombie.x<0):
                mode.appStarted()
                commonZombies1.count=30
                mode.app.setActiveMode(mode.app.LoseScreen)

    def checkWin(mode):
        if (commonZombies1.count==0 and mode.commonZombies==[]):
            mode.appStarted()
            commonZombies1.count=30
            mode.app.setActiveMode(mode.app.WinScreen)

    def dropSun(mode):
        mode.dropSunTime+=0.12
        if (mode.almostEqual(mode.dropSunTime,7.8)):
            mode.dropSunTime=0
            currSun=[]
            for sun in mode.dropSuns:
                (row,col)=(sun.row,sun.col)
                currSun.append((row,col))
            while True:
                ranRow=random.randint(0,4)
                ranCol=random.randint(0,8)
                if (not isinstance(mode.plantList[ranRow][ranCol],SunFlowers)):
                    sunInstance=Sun(ranRow,ranCol)
                    mode.dropSuns.append(sunInstance)
                    mode.hasDropSun[ranRow][ranCol]=True
                    return 

    def checkLose(mode):
        for zombie in mode.commonZombies:
            if (zombie.x<0):
                mode.appStarted()
                commonZombies1.count=30
                mode.app.setActiveMode(mode.app.LoseScreen)

    def checkWin(mode):
        if (commonZombies1.count==0 and mode.commonZombies==[]):
            mode.appStarted()
            commonZombies1.count=30
            mode.app.setActiveMode(mode.app.WinScreen)

    def mousePressed(mode,event):
        if (mode.isPause):
            if (235<event.x<570 and 310<event.y<390):
                mode.isPause=False
                mode.loadPause=False
            elif (300<event.x<513 and 245<event.y<282):
                mode.appStarted()
                commonZombies1.count=30
                mode.app.setActiveMode(mode.app.FirstScreen)
            elif(300<event.x<513 and 200<event.y<240):
                mode.appStarted()
                commonZombies1.count=30
            return

        if (mode.width-145<event.x<mode.width and 0<event.y<35):
            mode.isPause=True
            mode.loadPause=True

        elif (557<event.x<613 and 0<event.y<62):
            mode.showHint=not mode.showHint

        elif (150<event.x<200 and 8<event.y<75):
            if (mode.plantSun):
                mode.plantSun=False
            elif (mode.sunCounter>=50 and mode.sunCD==0):
                mode.plantSun=True
                return 

        elif (88<event.x<138 and 8<event.y<75):
            if (mode.plantPea):
                mode.plantPea=False
            elif (mode.sunCounter>=100 and mode.peaCD==0):
                mode.plantPea=True
                return 
        
        elif (460<event.x<545 and 0<event.y<88):
            mode.useShovel=not mode.useShovel

        (row,col)=mode.getCell(event.x,event.y)
        if (row<0 or row>4 or col<0 or col>8):
            return

        if (mode.plantSun and mode.plantList[row][col]==None):
            sunFlowerInstance=SunFlowers(row,col)
            mode.sunFlowers.append(sunFlowerInstance)
            mode.plantList[row][col]=sunFlowerInstance
            mode.sunCounter-=50
            mode.plantSun=False
            mode.sunCD=mode.sunCD1

        elif (mode.plantPea and mode.plantList[row][col]==None):
            peaShooterInstance=PeaShooters(row,col)
            mode.peaShooters.append(peaShooterInstance)
            mode.plantList[row][col]=peaShooterInstance
            mode.sunCounter-=100
            mode.plantPea=False
            mode.peaCD=mode.peaCD1

        elif (mode.useShovel and mode.plantList[row][col]!=None):
            plant=mode.plantList[row][col]
            if (isinstance(plant,SunFlowers)):
                mode.sunFlowers.remove(plant)
            elif (isinstance(plant,PeaShooters)):
                mode.peaShooters.remove(plant)
            mode.plantList[row][col]=None
            mode.useShovel=False

        elif (mode.hasDropSun[row][col]):
            mode.sunCounter+=25
            index=mode.checkSun(row,col)
            mode.dropSuns.pop(index)
            mode.hasDropSun[row][col]=False

        elif (mode.hasProducedSun[row][col]):
            mode.sunCounter+=25
            index=mode.checkSun2(row,col)
            mode.producedSuns.pop(index)
            mode.hasProducedSun[row][col]=False

    def updateEat(mode):
        for zombie in mode.commonZombies:
            zombie.isEat=super().isEat(zombie)
            
    def timerFired(mode):
        super().timerFired()
        if (mode.commonZombies!=[] and not mode.isPause):
            mode.updateEat()
            mode.cleverZombies()
            mode.changeZombies()

    def hasZombie(mode,zombie,peaShooter):
        (x0,y0,x1,y1)=super().getCellBounds(peaShooter.row,peaShooter.col)
        cx=(x0+x1)/2
        for currZombie in mode.commonZombies:
            if (currZombie!=zombie):
                if (cx<currZombie.x<zombie.x and super().almostEqual(zombie.y,currZombie.y)):
                    return True
        return False

    def getAttackValue(mode,zombie,row,col):
        total=0
        for j in range(col+1):
            if (isinstance(mode.plantList[row][j],PeaShooters)):
                peaShooter=mode.plantList[row][j]
                (x0,y0,x1,y1)=super().getCellBounds(row,j)
                cx=(x0+x1)/2
                if not (mode.hasZombie(zombie,peaShooter)):
                    total+=max(zombie.x-cx,0)
        return total

    def getLifeValue(mode,row):
        total=0
        for zombie in mode.commonZombies:
            if (zombie.row==row):
                total+=zombie.life
        return total

    def compareTwoRows(mode,ratio,row1,row2,row,col):
        if (max(abs(ratio[row1]-ratio[row2]),0.0000000000001)>60):
            if (ratio[row1]>ratio[row2]):
                bestRow=row2
            else:
                bestRow=row1
        else:
            bestRow=mode.getBestRowHelper(row1,row2,row,col)
        return bestRow

    def getBestRow(mode,ratio,row,col):
        if (ratio[0]==None):
            bestRow=mode.compareTwoRows(ratio,1,2,row,col)
        elif (ratio[2]==None):
            bestRow=mode.compareTwoRows(ratio,0,1,row,col)
        else:
            bestRow=mode.compareTwoRows(ratio,0,1,row,col)
            bestRow=mode.compareTwoRows(ratio,bestRow,2,row,col)
        return bestRow

    def countSunFlowers(mode,row,col):
        total=0
        for j in range(col+1):
            if (isinstance(mode.plantList[row][j],SunFlowers)):
                total+=1
        return total
        
    def countDistance(mode,row,col):
        for j in range(col,-1,-1):
            if (mode.plantList[row][j]!=None):
                return j
        return 100

    def getBestRowHelper(mode,row1,row2,row,col):
        newRow1=row+row1-1
        newRow2=row+row2-1
        total1=mode.countSunFlowers(newRow1,col)
        total2=mode.countSunFlowers(newRow2,col)
        if (total1>total2):
            bestRow=row1
        elif (total2>total1):
            bestRow=row2
        else:
            distance1=mode.countDistance(newRow1,col)
            distance2=mode.countDistance(newRow2,col)
            if (distance1>distance2):
                bestRow=row2
            elif (distance2>distance1):
                bestRow=row1
            else:
                if (row1==1):
                    bestRow=row1
                elif (row2==1):
                    bestRow=row2
                else:
                    ranRow=random.randint(0,1)
                    if (ranRow==0):
                        bestRow=row1
                    else:
                        bestRow=row2
        return bestRow

    def cleverZombies(mode):
        for zombie in mode.commonZombies:
            if (zombie.isChange or zombie.isEat):
                continue
            (row,col)=super().getCell(zombie.x,zombie.y)
            if (row==-1):
                continue
            attackValue=[None]*3
            lifeValue=[None]*3
            ratios=[None]*3
            bestRow=None
            for i in [-1,0,1]:
                if (row+i>=0 and row+i<=4):
                    attackValue[i+1]=mode.getAttackValue(zombie,row+i,col)
                    lifeValue[i+1]=mode.getLifeValue(row+i)
                    ratios[i+1]=attackValue[i+1]-lifeValue[i+1]
                    if (ratios[i+1]==0):
                        ratios[i+1]=0.000000001
            bestRow=mode.getBestRow(ratios,row,col)-1+row
            if (bestRow!=row):
                zombie.isChange=True
                zombie.changeTimes=20
                zombie.row=bestRow

    def commonZombietimerFired(mode):
        mode.commonZombieSheetCounter=(1+mode.commonZombieSheetCounter)%len(mode.commonZombiesSheets)
        mode.eatingZombieSheetCounter=(1+mode.eatingZombieSheetCounter)%len(mode.eatingZombiesSheets)
        for zombie in mode.commonZombies:
            if (zombie.isMove and not zombie.isChange):
                zombie.x-=2

    def changeZombies(mode):
        for zombie in mode.commonZombies:
            if (zombie.isChange):
                (currRow,currCol)=mode.getCell(zombie.x,zombie.y)
                (x0,y0,x1,y1)=mode.getCellBounds(zombie.row,currCol)
                cy=(y0+y1)/2
                if (zombie.y<cy):
                    change=5.05
                else:
                    change=-5.05
                if (zombie.changeTimes>0):
                    zombie.y+=change
                    zombie.changeTimes-=1
                elif(zombie.changeTimes==0):
                    zombie.isChange=False
                
    def drawProcess(mode,canvas):
        ratio=(30-commonZombies1.count)/30
        if (ratio>0):
            # CITATION: I got the color name from 
            # https://matplotlib.org/3.1.0/gallery/color/named_colors.html
            canvas.create_text(520,585,text='Hard Level',font='Arial 14 bold',fill='peru')
            canvas.create_rectangle(585,578,735,592,outline='steelblue',width=5)
            canvas.create_rectangle(587,580,735-(735-585)*ratio,590,fill='black',width=0)
            canvas.create_rectangle(735-(735-585)*ratio,580,733,590,fill='greenyellow',width=0)
            canvas.create_image(735-(735-585)*ratio,(578+592)/2,
                                image=ImageTk.PhotoImage(mode.zombieHead))
        else:
            # CITATION: I got the color name from 
            # https://matplotlib.org/3.1.0/gallery/color/named_colors.html
            canvas.create_text(580,585,text='Hard Level',font='Arial 14 bold',fill='peru')


class WinScreen(Mode):
    def appStarted(mode):
        # CITATION: I got the image from 
        # https://plantsvszombies.fandom.com/pl/wiki/Adventure_Mode
        mode.image=mode.loadImage("win.jpg")
        imageWidth,imageHeight=mode.image.size
        mode.image=mode.scaleImage(mode.image,800/imageWidth)
        # CITATION: I got the full image from 
        # https://gaming.stackexchange.com/questions/17001/
        # how-can-i-run-plant-vs-zombies-in-a-resizable-window-mode
        # and crop the partial image from it
        mode.mainMenu=mode.loadImage('main menu.png')

    def mousePressed(mode,event):
        if (295<event.x<505 and 0<event.y<40):
            mode.app.setActiveMode(mode.app.FirstScreen)

    def redrawAll(mode,canvas):
        canvas.create_image(mode.width/2,mode.height/2,
                            image=ImageTk.PhotoImage(mode.image))
        canvas.create_image(mode.width/2,0,anchor='n',
                            image=ImageTk.PhotoImage(mode.mainMenu))

class LoseScreen(Mode):
    def appStarted(mode):
        # CITATION: I got the image from 
        # https://www.youtube.com/watch?v=WAtPIsRHprk
        mode.image=mode.loadImage("lose.jpg")
        imageWidth,imageHeight=mode.image.size
        mode.image=mode.scaleImage(mode.image,800/imageWidth)
        # CITATION: I got the full image from 
        # https://gaming.stackexchange.com/questions/17001/
        # how-can-i-run-plant-vs-zombies-in-a-resizable-window-mode
        # and crop the partial image from it
        mode.mainMenu=mode.loadImage('main menu.png')

    def mousePressed(mode,event):
        if (295<event.x<505 and 0<event.y<40):
            mode.app.setActiveMode(mode.app.FirstScreen)

    def redrawAll(mode,canvas):
        canvas.create_image(mode.width/2,mode.height/2,
                            image=ImageTk.PhotoImage(mode.image))
        canvas.create_image(mode.width/2,0,anchor='n',
                            image=ImageTk.PhotoImage(mode.mainMenu))

class MainMode(ModalApp):
    def appStarted(app):
        app.FirstScreen=FirstScreen()
        app.ChooseMode=ChooseMode()
        app.EasyMode=EasyMode()
        app.MediumMode=MediumMode()
        app.HardMode=HardMode()
        app.WinScreen=WinScreen()
        app.LoseScreen=LoseScreen()
        app.setActiveMode(app.FirstScreen)

app=MainMode(width=800, height=600)