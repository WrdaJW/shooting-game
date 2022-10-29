import turtle
import random
import time
import winsound
import math


#터틀 이미지 저장
turtle.register_shape("게임배경.gif")
turtle.register_shape("플레이어.gif")
turtle.register_shape("보스배경.gif")
turtle.register_shape("도움말.gif")
turtle.register_shape("도움말2.gif")
turtle.register_shape("보스도움말.gif")
turtle.register_shape("돌.gif")
turtle.register_shape("파워.gif")
turtle.register_shape("물고기.gif")
turtle.register_shape("체력.gif")
turtle.register_shape("보스 하트.gif")
turtle.register_shape("보스.gif")
turtle.register_shape("공격.gif")
turtle.register_shape("그물.gif")
turtle.register_shape("승리.gif")

get_story = ["어느 강에 수달 가족이 살고있었습니다",
             "이 수달 가족은 맑은 강에서 물고기를 먹으며 행복하게 생활하고 있었습니다",
             "어느날 부모 수달이 잠깐 사냥을 하러간 사이 사냥꾼들이 새끼수달을 잡아갔습니다",
             "이를 본 엄마 수달은 사냥꾼들을 따라가게 되는데......"]
             
             
             
#게임 제어
gameover =False
start = True
story = True
play = False
pause = False
help = False
line = 0
boss = False
boss_help = False
sound =0
item_time1 = 0
item_time2 = 0
boss_timer = 0
sound = 0
sound_on = 0
basic_music = 0
boss_music = 0
no_key = 0


#캐릭터, 배경변수
help_num = 0
speed = 0.5
boss_life = 3
life = 3
score=0
mbg_speed = 0
player_speed = 0
rock_speed = 0
boss_speed = 0
item_speed1 = 0
item_speed2 = 0
boss_attack_speed = 0
player_attack_speed = 0
mode = 0

#스크린
start_screen = turtle.Screen()
start_screen.setup(1200, 700)
start_screen.tracer(0)

#배경화면
bg = turtle.Turtle()
bg.shape("게임배경.gif")
bg.penup()
bg.setposition(0,0)


#움직이는 배경
mbg=turtle.Turtle()
mbg.ht()
mbg.shape("게임배경.gif")
mbg.speed(0)
mbg.penup()
mbg.setposition(-350, 0)

#도움말
hpage = turtle.Turtle()
hpage.penup()
hpage.ht()
hpage.shape("도움말.gif")

#글자
#점수
score_text = turtle.Turtle()
score_text.color("black")
score_text.ht()
score_text.penup()
score_text.goto(0, 250)
#제목
title_text = turtle.Turtle()
title_text.color("black")
title_text.ht()
title_text.penup()
title_text.goto(0,100)
title_text.write("달려라 수달", align="center", font=("System", 50, "bold"))
#시작문구
start_text = turtle.Turtle()
start_text.color("black")
start_text.ht()
start_text.penup()
start_text.goto(0,-100)
start_text.write("스페이스 키를 누르세요", align="center", font=("System", 25, "bold"))
#스토리문구1
first_line = turtle.Turtle()
first_line.color("white")
first_line.ht()
first_line.penup()
first_line.goto(0, 150)
#스토리문구2
second_line = turtle.Turtle()
second_line.color("white")
second_line.ht()
second_line.penup()
second_line.goto(0, 50)
#스토리문구3
third_line = turtle.Turtle()
third_line.color("white")
third_line.ht()
third_line.penup()
third_line.goto(0, -50)
#스토리문구4
fourth_line = turtle.Turtle()
fourth_line.color("white")
fourth_line.ht()
fourth_line.penup()
fourth_line.goto(0, -150)

pause_text = turtle.Turtle()
pause_text.color("black")
pause_text.ht()
pause_text.penup()
pause_text.goto(0,-100)


#스페이스를 누르시오
press_space = turtle.Turtle()
press_space.color("white")
press_space.ht()
press_space.penup()


#함수
#접촉확인
def check_touch(t1, t2):
    dis = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(), 2))
    if dis<45:
        return True
    else:
        return False

#플레이어 조작
def move_up():
    y=p.ycor()
    y+=player_speed
    if y>280 :
        y=280
    p.sety(y)
   
def move_down():
    y=p.ycor()
    y-=player_speed
    if y<-280 :
        y=-280
    p.sety(y)

def move_left():
    x=p.xcor()
    x-=player_speed
    if x<-570 :
        x=-570
    p.setx(x)

def move_right():
    x=p.xcor()
    x+=player_speed
    if x>380 :
        x=380
    p.setx(x)

