# Add your Python code here. E.g.
from microbit import *

speed = 300
morse={'a':"01",'b':"1000",'c':"1010",'d':"100",'e':"0",'f':"0010",'g':"110",'h':"0000",'i':"00",'j':"0111",'k':"101",'l':"0100",'m':"11",'n':"10",'o':"111",'p':"0110",'q':"1101",'r':"010",'s':"000",'t':"1",'u':"001",'v':"0001",'w':"011",'x':"1001",'y':"1011",'z':"1100"}

def displayCode(phrase):
    message=[]
    if stringHasSpace(phrase):
        message=phrase.split(" ")
    else:
        message.append(phrase)
    for word in phrase:
        for letter in word:
            y = str(morse[letter])   
            sleep(speed*3) #delay between char
        
            for x in y:    
                display.clear()
                if x == "0":
                    display.set_pixel(2,2,9)
                    pin0.write_digital(1)
                    sleep(speed) #one di length
                    pin0.write_digital(0)
                    display.clear()
                    sleep(speed*2) #delay betwen elements (farnsworth timing)
          
                elif x == "1":
                    display.set_pixel(1,2,9)
                    display.set_pixel(2,2,9)
                    display.set_pixel(3,2,9)
                    pin0.write_digital(1)
                    sleep(speed*3) #one dah length
                    pin0.write_digital(0)
                    display.clear()
                    sleep(speed*2) #delay betwen elements (farnsworth timing)
        
        sleep(speed*7) #delay between words

def stringHasSpace(string):
    if ' ' in string: 
       return True 
    else: 
       return False
    
display.show(Image.HEART)
sleep(300)
display.clear()

while True:
    
    displayCode("sos sos")
