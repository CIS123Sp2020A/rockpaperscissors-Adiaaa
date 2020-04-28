#Adia Haynes - 4/16/2020 
#RockPaperScissors- Create a GUI that will simulate the game of rock, paper, scissors using radio buttons
#import tkinter etc...
import tkinter 
import tkinter.messagebox as box 
#import random
import random

#create a class for RPS,
class MyGUI:
    def __init__(self):
        #create the main window
        self.mainWindow = tkinter.Tk()
        self.mainWindow.geometry("200x100")
        

        # Create two frames. One for the Radiobuttons & another for the
        #regular Button widgets.
        self.radioFrame = tkinter.Frame(self.mainWindow)
        # self.middle_frame = tkinter.Frame(self.main_window)
        self.buttonFrame = tkinter.Frame(self.mainWindow)

        # Create an IntVar object to use with
        # the Radiobuttons.
        self.radioVar = tkinter.StringVar() #to update the labels 
        
        self.radioVars = tkinter.StringVar()# update comp selection
        
        self.resultVar = tkinter.StringVar() #update who wins and loses 
        
        ##Create radio buttons labeled "rock, papers, scissors"
        self.rb1 = tkinter.Radiobutton(self.radioFrame, text='Rock',
                                       variable=self.radioVar, value='Rock')
        self.rb2 = tkinter.Radiobutton(self.radioFrame, text='Paper',
                                       variable=self.radioVar, value='Paper')
        self.rb3 = tkinter.Radiobutton(self.radioFrame, text='Scissors',
                                       variable=self.radioVar, value='Scissors')
        #PACK the buttons
        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()

        #create play(bottom left) and quit buttons(bottom right)
        self.PlayButton = tkinter.Button(self.buttonFrame, text='Play!',
                                       command=self.displayInfo)
        self.quitButton = tkinter.Button(self.buttonFrame, text='Quit',
                                         command=self.mainWindow.destroy)

        #pack the buttons and frames 
        self.PlayButton.pack(side='left')
        self.quitButton.pack(side='left')

        self.radioFrame.pack()
        self.buttonFrame.pack()

        # Start the mainloop
        tkinter.mainloop()

         

    #have the computer make a random move out of the selections of
        #RPS (Rock- 0,Paper- 1, Scissors-2);
         #display MESSAGE BOX with player and computer selection selection
    def displayInfo(self):
        #random  numbers for computer turn 
        self.randomNum = random.randint(0,2)
        if self.randomNum == 0:
            #set variables to rock 
            self.radioVars.set('Rock')
            #set variables to paper 
        elif self.randomNum == 1:
            self.radioVars.set('Paper')
            
        else:#set variables to scissors
            self.radioVars.set('Scissors')
            
        #"Computer Selected: compchoice"
        #"You Selected: userchoice "
        #function with if/else showing winner
        #if rock beats scissors then player wins
        #if scissors cuts paper then player wins
        #if paper beats rock then player wins 
        box.showinfo('Selection',('Computer selected: ' + self.radioVars.get(),
                                  'You selected: ' + self.radioVar.get()))
        
        if ((self.radioVars.get() == 'Rock') and (self.radioVar.get() == 'Scissors')):
            
            self.resultVar.set('Rock crushes Scissors: You Lose :(')
            
        elif ((self.radioVars.get() == 'Scissors') and (self.radioVar.get() == 'Rock')):
            
            self.resultVar.set('Rock crushes Scissors: You Win! :)')
            
        elif ((self.radioVars.get() == 'Paper') and (self.radioVar.get() == 'Rock')):
            
            self.resultVar.set('Paper covers Rock: You Lose :(')
            
        elif ((self.radioVars.get() == 'Rock') and (self.radioVar.get() == 'Paper')):
            
            self.resultVar.set('Paper covers Rock: You Win! :)')
            
        elif ((self.radioVars.get() == 'Scissors') and (self.radioVar.get() == 'Paper')):
            
            self.resultVar.set('Scissors cuts Paper: You Lose :(')
            
        elif ((self.radioVars.get() == 'Paper') and (self.radioVar.get() == 'Scissors')):
            
            self.resultVar.set('Scissors cuts Paper: You Win :)')

        elif ((self.radioVars.get() == 'Scissors') and (self.radioVar.get() == 'Scissors')):
            
            self.resultVar.set('It\'s a Draw!')

        elif ((self.radioVars.get() == 'Paper') and (self.radioVar.get() == 'Paper')):
            
            self.resultVar.set('It\'s a Draw!')
            
        else:
            self.resultVar.set('It\'s a Draw!')

        box.showinfo('Winner',(self.resultVar.get()))


    #when user clicks "OK"

demoGUI = MyGUI() 
    
