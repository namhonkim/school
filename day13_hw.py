import turtle as t
import random

t.pensize(5)  #펜사이즈 5
 
t.up()        #한 변의 길이가 500인 사각형을 만듭니다.
t.goto(-250,0)
t.down()
t.goto(-250,250)
t.goto(250,250)
t.goto(250,-250)
t.goto(-250,-250)
t.goto(-250,0)



t.up()      #거북이를 원점으로 보냅니다.
t.goto(0,0)
t.down()

t.shape("turtle")  #거북이모양사용
t.pensize(1)       #펜사이즈 1

ang = random.randint(0,360)   # ang를 0부터 360중 랜덤으로 한 수를 지정
t.setheading(ang)             #거북이가 바라보는 방향을 ang로 지정


while True:        #영원히 반복
    while -250 < t.xcor() < 250 and -250 < t.ycor() < 250: # 거북이가 사각형안에 존재할때 계속 반복
        t.speed(0)
        t.fd(1)
        ang = t.heading()     #거북이가 바라보는 각도를 구합니다.

    while 250 <= t.xcor() < 251:    # 거북이가 오른쪽면에 충돌했을때 들어오는 각도를 계산하여 반사각을 정합니다
        if 0 < ang < 90:
            t.seth(180 - ang)
            t.fd(1)
        elif 270 < ang < 360:
            t.seth(540 - ang)
            t.fd(1)

    while -251 < t.xcor() <= -250:  # 거북이가 왼쪽면에 충돌했을때 들어오는 각도를 계산하여 반사각을 정합니다
        if 90 < ang < 180:
            t.seth(180 - ang)
            t.fd(1)
        elif 180 < ang < 270:
            t.seth(540 - ang)
            t.fd(1)

    while 250 <= t.ycor() < 251:   # 거북이가 위쪽면에 충돌했을때 들어오는 각도를 계산하여 반사각을 정합니다
        if 0 < ang < 180:
            t.seth(360 - ang)
            t.fd(1)

    while -251 < t.ycor() <= -250: # 거북이가 아래쪽면에 충돌했을때 들어오는 각도를 계산하여 반사각을 정합니다
        if 180 < ang < 360:
            t.seth(360 - ang)
            t.fd(1)

          