def shoot():
    if mode==1 and help == False:
        a.setposition(p.xcor()+5, p.ycor())
        a.st()


#게임상태 (시작화면, 중지, 도움말, 스토리)
#중지
def pause_game() :
    global pause
    change_speed(False)
    if no_key == 0:
        pause = True
        pause_text.write("스페이스 키를 누르면 시작됩니다", align="center", font=("System", 25, "bold"))
    

#재개
def resume_game():
    global pause
    if no_key==0:
        pause=False
        change_speed(True)
        p.st()
        if mode == 1:
            a.st()
        if boss == True:
            b_a.st()
        item1.st()
        item2.st()
        for r in rock:
            r.st()
        score_text.clear()
        s_t = "SCORE:%s"%score
        score_text.write(s_t, align="center", font=("System", 25, "normal"))
    
#스페이스 이벤트
def get_space():
    global start
    global line
    global story
    global help
    global help_num
    global basic_music
    global boss
    if start==True:
        start_text.clear()
        title_text.clear()
        start = False
    if story == True :
        
        if line == 0:
            first_line.write(get_story[line], align="center", font=("Arial", 25, "normal"))
            press_space.goto(390, 80)
            press_space.write("스페이스키를 누르세요" , align="center", font=("고딕", 17, "bold"))
            line+=1
        elif line == 1:
            second_line.write(get_story[line], align="center", font=("System", 25, "normal"))
            press_space.clear()
            press_space.goto(390, -20)
            press_space.write("스페이스키를 누르세요" , align="center", font=("고딕", 17, "bold"))
            line+=1
        elif line == 2:
            third_line.write(get_story[line], align="center", font=("System", 25, "normal"))
            press_space.clear()
            press_space.goto(390, -120)
            press_space.write("스페이스키를 누르세요" , align="center", font=("고딕", 17, "bold"))
            line+=1
        elif line == 3:
            fourth_line.write(get_story[line], align="center", font=("System", 25, "normal"))
            press_space.clear()
            press_space.goto(390, -220)
            press_space.write("스페이스키를 누르세요" , align="center", font=("고딕", 17, "bold"))
            line+=1
        elif line == 4:
            story=False
            first_line.clear()
            second_line.clear()
            third_line.clear()
            fourth_line.clear()
            press_space.clear()
            help_mode()
    else :
        if help==True :
            if help_num == 0:
                help_num = 1
                hpage.shape("도움말2.gif")
                
            elif help_num == 1:
                if boss_help == False :
                    help_num = 0
                    hpage.shape("도움말.gif")
                    hpage.ht()
                    mbg.st()
                    help=False
                    basic_music = 1
                    resume_game()
                else :
                    help_num = 2
                    hpage.shape("보스도움말.gif")
            elif help_num ==2 :
                help_num = 0
                hpage.shape("도움말.gif")
                hpage.ht()
                mbg.st()
                help=False
                boss=True
                resume_game()

        elif pause == True:
            resume_game()
            pause_text.clear()

#도움말           
def help_mode() :   
    global help
    if no_key==0:
        help = True
        pause = True
        mbg.st()
        hpage.st()
        for r in rock:
            r.ht()
        for p_l in p_life:
            p_l.ht()
        for b_l in b_life:
            b_l.ht()
        item1.ht()
        item2.ht()
        p.ht()
        b.ht()
        score_text.clear()
        change_speed(False)
        b_a.ht()
        a.ht()
    
    
def end_game():
    end_text=turtle.Turtle()
    end_text.color("white")
    end_text.ht()
    end_text.speed(0)
    end_text.penup()
    end_text.goto(0, 0)
    if life<=0:
        end_text.write("GAME OVER", align="center", font=("System", 50, "bold"))
    else:
        end_text.write("YOU WIN!", align="center", font=("System", 50, "bold"))

#플레이어 라이프
def show_life(l):
    temp = l
    for i in range(5):
        if temp < 0:
            p_life[i].ht()
        else : 
            p_life[i].st()
        temp-=1

#보스 라이프
def show_boss_life(boss_l):
    temp = boss_l
    for i in range(3):
        if temp <0:
            b_life[i].ht()
        else:
            b_life[i].st()
        temp-=1
        
#플레이중 변경사항(노래, 배경)
def changeSound(sound):
    if sound==0:
        winsound.PlaySound("Sabana Havana - Jimmy Fontanez_Media Right Productions.wav",winsound.SND_ASYNC)
    elif sound==1:
        winsound.PlaySound("Walking the Dog - Silent Partner.wav",winsound.SND_ASYNC)
    elif sound==2:
        winsound.PlaySound("Plain Truth - Gunnar Olsen.wav",winsound.SND_ASYNC)
        

