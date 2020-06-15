import pyautogui
from PIL import Image , ImageGrab
import time
##from numpy import asarray


def hit(key):
    pyautogui.keyDown(key)
    return

def isCollide(data):

    for i in range(300,415):
        #code for the bird
        for j in range(410,563):
            if  data[i, j] < 100:
                hit("down")
                return 

    for i in range(300,415):
        for j in range(563,650):
            if  data[i, j] < 100:  
                hit("up")  #zero means we are making the above rectangular co ordinates black
                return 
    return 


    

if __name__ == "__main__" :

    print('Hey! dino game is about to start in 2 seconds')

    time.sleep(2)
    ## hit('up')


    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        isCollide(data)



      
        '''
       
    #for cactus   
    for i in range(300,415):
        for j in range(610,650):
              data[i,j] = 0

    # for bird coming above
    for i in range(300,415):
        for j in range(410,610):
              data[i,j] = 71

        '''