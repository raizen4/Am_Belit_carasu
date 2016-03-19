from tkinter.ttk import *
from tkinter import *

import sys, time, random

class Window:

    def __init__(self, parent):
        self.parent = parent

        self.parent.title("Binary dash")
        self.parent.configure(background="#666666")
        self.parent.geometry("449x945")
        self.parent.resizable(0,0)
        #-- Moving Row --#
        self.rect_list_1 = [0,0,90,90]
        self.rect_list_2 = [90,0,180,90]
        self.rect_list_3 = [180,0,270,90]
        self.rect_list_4 = [270,0,360,90]
        self.rect_list_5 = [360,0,450,90]
        self.rect_list_6 = [-90,0,0,90]
        #--          --#
        self.space_flag = 0

        self.rr = 0

        self.bot_rect_list1 = [4,-102,445,-1]

        self.bot_rect_list2_1 = [4, -102, 225, -1]
        self.bot_rect_list2_2 = [225,-102,445,-1]

        self.bot_rect_list3_1 = [4,-102,147,-1]
        self.bot_rect_list3_2 = [147,-102,294,-1]
        self.bot_rect_list3_3 = [294,-102,445,-1]

        self.bot_rect_list4_1 = [4,-102,110,-1]
        self.bot_rect_list4_2 = [110,-102,220,-1]
        self.bot_rect_list4_3 = [220,-102,330,-1]
        self.bot_rect_list4_4 = [330,-102,445,-1]

        self.on_screen = {1:0, 2:0, 3:0, 4:0}

        #-- Widgets --#
        
        self.upper_frame = Frame(self.parent, background="#666666", relief="ridge", highlightthickness=0, bd=0)
        self.upper_frame.pack(fill=BOTH, side=TOP)

        self.top_canvas = Canvas(self.upper_frame, width=449, height = 100, background="#666666")
        self.top_canvas.pack()

        self.on_screen_dict = {1:0, 2:0, 3:0, 4:0}

        # Tot moving row e dedesubt 

        self.rect1 = self.top_canvas.create_rectangle(0,0,90,90,fill='red')
        self.rect2 = self.top_canvas.create_rectangle(90,0,180,90,fill='gray')
        self.rect3 = self.top_canvas.create_rectangle(180,0,270,90,fill='gray')
        self.rect4 = self.top_canvas.create_rectangle(270,0,360,90,fill='red')
        self.rect5 = self.top_canvas.create_rectangle(360,0,450,90,fill='gray')
        self.rect6 = self.top_canvas.create_rectangle(-90,0,0,90,fill='red')

        self.color_list=['r','g','g','r','g','r']

        self.current_color_list1 = [] ########
        self.color_check_list = []

        self.rect_list = [self.rect1,self.rect2,self.rect3,self.rect4,self.rect5,self.rect6]
        
        self.top_canvas.create_polygon((225, 80, 215, 100, 235, 100), fill="black")
        self.top_canvas.create_polygon((225, 20, 215, 0, 235, 0), fill = "black")
        self.top_canvas.config(highlightthickness=0)

        self.bot_frame = Frame(self.parent)
        self.bot_frame.pack()
        
        self.bot_canvas = Canvas(self.bot_frame, width=449, height=845, background="#666666")
        self.bot_canvas.pack(side=BOTTOM)

##        self.draw_single()
##        self.draw_double()
##        self.draw_triple()
##        self.draw_quadra()

        self.counter2 = 0

