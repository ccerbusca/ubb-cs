from circle import Circle
from tools import GameException,isInt,circle
from game import Game
from tkinter import *
from tkinter import messagebox
class GUI:
    def _init_(self):
        self.__game=Game()
        self.master=Tk()
        self.dict={}
        self.board=self.__game.board
        self._data=[[0]*7,[0]*7,[0]*7,[0]*7,[0]*7,[0]*7]
        #self.initi()   ##columnspans
        self.initia()
        self.playerTurn=True
        self.win=-1
        self.winLabelText=StringVar()
        self.winLabelText.set('Good Luck !')
        self.winLabel=Label(self.master,textvariable=self.winLabelText,font=('Helvetica',16))
        #self.winLabel.text='goodluck'
        self.winLabel.grid(row=2,columnspan=7)
    def show_error(self):
        messagebox.showwarning('Error',"Can't place it on this col")
    def show_congrats(self):
        messagebox.showinfo('YAAAY',"Congrats, you win")
    def show_tie(self):
        messagebox.showinfo('Not a lose !',"Congrats, Tie")
    def show_meh(self):
        messagebox.showinfo('F*CK!',"Computer Wins! AItality!")
    def start(self):
        mainloop()
    def initia(self):
        canvas_height = 315
        canvas_width = 365
        w = Canvas(self.master,
                   width=canvas_width,
                   height=canvas_height)
        w.grid(row=1,columnspan=7)
        c=[35,85,135,185,235,285,335]
        r=[35,85,135,185,235,285]
        for i in range(0,7):
            for j in range(0,6):
                cerc=circle(w,c[i],r[j],20)
                self._data[j][i]=cerc
            self.createButton(w,i)
            self.dict[i+1]=5
    def createButton(self,w,col):
        colBtn=Button(self.master,text=str(col+1),width=5,height=2,command= lambda: self.buttonPressed(w,col+1))
        colBtn.grid(row=0,column=col)
    ########
    def initi(self):
        for j in range(0,7):
            self.makeCol(self.master,j)
            self.dict[j+1]=5
    #x=red, 0 = blue
    def getAndSetRowOnGivenCol(self,w,col):
        x=self.dict[col]
        if x<0:
            #tkMessageBox.showinfo("t",'m')
            self.show_about()
            self.playerTurn=True
        else:
            self.dict[col]=x-1
            print(x,col-1)
            w.itemconfig(self._data[x][col-1],fill='red')
            #self.__board.move(circle,'X')
            self.__game.moveHuman(Circle(-1,col-1),'X')
            self.playerTurn=False
    def getAndSetRowOnGivenColAI(self,w,col):
        x=self.dict[col]
        self.dict[col]=x-1
        print(x,col-1)
        w.itemconfig(self._data[x][col-1],fill='blue')
        self.playerTurn=True
    def makeCol(self,master,col):
        canvas_height = 315
        canvas_width = 50
        w = Canvas(master,
                   width=canvas_width,
                   height=canvas_height)
        w.grid(row=1,column=col)
        circles=[]
        for i in [35,85,135,185,235,285]:
            c=circle(w,25,i,20)
            circles.append(c)
        colBtn=Button(master,text=str(col+1),width=5,height=2,command= lambda: self.buttonPressed(w,circles,col+1))#.grid(row=0,column=col)
        colBtn.grid(row=0,column=col)
    def buttonPressed(self,w,col):
        #w.itemconfig(circles[self.getAndSetRowOnGivenCol(col)],fill="blue")
        if self.win==-1:
            while self.playerTurn:
                self.getAndSetRowOnGivenCol(w,col)
            if self.board.win():
                self.winLabelText.set('Player wins')
                self.show_congrats()
                self.win=2
            elif self.board.tie():
                self.winLabelText.set("It's a tie")
                self.show_tie()
                self.win=0
            else:
            #verificidaca e castigat
                move=self.__game.moveComputer2()
                self.getAndSetRowOnGivenColAI(w,move+1)
                if self.board.win():
                    self.winLabelText.set('Computer wins')
                    self.show_meh()
                    self.win=1
                elif self.board.tie():
                    self.winLabelText.set("It's a tie")
                    self.show_tie()
                    self.win=0
        else:
            if self.win==0:
                self.winLabelText.set("It's a tie")
            elif self.win==2:
                self.winLabelText.set('Player wins')
            else:
                self.winLabelText.set('Computer wins')
    ###