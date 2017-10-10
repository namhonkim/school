import turtle  #거북이 모듈 사용

turtle.bgcolor("black") #배경색을 검은색으로 바꿈
t = turtle.Pen()  #거북이 선 색
t.pencolor("green") #거북이 선 색을 초록색으로 지정
t.left(90)  #거북이를 왼쪽으로 90도 만큼 회전
t.speed(0)  #거북이 이동 속도 최대

height = 5 #높이 5
width = 2 #폭 2

for i in range(10): #10번 반복
  t.pensize(3)  #펜 굵기를 3으로 설정 
  k = 10 - i #i만큼 빼고 이동
  t.forward(k * height) #k * height만큼이동
  t.right(90) #90도만큼 오른쪽으로 회전
  t.forward(k * width)  #k * width 만큼이동
  t.right(90) #90도만큼 오른쪽으로 회전
  t.forward(k * height) #k * height만큼이동
  t.right(90) #90도만큼 오른쪽으로 회전
  t.forward(k * width)  #k * width 만큼이동
  t.right(90) #90도만큼 오른쪽으로 회전
  t.forward(k * height) #k * height만큼이동
  t.left(5) #5도 만큼 왼쪽으로 회전

for i in range(120): #120번 반복
    t.pensize(2) #펜 굵기를 2로 설정
    t.pencolor("red") #거북이 선 색을 빨간색으로 지정
    t.fd(i) #i만큼 이동
    t.lt(70) #70도만큼 회전