##        self.bot_rect1 = self.bot_canvas.create_rectangle(4,-102,445,-1,fill = self.random_colour())
##
##        self.bot_rect2_1 = self.bot_canvas.create_rectangle(4,-102,225,-1,fill = self.random_colour())
##        self.bot_rect2_2 = self.bot_canvas.create_rectangle(225,-102,445,-1,fill = self.random_colour())
##            
##        self.bot_rect3_1 = self.bot_canvas.create_rectangle(4,-102,147,-1,fill=self.random_colour())
##        self.bot_rect3_2 = self.bot_canvas.create_rectangle(147,-102,294,-1,fill=self.random_colour())
##        self.bot_rect3_3 = self.bot_canvas.create_rectangle(294,-102,445,-1,fill=self.random_colour()) 
##            
##        self.bot_rect4_1 = self.bot_canvas.create_rectangle(4,-102,110,-1,fill=self.random_colour())
##        self.bot_rect4_2 = self.bot_canvas.create_rectangle(110,-102,220,-1,fill=self.random_colour())
##        self.bot_rect4_3 = self.bot_canvas.create_rectangle(220,-102,330,-1,fill=self.random_colour())
##        self.bot_rect4_4 = self.bot_canvas.create_rectangle(330,-102,445,-1,fill=self.random_colour())