def change_speed(gs):
    global mbg_speed, player_speed, rock_speed, boss_speed, item_speed1, item_speed2, boss_attack_speed, player_attack_speed
    if gs==True:
        mbg_speed = speed
        player_speed = speed*30
        rock_speed = speed
        boss_speed = speed
        item_speed1 = speed
        item_speed2 = speed*1.1
        boss_attack_speed = speed*1.4
        player_attack_speed = speed*1.4
        
    else :
        mbg_speed = 0
        player_speed = 0
        rock_speed = 0
        boss_speed = 0
        item_speed1 = 0
        item_speed2 = 0
        boss_attack_speed = 0
        player_attack_speed = 0

def shoot():
    if(mode==1):
        a.setposition(p.xcor()+5, p.ycor())
        a.st()

def end_credit():
    b_a.ht()
    a.ht()
    b.ht()
    p.ht()
    item1.ht()
    score_text.clear()
    for r in rock:
        r.ht()
    for p_l in p_life:
        p_l.ht()
    for b_l in b_life:
        b_l.ht()
    win=turtle.Turtle()
    win.penup()
    win.setposition(730, 0)
    win.shape("승리.gif")  
    while(p.xcor() >-730):
        start_screen.update()
        win.fd(-speed*0.7)
    
#터틀들
#보스공격
b_a =  turtle.Turtle()
b_a.shape("그물.gif")
b_a.color("red")
b_a.speed(0)
b_a.penup()
b_a.setposition(-500, -450)
b_a.ht()
#공격
a = turtle.Turtle()
a.shape("공격.gif")
a.speed(0)
a.penup()
a.setposition(-500, 450)
a.ht()

#보스
b = turtle.Turtle()
b.shape("보스.gif")
b.speed(0)
b.penup()
b.setposition(490, 0)
b.ht()

#플레이어
p = turtle.Turtle()
p.shape("플레이어.gif")
p.speed(0)
p.penup()
p.setposition(-450, 0)
p.ht()

#아이템
#체력회복
item1 = turtle.Turtle()
item1.shape("물고기.gif")
item1.speed(0)
item1.penup()
x=random.randint(-500, 370)
item1.setposition(x, 450)
#공격가능
item2=turtle.Turtle()
item2.shape("파워.gif")
item2.speed(0)
item2.penup()
x=random.randint(-500, 370)
item2.setposition(x, 450)

#적 
rock=[]
r_pos = -3
for i in range(5):
    rock.append(turtle.Turtle())
    
for r in rock:
    r.shape("돌.gif")
    r.speed(0)
    r.penup()
    y=random.randint((r_pos*100)+50, ((r_pos+1)*100)+50)
    x=random.randint(630, 730)
    r.setposition(x, y)
    r_pos+=1
    r.ht()

#플레이어 체력
p_life=[]
for i in range(5):
    p_life.append(turtle.Turtle())

l_pos = 0
for p_l in p_life:
    l_pos+=1
    p_l.shape("체력.gif")
    p_l.speed(0)
    p_l.penup()
    p_l.setposition(-570+(l_pos*70), -230)
    p_l.ht()
    
#보스 체력
b_life=[]
for i in range(3):
    b_life.append(turtle.Turtle())

b_l_pos = 0
for b_l in b_life:
    b_l_pos+=1
    b_l.ht()
    b_l.shape("보스 하트.gif")
    b_l.speed(0)
    b_l.penup()
    b_l.setposition(470-(b_l_pos*60), -230)


#커맨드
turtle.listen()
turtle.onkeypress(move_up, "Up")
turtle.onkeypress(move_down, "Down")
turtle.onkeypress(move_left, "Left")
turtle.onkeypress(move_right,"Right")
turtle.onkeypress(shoot, "a")
turtle.onkeypress(get_space, "space")
turtle.onkeypress(pause_game, "Escape")
turtle.onkeypress(help_mode, "h")


