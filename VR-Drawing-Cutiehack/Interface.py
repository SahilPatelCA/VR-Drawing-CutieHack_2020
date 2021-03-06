import socket
import pygame, math, time, sys, os
from ast import literal_eval


class GUI_Support:

    #Initializes the GUI display
    def initDisplay(self, dims):
        pygame.init()
        self.drawBool = False
        self.drawingColor = (0,0,0)
        self.BLACK = (0, 0, 0)
        self.RED = (255, 50, 50)
        self.YELLOW = (255, 255, 0)
        self.GREEN = (45, 87, 44)
        self.ORANGE = (246, 107, 41)
        self.GREY = (200, 200, 200)
        self.GREY2 = (236,236,236)
        self.BROWN = (101, 67, 33)
        self.WHITE = (255,255,255)
        self.CYAN = (0, 255, 255)
        self.BEIGE = (249,228,183)
        self.BEIGE2 = (207,185,151)
        self.thiccness = 3
        self.backgroundColor = (255,255,255)
        self.counter = 0
        return pygame.display.set_mode(dims)

    #Called when the x is clicked on the GUI
    def isQuit(self):
        pass

    #Function to draw and update GUI graphics as it receives new coordinates
    def drawGraphics(self, position, screen, dims):
        #For each event in the program
        for event in pygame.event.get():

            #If the close button is pressed
            if event.type == pygame.QUIT:
                # raise SystemExit
                pass

            #when mouse button is clicked, do nothing
            elif event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP:
                pass

            #When a button is pressed down
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    image = "Data/image" + str(self.counter) + ".jpg"
                    pygame.image.save(background, image)
                    self.counter +=1
                
                if event.key == pygame.K_c:
                    pygame.draw.rect(background,self.WHITE,(0,100,1200,900))
                    #screen.fill(self.WHITE)
                    #screen.blit(background, (0,0))

        indexX, indexY, indexZ = position[0]
        thumbX, thumbY, thumbZ = position[1]

        if(((indexX - thumbX) > 30) or ((thumbX - indexX) > 30) or ((indexZ - thumbZ) > 30) or ((thumbZ - indexZ) > 30)):
            self.drawBool = False
        else:
            self.drawBool = True
        indexX = indexX * 1.5
        indexZ = indexZ * 1.5
        thumbX = thumbX * 1.5
        thumbZ = thumbZ * 1.5

        #Centers the X and Z coordinates
        indexX += 600
        indexZ += 450
        
        thumbX += 600
        thumbZ += 450
       
        


        centerX = (indexX + thumbX)/2
        centerX = int(centerX)
        centerY = (indexY + thumbY)/40
        centerY = int(centerY)
        centerZ = (indexZ + thumbZ)/2
        centerZ = int(centerZ)

        width, height = dims
        screen.fill(self.backgroundColor)  #pass in chooseBackgroundColor() function
        circleRadius = centerY + 2

        
        #color palette lines
        screen.blit(background, (0,0))
        
        
        #dot
        pygame.draw.circle(screen, self.drawingColor, (centerX, centerZ), circleRadius)
        pygame.draw.circle(screen, self.BLACK, (centerX, centerZ), circleRadius+1,2)
            
            
        if(self.drawBool and not centerZ < 125):
            pygame.draw.circle(background,self.drawingColor,(centerX, centerZ), circleRadius)
        

        #color pallet
        pygame.draw.rect(background,self.BEIGE,(0,0,1200,100))
        pygame.draw.line(screen, self.BLACK, (0,100), (1200,100), 3)

        pygame.draw.circle(screen, self.BLACK, (50,50), 40)
        pygame.draw.circle(screen, self.BLACK, (50,50), 41, self.thiccness)

        pygame.draw.circle(screen, self.RED, (150,50), 40)
        pygame.draw.circle(screen, self.BLACK, (150,50), 41, self.thiccness)

        pygame.draw.circle(screen, self.ORANGE, (250,50), 40)
        pygame.draw.circle(screen, self.BLACK, (250,50), 41, self.thiccness)

        pygame.draw.circle(screen, self.GREEN, (350,50), 40)
        pygame.draw.circle(screen, self.BLACK, (350,50), 41, self.thiccness)

        pygame.draw.circle(screen, self.GREY, (450,50), 40)
        pygame.draw.circle(screen, self.BLACK, (450,50), 41, self.thiccness)

        pygame.draw.circle(screen, self.BROWN, (550,50), 40)
        pygame.draw.circle(screen, self.BLACK, (550,50), 41, self.thiccness)

        pygame.draw.circle(screen, self.YELLOW, (650,50), 40)
        pygame.draw.circle(screen, self.BLACK, (650,50), 41, self.thiccness)

        pygame.draw.circle(screen, self.CYAN, (750,50), 40)
        pygame.draw.circle(screen, self.BLACK, (750,50), 41, self.thiccness)

        pygame.draw.circle(screen, self.WHITE, (850,50), 40)
        pygame.draw.circle(screen, self.BLACK, (850,50), 41, self.thiccness)
        erasorImg = pygame.image.load('eraser.png')
        erasorImg = pygame.transform.scale(erasorImg, (40, 40))
        screen.blit(erasorImg, (829,29))

        clearVisual = myFont.render(f'Press C to Clear Drawing', True, self.BLACK)
        screen.blit(clearVisual, (930,20))

        clearVisual = myFont.render(f'Press S to Save Drawing', True, self.BLACK)
        screen.blit(clearVisual, (930,60))

  
        if(((math.sqrt(((centerX - 50)**2) + (centerZ - 50)**2))) <= 40):
            self.drawingColor = self.BLACK
        if(((math.sqrt(((centerX - 150)**2) + (centerZ - 50)**2))) <= 40):
            self.drawingColor = self.RED
        if(((math.sqrt(((centerX - 250)**2) + (centerZ - 50)**2))) <= 40):
            self.drawingColor = self.ORANGE
        if(((math.sqrt(((centerX - 350)**2) + (centerZ - 50)**2))) <= 40):
            self.drawingColor = self.GREEN
        if(((math.sqrt(((centerX - 450)**2) + (centerZ - 50)**2))) <= 40):
            self.drawingColor = self.GREY
        if(((math.sqrt(((centerX - 550)**2) + (centerZ - 50)**2))) <= 40):
            self.drawingColor = self.BROWN
        if(((math.sqrt(((centerX - 650)**2) + (centerZ - 50)**2))) <= 40):
            self.drawingColor = self.YELLOW
        if(((math.sqrt(((centerX - 750)**2) + (centerZ - 50)**2))) <= 40):
            self.drawingColor = self.CYAN
        if(((math.sqrt(((centerX - 850)**2) + (centerZ - 50)**2))) <= 40):
            self.drawingColor = self.WHITE
            
        # for event in pygame.event.get():
    # def keyCommands():
        
    

     #Not sure what this does but crashes without it
    def getTextObjects(self, text, font):
        textSurface = font.render(text, True, (255,255,255))
        return textSurface, textSurface.get_rect()

      
        


