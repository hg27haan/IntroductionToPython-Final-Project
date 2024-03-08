import pygame, sys, random
from pygame.locals import *
from tkinter import filedialog,ttk
import tkinter as tk_27hghan

def Load_Form_Car():
    #Chọn ảnh nền
    def selectBackGround_Game27():
        global Background_Game
        Background_Game=filedialog.askopenfilename(title='Select background', filetypes=[('Image file','*.png; *.jpg')])
        bt_Background_27.configure(background="#CCCC99")
    
    #chọn ảnh xe
    def SelectCar_27():
        global Car_27
        Car_27=filedialog.askopenfilename(title='Select Car', filetypes=[('Image file','*.png; *.jpg')])
        bt_SelectCar_27.configure(background="#CCCC99")
    
    #Chọn chướng ngại vật
    def SelectObstacle_27():
        global Obstacle_27
        Obstacle_27=filedialog.askopenfilename(title='Select background', filetypes=[('Image file','*.png; *.jpg')])
        bt_SelectObstacle_27.configure(background="#CCCC99")
        
    def Game():   
        FPS = int(spinbox_FPS_27.get()) #khuyến khích 60
        BGSPEED=float(spinbox_Vcuon_27.get()) #khuyến khích 1.5
        Road_lane=int(spinbox_Solan_27.get()) #3 làn
        
        
        HGH27_WINDOWWIDTH = 400
        HGH27_WINDOWHEIGHT = 600
        HGH27_WINDOWWIDTH_temp = EnTry_Rong.get()
        HGH27_WINDOWHEIGHT_temp = EnTry_Cao.get()
        if HGH27_WINDOWWIDTH_temp !='':
            HGH27_WINDOWWIDTH=int(HGH27_WINDOWWIDTH_temp)
        if HGH27_WINDOWHEIGHT_temp !='':
            HGH27_WINDOWHEIGHT=int(HGH27_WINDOWHEIGHT_temp)
            
        pygame.init()
    
        fpsClock = pygame.time.Clock() #Lặp theo nhịp clock (tham số FPS)

        BGIMG = pygame.image.load(Background_Game) # hình nền
        DISPLAYSURF = pygame.display.set_mode((HGH27_WINDOWWIDTH, HGH27_WINDOWHEIGHT))
        pygame.display.set_caption('27 Huỳnh Gia Hân = Ex7.5: Game = Game ĐUA XE')
        class Background():
            def __init__(self):
                self.x = 0
                self.y = 0
                self.speed = BGSPEED
                self.img = BGIMG
                self.width = self.img.get_width()
                self.height = self.img.get_height()
            def draw(self):
                DISPLAYSURF.blit(self.img, (int(self.x), int(self.y)))
                DISPLAYSURF.blit(self.img, (int(self.x), int(self.y-self.height)))
            def update(self):
                self.y += self.speed
                if self.y > self.height:
                    self.y -= self.height

        X_MARGIN = 80
        CARWIDTH = 40
        CARHEIGHT = 60
        CARSPEED = 3
        CARIMG = pygame.image.load(Car_27)
        class Car():
            def __init__(self):
                self.width = CARWIDTH
                self.height = CARHEIGHT
                self.x = (HGH27_WINDOWWIDTH-self.width)/2
                self.y = (HGH27_WINDOWHEIGHT-self.height)/2
                self.speed = CARSPEED
                self.surface = pygame.Surface((self.width, self.height))
                self.surface.fill((255, 255, 255))
            def draw(self):
                DISPLAYSURF.blit(CARIMG, (int(self.x), int(self.y)))
            def update(self, moveLeft, moveRight, moveUp, moveDown):
                if moveLeft == True:
                    self.x -= self.speed
                if moveRight == True:
                    self.x += self.speed
                if moveUp == True:
                    self.y -= self.speed
                if moveDown == True:
                    self.y += self.speed
                if self.x < X_MARGIN:
                    self.x = X_MARGIN
                if self.x + self.width > HGH27_WINDOWWIDTH - X_MARGIN:
                    self.x = HGH27_WINDOWWIDTH - X_MARGIN - self.width
                if self.y < 0:
                    self.y = 0
                if self.y + self.height > HGH27_WINDOWHEIGHT :
                    self.y = HGH27_WINDOWHEIGHT - self.height

        LANEWIDTH = 60
        DISTANCE = 200
        OBSTACLESSPEED = 2
        CHANGESPEED = 0.001
        OBSTACLESIMG = pygame.image.load(Obstacle_27)
        #Số làn xe
        Road_lane_temp=4
        if Road_lane != '':
            Road_lane_temp=Road_lane
            LANEWIDTH=(HGH27_WINDOWWIDTH-X_MARGIN*2)/(Road_lane_temp)
            
        class Obstacles():
            def __init__(self):
                self.width = CARWIDTH
                self.height = CARHEIGHT
                self.distance = DISTANCE
                self.speed = OBSTACLESSPEED
                self.changeSpeed = CHANGESPEED
                self.ls = []
                for i in range(5):
                    y = -CARHEIGHT-i*self.distance
                    lane = random.randint(0, Road_lane_temp-1)
                    self.ls.append([lane, y])
            def draw(self):
                for i in range(5):
                    x = int(X_MARGIN + self.ls[i][0]*LANEWIDTH + (LANEWIDTH-self.width)/2)
                    y = int(self.ls[i][1])
                    DISPLAYSURF.blit(OBSTACLESIMG, (x, y))
            def update(self):
                for i in range(5):
                    self.ls[i][1] += self.speed
                self.speed += self.changeSpeed
                if self.ls[0][1] > HGH27_WINDOWHEIGHT:
                    self.ls.pop(0)
                    y = self.ls[3][1] - self.distance
                    lane = random.randint(0, Road_lane_temp-1)
                    self.ls.append([lane, y])

        class Score():
            def __init__(self):
                self.score = 0
            def draw(self):
                font = pygame.font.SysFont('consolas', 30)
                scoreSuface = font.render('Score: '+str(int(self.score)), True, (0, 0, 0))
                DISPLAYSURF.blit(scoreSuface, (10, 10))
            def update(self):
                self.score += 0.02

        def rectCollision(rect1, rect2):
            if rect1[0] <= rect2[0]+rect2[2] and rect2[0] <= rect1[0]+rect1[2] and rect1[1]\
                        <= rect2[1]+rect2[3] and rect2[1] <= rect1[1]+rect1[3]:
                return True
            return False
        def isGameover(car, obstacles):
            carRect = [car.x, car.y, car.width, car.height]
            for i in range(5):
                x = int(X_MARGIN + obstacles.ls[i][0]*LANEWIDTH + (LANEWIDTH-obstacles.width)/2)
                y = int(obstacles.ls[i][1])
                obstaclesRect = [x, y, obstacles.width, obstacles.height]
                if rectCollision(carRect, obstaclesRect) == True:
                    return True
            return False

        def gameOver(bg, car, obstacles, score):
            font = pygame.font.SysFont('consolas', 60)
            headingSuface = font.render('GAMEOVER', True, (255, 0, 0))
            headingSize = headingSuface.get_size()
            font = pygame.font.SysFont('consolas', 20)
            commentSuface = font.render('Press "space" to replay', True, (0, 0, 0))
            commentSize = commentSuface.get_size()
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYUP:
                        if event.key == K_SPACE:
                            return
                bg.draw()
                car.draw()
                obstacles.draw()
                score.draw()
                DISPLAYSURF.blit(headingSuface, (int((HGH27_WINDOWWIDTH - headingSize[0])/2), 100))
                DISPLAYSURF.blit(commentSuface, (int((HGH27_WINDOWWIDTH - commentSize[0])/2), 400))
                pygame.display.update()
                fpsClock.tick(FPS)
    
        def gameStart(bg):
            bg.__init__()
            font = pygame.font.SysFont('consolas', 60)
            headingSuface = font.render('RACING', True, (255, 0, 0))
            headingSize = headingSuface.get_size()
            font = pygame.font.SysFont('consolas', 20)
            commentSuface = font.render('Press "space" to play', True, (0, 0, 0))
            commentSize = commentSuface.get_size()
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYUP:
                        if event.key == K_SPACE:
                            return
                bg.draw()
                DISPLAYSURF.blit(headingSuface, (int((HGH27_WINDOWWIDTH - headingSize[0])/2), 100))
                DISPLAYSURF.blit(commentSuface, (int((HGH27_WINDOWWIDTH - commentSize[0])/2), 400))
                pygame.display.update()
                fpsClock.tick(FPS)
    
        def gamePlay(bg, car, obstacles, score):
            car.__init__()
            obstacles.__init__()
            bg.__init__()
            score.__init__()
            moveLeft = False
            moveRight = False
            moveUp = False
            moveDown = False
            temp=DieuKhien.get()
            while True:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        if temp =='LEFT-RIGHT-UP-DOWN':
                            if event.type == KEYDOWN:
                                if event.key == K_LEFT:
                                    moveLeft = True
                                if event.key == K_RIGHT:
                                    moveRight = True
                                if event.key == K_UP:
                                    moveUp = True
                                if event.key == K_DOWN:
                                    moveDown = True
                            if event.type == KEYUP:
                                if event.key == K_LEFT:
                                    moveLeft = False
                                if event.key == K_RIGHT:
                                    moveRight = False
                                if event.key == K_UP:
                                    moveUp = False
                                if event.key == K_DOWN:
                                    moveDown = False
                        else:
                            if event.type == KEYDOWN:
                                if event.key == K_a:
                                    moveLeft = True
                                if event.key == K_d:
                                    moveRight = True
                                if event.key == K_w:
                                    moveUp = True
                                if event.key == K_s:
                                    moveDown = True
                            if event.type == KEYUP:
                                if event.key == K_a:
                                    moveLeft = False
                                if event.key == K_d:
                                    moveRight = False
                                if event.key == K_w:
                                    moveUp = False
                                if event.key == K_s:
                                    moveDown = False
                if isGameover(car, obstacles):
                    return
                bg.draw()
                bg.update()
                car.draw()
                car.update(moveLeft, moveRight, moveUp, moveDown)
                obstacles.draw()
                obstacles.update()
                score.draw()
                score.update()
                pygame.display.update()
                fpsClock.tick(FPS)

        bg = Background()
        car = Car()
        obstacles = Obstacles()
        score = Score()
        gameStart(bg)
        while True:
            gamePlay(bg, car, obstacles, score)
            gameOver(bg, car, obstacles, score)
            
    
    HGH27=tk_27hghan.Tk()
    HGH27.title('27_Huỳnh Gia Hân_21133031_GAME ĐUA XE')
    HGH27.geometry('550x250')
    bt_Background_27=tk_27hghan.Button(HGH27, text='Lựa chọn Background',command=selectBackGround_Game27,background='yellow')
    bt_Background_27.place(x=5,y=30)

    bt_SelectCar_27=tk_27hghan.Button(HGH27, text='Lựa chọn Car',command=SelectCar_27,background='yellow')
    bt_SelectCar_27.place(x=135,y=30)
        
    bt_SelectObstacle_27=tk_27hghan.Button(HGH27, text='Lựa chọn Obstacle',command=SelectObstacle_27,background='yellow')
    bt_SelectObstacle_27.place(x=225,y=30)


    lb_DoRong_27=tk_27hghan.Label(HGH27, text='Độ rộng: ', background='#FFCC66')
    lb_DoRong_27.place(x=10,y=90)
    EnTry_Rong = tk_27hghan.Entry(HGH27, width=20)
    EnTry_Rong.place(x = 70,y=90)

    lb_DoCao_27=tk_27hghan.Label(HGH27, text='Độ cao: ', background='#FFCC66')
    lb_DoCao_27.place(x=200,y=90)
    EnTry_Cao = tk_27hghan.Entry(HGH27, width=20)
    EnTry_Cao.place(x = 250,y=90)

    lb_FPS_27=tk_27hghan.Label(HGH27, text='FPS: ', background='#FFCC66')
    lb_FPS_27.place(x=375,y=90)
    spinbox_FPS_27 = tk_27hghan.Spinbox(HGH27, from_=0, to=120)
    spinbox_FPS_27.place(x=410,y=90)

    lb_TocDoCuon_27=tk_27hghan.Label(HGH27, text='Tốc độ cuốn: ', background='#FFCC66')
    lb_TocDoCuon_27.place(x=10,y=120)
    spinbox_Vcuon_27 = tk_27hghan.Spinbox(HGH27, from_=0, to=50, increment=0.1, format="%0.2f")
    spinbox_Vcuon_27.place(x=90,y=120)

    lb_Solan_27=tk_27hghan.Label(HGH27, text='Số làn: ', background='#FFCC66')
    lb_Solan_27.place(x=200,y=120)
    spinbox_Solan_27 = tk_27hghan.Spinbox(HGH27, from_=0, to=10)
    spinbox_Solan_27.place(x=250,y=120)

    lb_control_27=tk_27hghan.Label(HGH27, text='Lựa chọn nút điều khiển:')
    lb_control_27.place(x=10, y=150)
    DieuKhienList = ['A-D-W-S','LEFT-RIGHT-UP-DOWN']
    DieuKhien = ttk.Combobox(HGH27,values=DieuKhienList,state='readonly')
    DieuKhien.place(x=150,y=150)
    
    bt_PlayGame_27=tk_27hghan.Button(HGH27, text='Play Game',command=Game,background='Light Blue')
    bt_PlayGame_27.place(x=150,y=200)
    def Thoat():
        HGH27.destroy()    
        
    bt_Thoat_27=tk_27hghan.Button(HGH27, text='Thoát',command=Thoat,background='#CC99CC')
    bt_Thoat_27.place(x=400,y=200)
    
    HGH27.mainloop()
if __name__=='__main__':
    Load_Form_Car()