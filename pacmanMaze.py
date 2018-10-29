import pygame
from Tkinter import Tk


class Ghost(pygame.sprite.Sprite):
    def __init__(self,image,ghostXPosition,ghostYPosition,name):
        self.rect = image.get_rect()
        self.rect.x = ghostXPosition
        self.rect.y = ghostYPosition
        self.name = name
class Node:
    def __init__(self,nodeXPosition,nodeYPosition, key):
        self.x = nodeXPosition
        self.y = nodeYPosition
        self.key = key


class Node1:
    def __init__(self,nodeXPosition,nodeYPosition, key, nodeWeight, nodeName):
        self.x = nodeXPosition
        self.y = nodeYPosition
        self.key = key
        self.weight = nodeWeight
        self.name = nodeName




class NodesProximity:
    def __init__(self,nodeXPosition,nodeYPosition,proximityToPacman, name):
        self.proximitiyToPacman = proximityToPacman
        self.nodeXPosition = nodeXPosition
        self.nodeYPosition = nodeYPosition
        self.name = name





class Brick(pygame.sprite.Sprite):
     def __init__(self,image,rectX,rectY):
       self.image = image
       self.rect = image.get_rect()
       self.rect.x = rectX
       self.rect.y = rectY
       self.rect.width = 15
       self.rect.height = 15




class PacMan(pygame.sprite.Sprite):
    def __init__(self, image):
        self.image = image
        self.rect = image.get_rect()
        self.rect.width = 50
        self.rect.height = 50