#Changes the screen content and updates the display
def guiDisplay(coords):
    guiSupport.drawGraphics(coords, screen, (800, 800))
    pygame.display.update()


#Initializes the socket connection with the hand sensor file and starts the main loop
def connectToSocket():
    global s
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((socket.gethostname(), 1243))
    main()


#Receives coordinates from web socket connection and passes them to the  and GUI portions of the code
def main():
    
    try:
        while True:
            
            #Receive 1024 bits of websocket information (Is enough for our purposes)
            full_msg = ''
            msg = s.recv(1024)

            #Full message recieves a decoded string of the server data
            full_msg = msg.decode("utf-8")
            print(full_msg)

            #This is meant to clear the buffer until only one array is left if the buffer is filled too fast
            while(len(full_msg) > 40):

                #Re-receives 1024 bits of websocket information in order to clear the buffer 1024 bits at a time
                full_msg = ''
                msg = s.recv(1024)
                full_msg = msg.decode("utf-8")
                print(full_msg)
            

            #Turns the string array into an actual array of integers
            coordinateArr = literal_eval(full_msg)
            print(coordinateArr)
            #Passes the GUI an array of the hand coordinates
            guiDisplay(coordinateArr)
            
            #Testing
            # guiDisplay((0,450,0))

            #Function that takes coordinates and outputs  commands to the connected 
            # keyCommands()



    except Exception as inst:
        print(type(inst)) 
        print(inst) 
        print("Connection closed")
       


#Initial function that runs 
if __name__ == "__main__":
    #Gets current working directory to pass to the GUI
    path = os.getcwd()


    #Initializes the pygame GUI window
    guiSupport = GUI_Support()

    #Initializes window to  (1.50 multiplier)
    xWidth = 1200   
    yHeight = 900
    screen = guiSupport.initDisplay((xWidth, yHeight))
    background=pygame.Surface(screen.get_size())
    background=background.convert()
    background.fill((255,255,255))

    #Initializing font for coordinate display
    pygame.font.init()
    myFont = pygame.font.SysFont('Arial', 22)
    
    

    # icon
    icon = pygame.image.load(path + '\icon.png')
    icon = pygame.transform.scale(icon, (32, 32))
    pygame.display.set_icon(icon)
    pygame.display.set_caption('VR Paint')

    #Connect to socket
    #main()
    connectToSocket()