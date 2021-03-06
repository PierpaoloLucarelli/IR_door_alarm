''' 
Author : Pierpaolo Lucarelli 
MonitorFSM class taht extends the FSM class.
this class ir sesponsible for handling the I/O of the machine
Give a certain type of input and the correct type of output will be send
'''
from FSM import *

class MonitorFSM(FSM):

    startState = 'deactivated'
    codeState = 0 #state of the code [0,1,2,3,accepted]
   
    def getNextValues(self, state, inp):
        if state == 'deactivated' or state == "deactivated-trans":
            if inp == "Up" or inp == "Down" or inp == "Left" or inp == "Right":
                self.check_code(inp) 
                # print("Code state: %s" % self.codeState)
                if self.codeState == 0:
                    return ("deactivated", "cross")
                elif self.codeState in (1,2,3): 
                    return ("deactivated-trans", "right_arrow")
                elif self.codeState == "accepted": 
                    self.codeState = 0    #when code is correct reset the code state to zero and ouput red circle 
                    return ("deactivated-in-trans", "empty_circle_red")
            elif inp != "IRSens":  #for any input other than Sensor input and dirKeys
                print("unacepted input")
                self.codeState = 0
                return("deactivated", "cross") #machine state back to start (deactivated)
                

        #from here machine is in activated sate
        elif state == "activated" or state == "activated-trans":
            if inp == "IRSens":
                return ("activated", "alarmed") #alarm is alarmed when IR signal is recieved

            if inp == "Up" or inp == "Down" or inp == "Left" or inp == "Right":
                self.check_code(inp) 
                # print("Code state: %s" % self.codeState)
                if self.codeState == 0:
                    return ("activated", "full_circle_green") #if code is incorrect return to activated state
                elif self.codeState in (1,2,3):
                    return ("activated-trans", "left_arrow")
                elif self.codeState == "accepted":
                    self.codeState = 0     #reset code check to zero for next code check
                    return ("deactivated", "cross")

            elif inp != "IRSens" : #for any input other that IRsens and dirKeys 
                self.codeState = 0
                return ("activated", "full_circle_green") #return to activated state


    #this function gets called when a key is entered, check if the sequience of theese key is Up, Down, Left, Right
    def check_code(self,inp):
        if self.codeState == 0:
            if inp == "Up":
                self.codeState = 1
            else:
                self.codeState = 0
        elif self.codeState == 1:
            if inp == "Down":
                self.codeState = 2
            else:
                self.codeState = 0
        elif self.codeState == 2:
            if inp == "Left":
                self.codeState = 3
            else:
                self.codeState = 0
        elif self.codeState == 3:
            if inp == "Right":
                self.codeState = "accepted" #change state of codeState to accepted when sequence is correct
            else:
                self.codeState = 0
        else:
            print ("Something went wrong in the code (test only)")



               

    