class Food(pygame.sprite.Sprite):

    def __init__(self,image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = image.get_rect()

brickGroup = pygame.sprite.Group()
foodGroup = pygame.sprite.Group()
ticks = 0


startPacmanAnimation = False

numberOfColumns = 2000
numberOfRows = 2000
i = 0
j = 0
Matrix = [[0 for x in range(numberOfRows)] for y in range(numberOfColumns)]



nodeArray = []
key = 0
count  = 0
rightPath = 999999
leftPath = 999999
upPath = 999999
downPath = 99999
goRightVirtualXGhostPosition = 0
goRightGhostXPosition =0
goUpVirtualGhostYPosition =0
goUpGhostYPosition = 0
goLeftVirtualXGhostPosition = 0
goLeftGhostXPosition = 0
goDownVirtualYGhostPosition = 0
goDownGhostYPosition = 0

goalNode = 0

rightNode = 0
leftNode = 0
upNode = 0
downNode = 0







def NavigateUsingShortestPath(virtualXGhostPosition, virtualYGhostPosition, GhostXPosition,GhostYPosition,pacmanXPosition,pacmanYPosition,brickGroup, NodeGroup,ghost):
   global blinkyXPosition
   global blinkyYPosition
   global inkyXPosition
   global inkyYPosition
   global clydeXPosition
   global clydeYPosition
   RightBrickFaced = False
   RightNodeFaced = False
   LeftBrickFaced = False
   LeftNodeFaced = False
   UpBrickFaced = False
   UpNodeFaced = False
   DownBrickFaced = False
   DownNodeFaced = False

   global count
   global goRightVirtualXGhostPosition
   global goLeftVirtualXGhostPosition
   global goUpVirtualGhostYPosition
   global goRightGhostXPosition
   global goLeftGhostXPosition
   global goDownGhostYPosition
   global goUpGhostYPosition
   global goDownVirtualYGhostPosition
   global leftPath
   global rightPath
   global downPath
   global upPath
   global leftNode
   global rightNode
   global upNode
   global downNode
   global goalNode


   rightPath = 9999




   weightOfRightPath = 999999
   weightOfLeftPath = 999999
   weightOfUpPath = 999999
   weightOfDownPath = 99999

   goRightGhostXPosition = GhostXPosition
   goUpGhostYPosition = GhostYPosition

   goLeftGhostXPosition = GhostXPosition

   goDownGhostYPosition = GhostYPosition




   goRightVirtualXGhostPosition = virtualXGhostPosition
   goUpVirtualGhostYPosition = virtualYGhostPosition
   goLeftVirtualXGhostPosition = virtualXGhostPosition
   goDownVirtualYGhostPosition = virtualYGhostPosition







   goalNode = 0

   rightNode = 0
   leftNode = 0
   upNode = 0
   downNode = 0






   for brick in brickGroup:


       for node in nodeArray:




        if node != 0:





           if node.x != goRightVirtualXGhostPosition + 20 and brick.rect.x !=goRightGhostXPosition:
               goRightVirtualXGhostPosition = goRightVirtualXGhostPosition + 20
               goRightGhostXPosition = goRightGhostXPosition + 20
               weightOfRightPath = weightOfRightPath + 20


           if brick.rect.x == goRightGhostXPosition:
               weightOfRightPath = 99999
               RightBrickFaced = True
               node1 = Node1(node.x,node.y,node.key,weightOfRightPath,"rightNode")
               rightNode = node1





           if node.x == goRightVirtualXGhostPosition:
               RightNodeFaced = True
               node1 = Node1(node.x, node.y, node.key, weightOfRightPath, "rightNode")
               rightNode = node1


           if node.x != goLeftVirtualXGhostPosition - 20 and brick.rect.x != goLeftGhostXPosition:
                   goLeftVirtualXGhostPosition = goLeftVirtualXGhostPosition + 20
                   goLeftGhostXPosition = goLeftGhostXPosition + 20
                   weightOfLeftPath = weightOfLeftPath + 20

           if brick.rect.x == goLeftGhostXPosition:
                   weightOfRightPath = 99999
                   LeftBrickFaced = True
                   node1 = Node1(node.x, node.y, node.key, weightOfLeftPath, "leftNode")
                   leftNode = node1


           if node.x == goLeftVirtualXGhostPosition:
                   LeftNodeFaced = True
                   node1 = Node1(node.x, node.y, node.key, weightOfLeftPath, "leftNode")
                   leftNode = node1



           if node.y != goUpVirtualGhostYPosition - 20 and brick.rect.y != goUpGhostYPosition:
                   goUpVirtualGhostYPosition = goUpVirtualGhostYPosition - 20
                   goUpGhostYPosition = goUpGhostYPosition - 20
                   weightOfUpPath = weightOfUpPath + 20

           if brick.rect.y == goUpGhostYPosition:
                   weightOfUpPath = 99999
                   UpBrickFaced = True
                   node1 = Node1(node.x, node.y, node.key, weightOfUpPath, "upNode")
                   upNode = node1


           if node.y == goUpVirtualGhostYPosition:
                   UpNodeFaced = True
                   node1 = Node1(node.x, node.y, node.key, weightOfUpPath, "upNode")
                   upNode = node1


           if node.y != goDownVirtualYGhostPosition + 20 and brick.rect.y != goDownGhostYPosition:
               goDownVirtualYGhostPosition = goDownVirtualYGhostPosition + 20
               goDownGhostYPosition = goDownGhostYPosition + 20
               weightOfDownPath = weightOfDownPath + 20

           if brick.rect.y == goDownGhostYPosition:
               weightOfDownPath = 99999
               DownBrickFaced = True
               node1 = Node1(node.x, node.y, node.key, weightOfDownPath, "downNode")
               downNode = node1


           if node.y == goDownVirtualYGhostPosition:
               DownNodeFaced = True
               node1 = Node1(node.x, node.y, node.key, weightOfDownPath, "downNode")
               downNode = node1



       if (RightNodeFaced or RightBrickFaced) and (LeftBrickFaced or LeftNodeFaced) and (UpBrickFaced or UpNodeFaced) and (DownNodeFaced or DownBrickFaced):
           break;

   PathList = []

   PathList.append(downNode)
   print(PathList[0].weight)
   PathList.append(leftNode)
   print(PathList[1].weight)
   PathList.append(upNode)
   print(PathList[2].weight)
   PathList.append(rightNode)
   print(PathList[3].weight)






   PathList.sort(key = lambda x: x.weight)



   ProxNodeToPacman = []








   for node in PathList:

       if  node.name == "upNode":
         if GhostYPosition > node.y:
           proximityToPacman = GhostYPosition - node.weight
           node1 = NodesProximity(node.x,node.y,proximityToPacman,node.name)
           ProxNodeToPacman.append(node1)


         if GhostYPosition < node.weight:
           proximityToPacman = node.weight - GhostYPosition
           node1 = NodesProximity(node.x, node.y, proximityToPacman,node.name)
           ProxNodeToPacman.append(node1)


       if node.name == "downNode":
           if GhostYPosition > node.y:
               proximityToPacman = GhostYPosition - node.weight
               node1 = NodesProximity(node.x, node.y, proximityToPacman,node.name)
               ProxNodeToPacman.append(node1)


           if GhostYPosition < node.weight:
            proximityToPacman = node.weight - GhostYPosition
            node1 = NodesProximity(node.x, node.y, proximityToPacman,node.name)
            ProxNodeToPacman.append(node1)


       if node.name == "leftNode":
           if GhostXPosition > node.x:
               proximityToPacman = GhostXPosition - node.weight
               node1 = NodesProximity(node.x, node.y, proximityToPacman,node.name)
               ProxNodeToPacman.append(node1)


           if GhostXPosition < node.weight:
            proximityToPacman = node.weight - GhostYPosition
            node1 = NodesProximity(node.x, node.y, proximityToPacman,node.name)
            ProxNodeToPacman.append(node1)


       if node.name == "rightNode":
           if GhostXPosition > node.x:
               proximityToPacman = GhostXPosition - node.weight
               node1 = NodesProximity(node.x, node.y, proximityToPacman,node.name)
               ProxNodeToPacman.append(node1)


           if GhostXPosition < node.weight:
            proximityToPacman = node.weight - GhostYPosition
            node1 = NodesProximity(node.x, node.y, proximityToPacman,node.name)
            ProxNodeToPacman.append(node1)




   ProxNodeToPacman.sort(key= lambda x : x.proximityToPacman)




   if ProxNodeToPacman[0].name == "upNode":
       goalNode = ProxNodeToPacman[0]



   if ProxNodeToPacman[0].name == "downNode":
       goalNode = ProxNodeToPacman[0]

   if ProxNodeToPacman[0].name == "leftNode":
       goalNode = ProxNodeToPacman[0]


   if ProxNodeToPacman[0].name == "rightNode":
       goalNode = ProxNodeToPacman[0]






   if goalNode != 0:
    if goalNode.name == "rightNode" and GhostXPosition != pacmanXPosition and goalNode.x != virtualXGhostPosition :
       if ghost.name == "inkey":
           inkyXPosition = inkyXPosition + 20
           virtualXGhostPosition = virtualXGhostPosition + 20
       if ghost.name == "blinkey":
           blinkyXPosition = blinkyXPosition + 20
           virtualXGhostPosition = virtualXGhostPosition + 20
       if ghost.name == "clyde":
           clydeXPosition = clydeXPosition + 20
           virtualXGhostPosition = virtualXGhostPosition + 20



   if goalNode != 0:
    if goalNode.name =="leftNode" and GhostXPosition != pacmanXPosition and goalNode.x != virtualXGhostPosition:
       if ghost.name == "inkey":
           inkyXPosition = inkyXPosition - 20
           virtualXGhostPosition = virtualXGhostPosition - 20
       if ghost.name == "blinkey":
           blinkyXPosition = blinkyXPosition - 20
           virtualXGhostPosition = virtualXGhostPosition - 20
       if ghost.name == "clyde":
           clydeXPosition = clydeXPosition - 20
           virtualXGhostPosition = virtualXGhostPosition - 20


   if goalNode != 0:
    if goalNode.name == "upNode" and GhostXPosition != pacmanYPosition and goalNode.y != virtualYGhostPosition:
       if ghost.name == "inkey":
           inkyYPosition = inkyYPosition - 20
           virtualYGhostPosition = virtualYGhostPosition - 20
       if ghost.name == "blinkey":
         blinkyYPosition = blinkyYPosition - 20
         virtualYGhostPosition = virtualYGhostPosition - 20
       if ghost.name == "clyde":
           clydeYPosition = clydeYPosition - 20
           virtualYGhostPosition = virtualYGhostPosition - 20



   if goalNode != 0:
    if goalNode.name == "downNode" and GhostXPosition != pacmanYPosition and goalNode.y != virtualYGhostPosition:
       if ghost.name == "inkey":
           inkyYPosition = inkyYPosition +20
           virtualYGhostPosition = virtualYGhostPosition + 20
       if ghost.name == "blinkey":
           blinkyYPosition = blinkyYPosition + 20
           virtualYGhostPosition = virtualYGhostPosition + 20
       if ghost.name == "clyde":
           clydeYPosition = clydeYPosition + 20
           virtualYGhostPosition = virtualYGhostPosition + 20


def makePacmanMaze(screen):
    global brickGroup
    global foodGroup
    global numberOfColumns
    global numberOfRows
    global nodeArray
    global i
    global Matrix
    global j
    global key









    i = 0
    j = 0

    brickGroup = pygame.sprite.Group()
    brickXPosition = 0
    brickYPosition = 0
    foodXPosition = 0
    foodYPosition = 0
    nodeXPosition = 0
    nodeYPosition = 0
    nodeArray = [0] * 500
    k = 0
    count = 2;

    file = open("pacmanportalmaze.txt","r")








    while True:
         c = file.read(1)


         if c == "\n":
             foodYPosition = foodYPosition + 20
             nodeYPosition = nodeYPosition + 20
             brickYPosition = brickYPosition + 20
             brickXPosition = 0
             foodXPosition = 0
             count = count + 1

             i = i + 20
             j = 0
             print("\n")
         food = pygame.image.load("images/points.png")

         Food1 = Food(food)
         Food1.rect.x = foodXPosition;
         Food1.rect.y = foodYPosition;






         if (c == "N"):
             node = Node(nodeXPosition,nodeYPosition,key)
             nodeArray[k] = node
             nodeXPosition = nodeXPosition + 20
             k = k + 1
             key = key + 1









         if(c== '.') and Matrix[Food1.rect.x][Food1.rect.y] != ".":





             foodGroup.add_internal(Food1)








             screen.blit(Food1.image, (foodXPosition,foodYPosition))
             foodXPosition = foodXPosition + 20
















         if(c == 'X'):


             Matrix[i][j] = "X"
             print(Matrix[i][j])
             j = j + 20






             brick = pygame.image.load("images/square.png")













             brickObject = Brick(brick,brickXPosition,brickYPosition)

             brickGroup.add_internal(brickObject)

             screen.blit(brick, (brickXPosition,brickYPosition))
             brickXPosition = brickXPosition + 20




         if(c!= 'X' and c!= "\n"):
             j = j + 20
             brickXPosition = brickXPosition + 20
             nodeXPosition = nodeXPosition + 20





         if not c:
            break

























screen = pygame.display.set_mode((2000,2000))


rect = pygame.Surface((50,50),pygame.SRCALPHA, 32)
rect.fill((255,255,255,0))



screen.set_alpha(0)
screen.fill((255,255,255))



pacman = pygame.image.load("images/pacman.png")

pacman = pygame.transform.scale(pacman,(50,50))



pacmanObject = PacMan(pacman)



xPositionForPacman = 10
yPositionForPacman = 20

rowForPacman = 20
columnForPacman = 20









makePacmanMaze(screen)










rowNumber = 0
columnNumber = 0



screen.blit(pacman,(xPositionForPacman,yPositionForPacman))
movingRight = False
movingLeft = False
movingUp = False
movingDown = False




hitWall = False
allowPacmanToComeOutOfX = True
allowPacmanToMoveRight = True
allowPacmanToMoveLeft = True
allowPacmanToMoveDown = True
allowPacmanToMoveUp = True
facingRight = True
facingLeft = False
facingDown = False
facingUp = False

fullClock = 0



blinkyXPosition = 400
blinkyYPosition = 400



clydeXPosition = 400
clydeYPosition = 400


inkyXPosition  = 400
inkyYPosition = 400



pinkyXPosition = 400
pinkyYPosition = 400

inky = pygame.image.load("images/InkyLookingMiddle.png")
blinky = pygame.image.load("images/blinkyLookingMiddle.png")
pinky = pygame.image.load("images/pinkyLookingMiddle.png")
clyde = pygame.image.load("images/clydeLookingMiddle.png")


Inky = Ghost(inky,inkyXPosition,inkyYPosition,"inkey")
Blinky = Ghost(blinky,blinkyXPosition,blinkyYPosition,"blinkey")
Clyde = Ghost(clyde,clydeXPosition,clydeYPosition, "clyde")


screen.blit(inky, (inkyXPosition, inkyYPosition))
screen.blit(blinky,(blinkyXPosition, blinkyYPosition))
screen.blit(pinky,(pinkyXPosition,pinkyYPosition))
screen.blit(clyde,(clydeXPosition,clydeYPosition))
pygame.display.update()










countForDoingLoop = 0;




node1 = 0
node2 = 0
node3 = 0
blinkyFinishedMovingUp = False
inkyFinishedMovingUp = False

virtualClydeYPosition = 440
virtualXClydePosition = 17580
virtualXBlinkyPosition = 17640
virtualYBlinkyPosition = 380

virtualXInkyPosition = 17480
virtualYInkyPosition = 380
blinkyFinishedMovingLeft = False
inkyFinishedMovingRight = False

while True:




























   if countForDoingLoop!= 1:

    for node in nodeArray:
     print("node key")
     print(node.key)
     if node!= 0:







      if node.key == 24:
          node2 = node


      if node.key == 25:

        node1 = node


      if node.key == 26:
         node3 = node

         break;

    countForDoingLoop = countForDoingLoop + 1




   if node1.y != virtualClydeYPosition:

     print("virtual cylde y position")
     print(virtualClydeYPosition)
     print("node y")
     print(node1.y)
     print("node x")
     print(node1.x)







     screen.fill((255,255,255))
     screen.blit(clyde,(clydeXPosition,clydeYPosition))
     screen.blit(pinky,(pinkyXPosition,pinkyYPosition))
     screen.blit(blinky,(blinkyXPosition,blinkyYPosition))
     screen.blit(inky,(inkyXPosition,inkyYPosition))
     clydeYPosition = clydeYPosition  -20
     blinkyYPosition = blinkyYPosition - 20
     inkyYPosition = inkyYPosition - 20
     virtualClydeYPosition = virtualClydeYPosition - 20
     if (node1.y == virtualClydeYPosition):
         blinkyFinishedMovingUp = True
         inkyFinishedMovingUp = True






   if node2.x != virtualXBlinkyPosition and blinkyFinishedMovingUp:
       print("virtual blinky X Position")
       print(virtualXBlinkyPosition)
       print("node 2 x position")
       print(node2.x)
       print("blinkyXPosition")
       print(blinkyXPosition)
       screen.fill((255,255,255))
       screen.blit(clyde, (clydeXPosition, clydeYPosition))
       screen.blit(pinky, (pinkyXPosition, pinkyYPosition))
       screen.blit(blinky, (blinkyXPosition, blinkyYPosition))
       screen.blit(inky, (inkyXPosition, inkyYPosition))


       virtualXBlinkyPosition = virtualXBlinkyPosition - 20

       blinkyXPosition = blinkyXPosition - 20



   if node2.x == virtualXBlinkyPosition:
        blinkyFinishedMovingLeft  = True



   if node3.x != virtualXInkyPosition and inkyFinishedMovingUp:
       print("inky virtual x position")
       print(virtualXInkyPosition)
       print("node 3 x position")
       print(node3.x)
       print("inkyXPosition")
       print(inkyXPosition)
       screen.fill((255, 255, 255))
       screen.blit(clyde, (clydeXPosition, clydeYPosition))
       screen.blit(pinky, (pinkyXPosition, pinkyYPosition))
       screen.blit(blinky, (blinkyXPosition, blinkyYPosition))
       screen.blit(inky, (inkyXPosition, inkyYPosition))



       virtualXInkyPosition = virtualXInkyPosition + 20

       inkyXPosition = inkyXPosition + 20


   if node3.x == virtualXInkyPosition:
       inkyFinishedMovingRight = True


   if inkyFinishedMovingRight and blinkyFinishedMovingLeft:
       NavigateUsingShortestPath(virtualXInkyPosition,virtualYInkyPosition,inkyXPosition,inkyYPosition,xPositionForPacman,yPositionForPacman,brickGroup,nodeArray,Inky)

       count =0
       NavigateUsingShortestPath(virtualXBlinkyPosition, virtualYBlinkyPosition, blinkyXPosition, blinkyYPosition,
                                 xPositionForPacman, yPositionForPacman, brickGroup, nodeArray,Blinky)

       count = 0

       NavigateUsingShortestPath(virtualXClydePosition, virtualClydeYPosition, clydeXPosition, clydeYPosition,
                                 xPositionForPacman, yPositionForPacman, brickGroup, nodeArray,Clyde)

























   hitWall = False











   pacmanObject.rect.x = xPositionForPacman
   pacmanObject.rect.y = yPositionForPacman

   collisions = pygame.sprite.spritecollide(pacmanObject, brickGroup, False)

   collisions1 = pygame.sprite.spritecollide(pacmanObject, foodGroup, True)


   if collisions1:




     startPacmanAnimation = True

     for food in collisions1:
         Matrix[food.rect.x][food.rect.y] = "."

























   if startPacmanAnimation:
        screen.fill((255, 255, 255))
        pacmanClosedImage = pygame.image.load("images/pacman1.png")
        pacmanClosedImage  = pygame.transform.scale(pacmanClosedImage,(400,400))
        screen.blit(pacmanClosedImage, (xPositionForPacman-200, yPositionForPacman-100))
        inky = pygame.image.load("images/InkyLookingMiddle.png")
        screen.blit(inky, (inkyXPosition, inkyYPosition))
        screen.blit(blinky, (blinkyXPosition, blinkyYPosition))
        screen.blit(pinky, (pinkyXPosition, pinkyYPosition))
        screen.blit(clyde, (clydeXPosition, clydeYPosition))




        ticks = ticks + 1


        print("ticks")
        print(ticks)
        if ticks == 10:

         screen.fill((255, 255, 255))
         screen.blit(pacman, (xPositionForPacman, yPositionForPacman))
         inky = pygame.image.load("images/InkyLookingMiddle.png")
         screen.blit(inky, (inkyXPosition, inkyYPosition))
         screen.blit(blinky, (blinkyXPosition, blinkyYPosition))
         screen.blit(pinky, (pinkyXPosition, pinkyYPosition))
         screen.blit(clyde, (clydeXPosition, clydeYPosition))
         startPacmanAnimation = False
         ticks = 0















   keys = pygame.key.get_pressed()















   # 56,50 at the black x

   #101,50 at the real black x y


















   if collisions and movingLeft  == True:

        allowPacmanToMoveDown = True
        allowPacmanToMoveLeft = False
        allowPacmanToMoveUp = True
        allowPacmanToMoveRight = True






   if collisions and movingRight  == True:

        allowPacmanToMoveDown = True
        allowPacmanToMoveLeft = True
        allowPacmanToMoveUp = True
        allowPacmanToMoveRight = False


   if collisions and movingDown  == True:

        allowPacmanToMoveDown = False
        allowPacmanToMoveLeft = True
        allowPacmanToMoveUp = True
        allowPacmanToMoveRight = True


   if collisions and movingUp  == True:

        allowPacmanToMoveDown = True
        allowPacmanToMoveLeft = True
        allowPacmanToMoveUp = False
        allowPacmanToMoveRight = True








   if keys[pygame.K_LEFT]:
       movingLeft = True
       movingRight = False
       movingDown = False
       movingUp = False


















       if  not collisions or  allowPacmanToMoveLeft:

        if fullClock == 0:
            pacman = pygame.transform.rotate(pacman,-180)
            fullClock = 2

        if fullClock == 3:
            pacman = pygame.transform.rotate(pacman,90 )
            fullClock = 2

        if fullClock == 1:
            pacman = pygame.transform.rotate(pacman, -90)
            fullClock = 2



        hitWall = True
        xPositionForPacman = xPositionForPacman -20
        columnForPacman = columnForPacman -20

        screen.fill((255,255,255))







        screen.blit(pacman, (xPositionForPacman, yPositionForPacman));
        screen.blit(pinky, (pinkyXPosition, pinkyYPosition))
        screen.blit(inky, (inkyXPosition, inkyYPosition))
        screen.blit(blinky, (blinkyXPosition, blinkyYPosition))
        screen.blit(clyde, (clydeXPosition, clydeYPosition))










   if keys[pygame.K_RIGHT] and (not collisions or allowPacmanToMoveRight == True):

        if fullClock == 1:
            pacman = pygame.transform.rotate(pacman,90)
            fullClock = 0


        if fullClock == 2:
            pacman = pygame.transform.rotate(pacman, -180)
            fullClock = 0


        if fullClock == 3:
            pacman = pygame.transform.rotate(pacman,-90)
            fullClock = 0




























        hitWall = True
        movingRight = True
        movingLeft = False
        movingUp = False
        movingDown = False
        print("row for pacman inside of this")
        print(rowForPacman)
        print("column for pacman inside of this")
        print(columnForPacman)
        print("Matrix for pacman inside of this")
        print(Matrix[rowForPacman][columnForPacman])




        xPositionForPacman = xPositionForPacman +20
        columnForPacman = columnForPacman + 20








        print("Matrix for pacman inside of this after make pacman maze")
        print(Matrix[rowForPacman][columnForPacman])
        screen.fill((255,255,255))
        screen.blit(pacman, (xPositionForPacman, yPositionForPacman));
        screen.blit(inky, (inkyXPosition, inkyYPosition))

        screen.blit(blinky, (blinkyXPosition, blinkyYPosition))
        screen.blit(pinky, (pinkyXPosition, pinkyYPosition))
        screen.blit(clyde, (clydeXPosition, clydeYPosition))








   if keys[pygame.K_UP] and (not collisions or allowPacmanToMoveUp):
        hitWall = True
        movingLeft = False
        movingRight = False
        movingDown = False
        movingUp = True




        if fullClock == 0:
            pacman = pygame.transform.rotate(pacman, 90)
            fullClock = 3


        if fullClock == 2:
            pacman = pygame.transform.rotate(pacman, -90)
            fullClock = 3


        if fullClock == 1:
            pacman = pygame.transform.rotate(pacman, -180)
            fullClock = 3

















        yPositionForPacman = yPositionForPacman - 20
        rowForPacman = rowForPacman -20

        screen.fill((255,255,255))






        screen.blit(pacman, (xPositionForPacman, yPositionForPacman));
        screen.blit(inky, (inkyXPosition, inkyYPosition))
        screen.blit(blinky, (blinkyXPosition, blinkyYPosition))
        screen.blit(pinky, (pinkyXPosition, pinkyYPosition))
        screen.blit(clyde, (clydeXPosition, clydeYPosition))





   if keys[pygame.K_DOWN] and (not collisions or allowPacmanToMoveDown):
        hitWall = True
        movingLeft = False
        movingRight = False
        movingDown = True
        movingUp = False




        if fullClock == 3:
            pacman = pygame.transform.rotate(pacman,-180)
            fullClock = 1

        if fullClock == 0:
            pacman = pygame.transform.rotate(pacman, -90)
            fullClock = 1


        if fullClock == 2:
            pacman = pygame.transform.rotate(pacman,90)
            fullClock = 1






        yPositionForPacman = yPositionForPacman + 20
        rowForPacman = rowForPacman+ 20

        screen.fill((255, 255, 255))





        screen.blit(pacman, (xPositionForPacman, yPositionForPacman));
        screen.blit(inky, (inkyXPosition, inkyYPosition))
        screen.blit(blinky, (blinkyXPosition, blinkyYPosition))
        screen.blit(pinky, (pinkyXPosition, pinkyYPosition))
        screen.blit(clyde, (clydeXPosition, clydeYPosition))













   for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()







   makePacmanMaze(screen)
   pygame.display.flip()

   pygame.display.update()