##        self.main_rect = self.bot_canvas.create_rectangle(4,740,445,840)
        
        self.bot_canvas.config(highlightthickness=0)

        self.parent.bind("<space>",lambda event: self.edit_rectangle(0))

    def draw_single(self):
        self.bot_rect1 = self.bot_canvas.create_rectangle(4,-102,445,-1,fill = self.random_colour())
        self.acc1 = 1
    def draw_double(self):
        self.bot_rect2_1 = self.bot_canvas.create_rectangle(4,-102,225,-1,fill = self.random_colour())
        self.bot_rect2_2 = self.bot_canvas.create_rectangle(225,-102,445,-1,fill = self.random_colour())
        self.acc2 = 2
    def draw_triple(self):
        self.bot_rect3_1 = self.bot_canvas.create_rectangle(4,-102,147,-1,fill=self.random_colour())
        self.bot_rect3_2 = self.bot_canvas.create_rectangle(147,-102,294,-1,fill=self.random_colour())
        self.bot_rect3_3 = self.bot_canvas.create_rectangle(294,-102,445,-1,fill=self.random_colour())
        self.acc3 = 3
    def draw_quadra(self):
        self.bot_rect4_1 = self.bot_canvas.create_rectangle(4,-102,110,-1,fill=self.random_colour())
        self.bot_rect4_2 = self.bot_canvas.create_rectangle(110,-102,220,-1,fill=self.random_colour())
        self.bot_rect4_3 = self.bot_canvas.create_rectangle(220,-102,330,-1,fill=self.random_colour())
        self.bot_rect4_4 = self.bot_canvas.create_rectangle(330,-102,445,-1,fill=self.random_colour())
        self.acc4 = 4
        
    def random_colour(self):
        self.ran = random.randint(1,2)
        if self.ran == 1:
            self.current_color_list1.append('red')
            return 'red'
        else:
            self.current_color_list1.append('gray')
            return 'gray'
            

        
        
    def edit_main(self, n):
        self.n = n
        if n == 0:
            self.main_rect = self.bot_canvas.create_rectangle(4,740,445,840)
            self.acc1 = 1
        elif n==1:
            self.main_rect2_1 = self.bot_canvas.create_rectangle(4,740,225,840)
            self.main_rect2_2 = self.bot_canvas.create_rectangle(225,740,445,840)

        elif n==2:
            self.main_rect3_1 = self.bot_canvas.create_rectangle(4,740,147,840)
            self.main_rect3_2 = self.bot_canvas.create_rectangle(147,740,294,840)
            self.main_rect3_3 = self.bot_canvas.create_rectangle(294,740,445,840) 
        elif n==3:
            self.main_rect4_1 = self.bot_canvas.create_rectangle(4,740,110,840)
            self.main_rect4_2 = self.bot_canvas.create_rectangle(110,740,220,840)
            self.main_rect4_3 = self.bot_canvas.create_rectangle(220,740,330,840)
            self.main_rect4_4 = self.bot_canvas.create_rectangle(330,740,445,840)
            
            
        self.bot_canvas.update()

    def edit_rectangle(self, x):
        
        if self.space_flag == 0:
            self.space_flag = 1
            self.parent.bind("<space>",lambda event: self.selected_color())

            self.order =[0,0,0,0]
            self.max_val = 0
        
        while x < 99999 :
            for i in range(0,4):
                if self.order[i] == 1: # daca gasesti primul element vrei sa redimensionezi mainul
                    self.edit_main(i)
            if self.rr == 1:
                self.acc1 = 1
                self.acc2 = 2
                self.acc3 = 3
                self.acc4 = 4
                self.rr = 0
            if x % 50 == 0 :
                self.cristi = random.randint(1,4)
                if self.on_screen[self.cristi] == 1:
                    while self.on_screen[self.cristi]== 1:
                        self.cristi = random.randint(1,4)
                        
                if self.cristi == 1:
                    self.draw_single()
                elif self.cristi == 2:
                    self.draw_double()
                elif self.cristi == 3:
                    self.draw_triple()
                elif self.cristi == 4:
                    self.draw_quadra()
                    
                self.on_screen[self.cristi] = 1
                    
            self.speed = 3 #horizontal
            self.speed2 = 5 #vertical
            self.counter = 0
            if self.on_screen[1] == 1:
                
                    
                
                self.bot_rect_list1[1]+=self.speed2
                self.bot_rect_list1[3]+=self.speed2

                self.bot_canvas.coords(self.bot_rect1, (self.bot_rect_list1[0],self.bot_rect_list1[1],
                                                   self.bot_rect_list1[2],self.bot_rect_list1[3]))
                if self.order[0] == 0:
                    for i in range(0,4):
                        if self.order[i]!=0 and self.max_val < self.order[i]:
                            self.max_val = self.order[i]
                    if self.max_val == 0:
                        self.order[0] = 1
                    else:
                        self.order[0] = self.max_val + 1

            if self.on_screen[2] == 1:
                self.first = 2
                
                self.bot_rect_list2_1[1]+=self.speed2
                self.bot_rect_list2_1[3]+=self.speed2

                self.bot_rect_list2_2[1]+=self.speed2
                self.bot_rect_list2_2[3]+=self.speed2

                self.bot_canvas.coords(self.bot_rect2_1, (self.bot_rect_list2_1[0],self.bot_rect_list2_1[1],
                                                   self.bot_rect_list2_1[2],self.bot_rect_list2_1[3]))
                self.bot_canvas.coords(self.bot_rect2_2, (self.bot_rect_list2_2[0],self.bot_rect_list2_2[1],
                                                      self.bot_rect_list2_2[2],self.bot_rect_list2_2[3]))
                if self.order[1] == 0:
                    for i in range(0,4):
                        if self.order[i]!=0 and self.max_val < self.order[i]:
                            self.max_val = self.order[i]
                    if self.max_val == 0:
                        self.order[1] = 1
                    else:
                        self.order[1] = self.max_val + 1

            if self.on_screen[3] == 1:
                self.first = 3

                self.bot_rect_list3_1[1]+=self.speed2
                self.bot_rect_list3_1[3]+=self.speed2

                self.bot_rect_list3_2[1]+=self.speed2
                self.bot_rect_list3_2[3]+=self.speed2

                self.bot_rect_list3_3[1]+=self.speed2
                self.bot_rect_list3_3[3]+=self.speed2

                self.bot_canvas.coords(self.bot_rect3_1, (self.bot_rect_list3_1[0],self.bot_rect_list3_1[1],
                                                   self.bot_rect_list3_1[2],self.bot_rect_list3_1[3]))
                self.bot_canvas.coords(self.bot_rect3_2, (self.bot_rect_list3_2[0],self.bot_rect_list3_2[1],
                                                      self.bot_rect_list3_2[2],self.bot_rect_list3_2[3]))
                self.bot_canvas.coords(self.bot_rect3_3, (self.bot_rect_list3_3[0],self.bot_rect_list3_3[1],
                                                      self.bot_rect_list3_3[2],self.bot_rect_list3_3[3]))
                if self.order[2]==0:
                    for i in range(0,4):
                        if self.order[i]!=0 and self.max_val < self.order[i]:
                            self.max_val = self.order[i]
                    if self.max_val == 0:
                        self.order[2] = 1
                    else:
                        self.order[2] = self.max_val + 1

            if self.on_screen[4] == 1:
                self.first = 4

                self.bot_rect_list4_1[1]+=self.speed2
                self.bot_rect_list4_1[3]+=self.speed2

                self.bot_rect_list4_2[1]+=self.speed2
                self.bot_rect_list4_2[3]+=self.speed2

                self.bot_rect_list4_3[1]+=self.speed2
                self.bot_rect_list4_3[3]+=self.speed2

                self.bot_rect_list4_4[1]+=self.speed2
                self.bot_rect_list4_4[3]+=self.speed2

                self.bot_canvas.coords(self.bot_rect4_1, (self.bot_rect_list4_1[0],self.bot_rect_list4_1[1],
                                                   self.bot_rect_list4_1[2],self.bot_rect_list4_1[3]))
                self.bot_canvas.coords(self.bot_rect4_2, (self.bot_rect_list4_2[0],self.bot_rect_list4_2[1],
                                                      self.bot_rect_list4_2[2],self.bot_rect_list4_2[3]))
                self.bot_canvas.coords(self.bot_rect4_3, (self.bot_rect_list4_3[0],self.bot_rect_list4_3[1],
                                                      self.bot_rect_list4_3[2],self.bot_rect_list4_3[3]))
                self.bot_canvas.coords(self.bot_rect4_4, (self.bot_rect_list4_4[0],self.bot_rect_list4_4[1],
                                                      self.bot_rect_list4_4[2],self.bot_rect_list4_4[3]))
                if self.order[3] == 0:
                    for i in range(0,4):
                        if self.order[i]!=0 and self.max_val < self.order[i]:
                            self.max_val = self.order[i]
                    if self.max_val == 0:
                        self.order[3] = 1
                    else:
                        self.order[3] = self.max_val + 1

            