#반복
while True:
    start_screen.update()
    if sound_on==0:
        changeSound(0)
        sound_on+=1

    elif sound_on==1 and basic_music==1:
        changeSound(1)
        sound_on+=1

    elif sound_on==2 and boss==True:
        changeSound(2)
        sound_on+=1
        
    if boss == True:
        mbg.shape("보스배경.gif")
    if help == False and story == False:
        b.st()
        mbg_x=mbg.xcor()
        mbg_x-=mbg_speed
        mbg.setx(mbg_x)
        if mbg.xcor() <-350:
            mbg.setposition(350, 0)
        
        if mode == 1:
            a.fd(player_attack_speed)

        #보스 관련
        if boss == True:
            boss_timer+=1
            if boss_timer == 100:
                b_x = random.randint(380, 460)
                b_y = random.randint(-280, 280)
                b.setposition(b_x, b_y)
                b_a.setposition(b.xcor()-5, b.ycor())
                b_a.st()
            b_a.fd(-boss_attack_speed)
            if b_a.xcor()<-500:
                b_a.setposition(700,400)
                boss_timer = 0
           
            if check_touch(p, b_a):
                life-=1
                b_a.ht()
                b_a.setposition(700,400)
                if life==0:
                    gameover=True

                score-=10
                s_t="SCORE:%s"%score
                score_text.clear()
                score_text.write(s_t, align="center", font=("System", 25, "bold"))
                boss_timer = 0
                
            if check_touch(a, b_a) and mode==1:
                score+=10
                boss_life -= 1
                if score>= 50:
                    boss=True
                s_t="SCORE:%s"%score
                score_text.clear()
                score_text.write(s_t, align="center", font=("System", 25, "bold"))                
                b_a.setposition(500, -450)
                a.setposition(-500, 450)
                a.ht()
                b_a.ht()
                boss_timer = 0
                
        #적 관련
        for r in rock:
            if r_pos > 1:
                r_pos = -3
            r_x = r.xcor()
            r_x-=rock_speed
            r.setx(r_x)

            if r.xcor()<-505:
                r_y=random.randint((r_pos*100)+50, ((r_pos+1)*100)+50)
                r_x=random.randint(630, 730)
                r.setposition(r_x, r_y)

            #플레이어, 적 접촉
            if check_touch(p, r):
                life-=1
                
                x=random.randint(630, 730)
                y=random.randint((r_pos*100)+50, ((r_pos+1)*100)+50)
                r.setposition(x, y)

                if life==0:
                    gameover=True

                score-=10
                s_t="SCORE:%s"%score
                score_text.clear()
                score_text.write(s_t, align="center", font=("System", 25, "bold"))
                
            #공격, 적 접촉
            if check_touch(a, r) and mode==1:
                score+=10
                
                s_t="SCORE:%s"%score
                score_text.clear()
                score_text.write(s_t, align="center", font=("System", 25, "bold"))                
                y=random.randint((r_pos*100)+50, ((r_pos+1)*100)+50)
                x=random.randint(630, 730)
                r.setposition(x, y)
                a.ht()
                a.setposition(-500, 450)
            r_pos+=1
            
            if score>= 50:
                    if boss_help == False :
                        hpage.shape("보스도움말.gif")
                        help_num = 2
                        help_mode()
                        boss_help = True
                        
                    
        # 아이템관련
        item_time1 += 1
        # 공격 불가일때만 아이템 드랍
        if(mode==0):
            item_time2 +=1
            
        if item_time1 >=80:
            i1_y= item1.ycor()
            i1_y-=item_speed1
            item1.sety(i1_y)
            
        if item_time2 >=80:
            i2_y= item2.ycor()
            i2_y-=item_speed2
            item2.sety(i2_y)

        if item1.ycor()<-300:
            x=random.randint(-380,370)
            item1.setposition(x, 450)
            item_time1=0
            
        if item2.ycor()<-300:
            x=random.randint(-380,370)
            item2.setposition(x, 450)
            item_time2=0

        #회복 아이템 획득 
        if check_touch(p, item1):
            life+=1
            if life>=5 : life=5
       
            score+=20
            s_t="SCORE:%s"%score
            score_text.clear()
            score_text.write(s_t, align="center", font=("System", 25, "bold"))
            x=random.randint(-380,370)
            item1.setposition(x, 450)
            item_time1=0

        #공격가능 아이템 획득
        if check_touch(p, item2):
           x=random.randint(-380,370)
           item2.setposition(x, 450)
           item_time2=0
           mode=1
           
           
        #플레이어 라이프
        if help==False and story == False:
            show_life(life-1)
            if boss ==True :
                show_boss_life(boss_life-1)
        
        #게임종료
        if gameover==True:
            no_key = 1
            pause_game()
            winsound.PlaySound("Radio Macarena Jingle Logo 04 C by deleted_user_133379 Id-137212.wav",winsound.SND_ASYNC)
            end_game()
            break
        
        if boss_life==0:
            no_key = 1
            winsound.PlaySound("Twinkle Twinkle Little Star (instrumental) - The Green Orbs.wav",winsound.SND_ASYNC)
            end_game()
            pause_game()
            end_credit()
            break
start_screen.mainloop()

    