##################################################################################
            self.rect_list_1[0]+=10
            self.rect_list_1[2]+=10

            self.rect_list_2[0]+=10
            self.rect_list_2[2]+=10

            self.rect_list_3[0]+=10
            self.rect_list_3[2]+=10

            self.rect_list_4[0]+=10
            self.rect_list_4[2]+=10

            self.rect_list_5[0]+=10
            self.rect_list_5[2]+=10

            self.rect_list_6[0]+=10
            self.rect_list_6[2]+=10
            
            
            ######################################################################################

            self.top_canvas.coords(self.rect_list[0], (self.rect_list_1[0],self.rect_list_1[1],
                                               self.rect_list_1[2],self.rect_list_1[3]))
            self.top_canvas.coords(self.rect_list[1], (self.rect_list_2[0],self.rect_list_2[1],
                                               self.rect_list_2[2],self.rect_list_2[3]))
            self.top_canvas.coords(self.rect_list[2], (self.rect_list_3[0],self.rect_list_3[1],
                                               self.rect_list_3[2],self.rect_list_3[3]))
            self.top_canvas.coords(self.rect_list[3], (self.rect_list_4[0],self.rect_list_4[1],
                                               self.rect_list_4[2],self.rect_list_4[3]))
            self.top_canvas.coords(self.rect_list[4], (self.rect_list_5[0],self.rect_list_5[1],
                                               self.rect_list_5[2],self.rect_list_5[3]))
            self.top_canvas.coords(self.rect_list[5], (self.rect_list_6[0],self.rect_list_6[1],
                                               self.rect_list_6[2],self.rect_list_6[3]))
            #####################################################################################

            #-- Bot widget --#
            ''' AICI COAIEEEEEEEE '''
            if self.bot_rect_list1[3] >= 740 or self.bot_rect_list2_1[3] >= 740 or self.bot_rect_list3_1[3] >= 740 or self.bot_rect_list4_1[3] >740:
                self.lose() 
            x+=1

            self.n2 = self.rect_list[5]
            #print(x)
            
            if x%9 == 0:
                self.rect_list_1[0]-=90
                self.rect_list_1[2]-=90

                self.rect_list_2[0]-=90
                self.rect_list_2[2]-=90

                self.rect_list_3[0]-=90
                self.rect_list_3[2]-=90

                self.rect_list_4[0]-=90
                self.rect_list_4[2]-=90

                self.rect_list_5[0]-=90
                self.rect_list_5[2]-=90

                self.rect_list_6[0]-=90
                self.rect_list_6[2]-=90

                i = 5
                while(i>=0):
                    if i == 0:
                        self.rect_list[i] = self.n2
                    else:
                        self.rect_list[i] = self.rect_list[i-1]
                    i-=1

                randomizer = random.randint(0,1)
                if randomizer == 1:
                    self.top_canvas.itemconfig(self.rect_list[5], fill = 'red')
                    j=5
                    while(j>=0):
                        if j==0:
                            self.color_list[j] = 'r'
                        else:
                            self.color_list[j] = self.color_list[j-1]
                        j-=1
                    
                else:
                    self.top_canvas.itemconfig(self.rect_list[5], fill = 'grey')
                    j=5
                    while(j>=0):
                        if j==0:
                            self.color_list[j] = 'g'
                        else:
                            self.color_list[j] = self.color_list[j-1]
                        j-=1
                    

            self.top_canvas.update()
            time.sleep(0.03)

    def lose(self):
        print('lost')
        #self.bot_canvas.create_rectangle(0,0,700,700,fill='black')
        #self.close()
        
    def selected_color(self):
        
        if self.n == 0:
        
            if self.rect_list_2[0] <= 225 and self.rect_list_2[2] >= 225:
                if self.color_list[2] == 'r':
                    self.bot_canvas.itemconfig(self.main_rect, fill='red')
                    self.color_check_list.append('red')
                else:
                    self.bot_canvas.itemconfig(self.main_rect, fill='gray')
                    self.color_check_list.append('gray')

            elif self.rect_list_3[0] <= 225 and self.rect_list_3[2] >= 225:
                if self.color_list[3] == 'r':
                    self.bot_canvas.itemconfig(self.main_rect, fill='red')
                    self.color_check_list.append('red')
                else:
                    self.bot_canvas.itemconfig(self.main_rect, fill='gray')
                    self.color_check_list.append('gray')

        elif self.n == 1:

            if self.counter2 == 0:
                if self.rect_list_2[0] <= 225 and self.rect_list_2[2] >= 225:
                    if self.color_list[2] == 'r':
                        self.bot_canvas.itemconfig(self.main_rect2_1, fill='red')
                        self.color_check_list.append('red')
                    else:
                        self.bot_canvas.itemconfig(self.main_rect2_1, fill='gray')
                        self.color_check_list.append('gray')

                elif self.rect_list_3[0] <= 225 and self.rect_list_3[2] >= 225:
                    if self.color_list[3] == 'r':
                        self.bot_canvas.itemconfig(self.main_rect2_1, fill='red')
                        self.color_check_list.append('red')
                    else:
                        self.bot_canvas.itemconfig(self.main_rect2_1, fill='gray')
                        self.color_check_list.append('gray')

            elif self.counter2 == 1:
                if self.rect_list_2[0] <= 225 and self.rect_list_2[2] >= 225:
                    if self.color_list[2] == 'r':
                        self.bot_canvas.itemconfig(self.main_rect2_2, fill='red')
                        self.color_check_list.append('red')
                    else:
                        self.bot_canvas.itemconfig(self.main_rect2_2, fill='gray')
                        self.color_check_list.append('gray')

                elif self.rect_list_3[0] <= 225 and self.rect_list_3[2] >= 225:
                    if self.color_list[3] == 'r':
                        self.bot_canvas.itemconfig(self.main_rect2_2, fill='red')
                        self.color_check_list.append('red')
                    else:
                        self.bot_canvas.itemconfig(self.main_rect2_2, fill='gray')
                        self.color_check_list.append('gray')
            if self.counter2 == 2:
                self.counter2 = 0
        

        elif self.n == 2:

            if self.counter2 == 0:
                if self.rect_list_2[0] <= 225 and self.rect_list_2[2] >= 225:
                    if self.color_list[2] == 'r':
                        self.bot_canvas.itemconfig(self.main_rect3_1, fill='red')
                        self.color_check_list.append('red')
                    else:
                        self.bot_canvas.itemconfig(self.main_rect3_1, fill='gray')
                        self.color_check_list.append('gray')

                elif self.rect_list_3[0] <= 225 and self.rect_list_3[2] >= 225:
                    if self.color_list[3] == 'r':
                        self.bot_canvas.itemconfig(self.main_rect3_1, fill='red')
                        self.color_check_list.append('red')
                    else:
                        self.bot_canvas.itemconfig(self.main_rect3_1, fill='gray')
                        self.color_check_list.append('gray')

            elif self.counter2 == 1:
                if self.rect_list_2[0] <= 225 and self.rect_list_2[2] >= 225:
                    if self.color_list[2] == 'r':
                        self.bot_canvas.itemconfig(self.main_rect3_2, fill='red')
                        self.color_check_list.append('red')
                    else:
                        self.bot_canvas.itemconfig(self.main_rect3_2, fill='gray')
                        self.color_check_list.append('gray')

                elif self.rect_list_3[0] <= 225 and self.rect_list_3[2] >= 225:
                    if self.color_list[3] == 'r':
                        self.bot_canvas.itemconfig(self.main_rect3_2, fill='red')
                        self.color_check_list.append('red')
                    else:
                        self.bot_canvas.itemconfig(self.main_rect3_2, fill='gray')
                        self.color_check_list.append('gray')

            elif self.counter2 == 2:
                if self.rect_list_2[0] <= 225 and self.rect_list_2[2] >= 225:
                    if self.color_list[2] == 'r':
                        self.bot_canvas.itemconfig(self.main_rect3_3, fill='red')
                        self.color_check_list.append('red')
                    else:
                        self.bot_canvas.itemconfig(self.main_rect3_3, fill='gray')
                        self.color_check_list.append('gray')

                elif self.rect_list_3[0] <= 225 and self.rect_list_3[2] >= 225:
                    if self.color_list[3] == 'r':
                        self.bot_canvas.itemconfig(self.main_rect3_3, fill='red')
                        self.color_check_list.append('red')
                    else:
                        self.bot_canvas.itemconfig(self.main_rect3_3, fill='gray')
                        self.color_check_list.append('gray')
            if self.counter2 == 3:
                self.counter2 = 0

        elif self.n == 3:
            if self.counter2 == 0:
                if self.rect_list_2[0] <= 225 and self.rect_list_2[2] >= 225:
                    if self.color_list[2] == 'r':
                        self.bot_canvas.itemconfig(self.main_rect4_1, fill='red')
                        self.color_check_list.append('red')
                    else:
                        self.bot_canvas.itemconfig(self.main_rect4_1, fill='gray')
                        self.color_check_list.append('gray')

                elif self.rect_list_3[0] <= 225 and self.rect_list_3[2] >= 225:
                    if self.color_list[3] == 'r':
                        self.bot_canvas.itemconfig(self.main_rect4_1, fill='red')
                        self.color_check_list.append('red')
                    else:
                        self.bot_canvas.itemconfig(self.main_rect4_1, fill='gray')
                        self.color_check_list.append('gray')

            elif self.counter2 == 1:
                if self.rect_list_2[0] <= 225 and self.rect_list_2[2] >= 225:
                    if self.color_list[2] == 'r':
                        self.bot_canvas.itemconfig(self.main_rect4_2, fill='red')
                        self.color_check_list.append('red')
                    else:
                        self.bot_canvas.itemconfig(self.main_rect4_2, fill='gray')
                        self.color_check_list.append('gray')

                elif self.rect_list_3[0] <= 225 and self.rect_list_3[2] >= 225:
                    if self.color_list[3] == 'r':
                        self.bot_canvas.itemconfig(self.main_rect4_2, fill='red')
                        self.color_check_list.append('red')
                    else:
                        self.bot_canvas.itemconfig(self.main_rect4_2, fill='gray')
                        self.color_check_list.append('gray')

            elif self.counter2 == 2:
                if self.rect_list_2[0] <= 225 and self.rect_list_2[2] >= 225:
                    if self.color_list[2] == 'r':
                        self.bot_canvas.itemconfig(self.main_rect4_3, fill='red')
                        self.color_check_list.append('red')
                    else:
                        self.bot_canvas.itemconfig(self.main_rect4_3, fill='gray')
                        self.color_check_list.append('gray')

                elif self.rect_list_3[0] <= 225 and self.rect_list_3[2] >= 225:
                    if self.color_list[3] == 'r':
                        self.bot_canvas.itemconfig(self.main_rect4_3, fill='red')
                        self.color_check_list.append('red')
                    else:
                        self.bot_canvas.itemconfig(self.main_rect4_3, fill='gray')
                        self.color_check_list.append('gray')

            elif self.counter2 == 3:
                if self.rect_list_2[0] <= 225 and self.rect_list_2[2] >= 225:
                    if self.color_list[2] == 'r':
                        self.bot_canvas.itemconfig(self.main_rect4_4, fill='red')
                        self.color_check_list.append('red')
                    else:
                        self.bot_canvas.itemconfig(self.main_rect4_4, fill='gray')
                        self.color_check_list.append('gray')

                elif self.rect_list_3[0] <= 225 and self.rect_list_3[2] >= 225:
                    if self.color_list[3] == 'r':
                        self.bot_canvas.itemconfig(self.main_rect4_4, fill='red')
                        self.color_check_list.append('red')
                    else:
                        self.bot_canvas.itemconfig(self.main_rect4_4, fill='gray')
                        self.color_check_list.append('gray')
            if self.counter2 == 4:
                self.counter2 = 0

        if self.color_check_list[len(self.color_check_list)-1]!=self.current_color_list1[len(self.color_check_list)-1]:
            pass
        else:
            if self.order[0] == 1:
                self.acc1 = self.acc1 - 1
                print(self.acc1)
                if self.acc1 == 0:
                    self.bot_canvas.delete(self.bot_rect1)
                    self.bot_canvas.delete(self.main_rect)
                    self.rr += 1
            elif self.order[1] == 1:
                self.acc2 = self.acc2 - 1
                print(self.acc2)
                if self.acc2 ==0:
                    self.bot_canvas.delete(self.bot_rect2_1)
                    self.bot_canvas.delete(self.bot_rect2_2)
                    self.bot_canvas.delete(self.main_rect2_1)
                    self.bot_canvas.delete(self.main_rect2_2)
                    self.rr += 1
            elif self.order[2] == 1:
                self.acc3 = self.acc3 - 1
                print(self.acc3)
                if self.acc3 == 0:
                    self.bot_canvas.delete(self.bot_rect3_1)
                    self.bot_canvas.delete(self.bot_rect3_2)
                    self.bot_canvas.delete(self.bot_rect3_3)
                    self.bot_canvas.delete(self.main_rect3_1)
                    self.bot_canvas.delete(self.main_rect3_2)
                    self.bot_canvas.delete(self.main_rect3_3)
                    sself.rr += 1 
            elif self.order[3] == 1:
                self.acc4 = self.acc4 - 1
                print(self.acc4)
                if self.acc4 == 0:
                    self.bot_canvas.delete(self.bot_rect4_1)
                    self.bot_canvas.delete(self.bot_rect4_2)
                    self.bot_canvas.delete(self.bot_rect4_3)
                    self.bot_canvas.delete(self.bot_rect4_4)
                    self.bot_canvas.delete(self.main_rect4_1)
                    self.bot_canvas.delete(self.main_rect4_2)
                    self.bot_canvas.delete(self.main_rect4_3)
                    self.bot_canvas.delete(self.main_rect4_4)
                    self.rr += 1
        self.bot_canvas.update()
        self.counter2 += 1
            
    def close(self):
        sys.exit()
        
