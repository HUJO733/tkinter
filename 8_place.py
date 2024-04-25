from tkinter import *

win = Tk() # 창 생성하기

win.geometry('550x550') # 창 크기
win.title('title') # 창 제목
win.option_add('*Font', '맑은고딕 25') # 폰트 설정

# 절대좌표(창 크기가 바뀌어도 위치 그대로)
xx = 30
yy = 50

btn = Button(win)
btn.config(text= '({}, {})'.format(xx, yy))
btn.place(x = xx, y = yy)

# 상대좌표(창 크기에 따라 위치 조정), 창 크기를 1로 가정
xxx = 0.3
yyy = 0.4

btn2 = Button(win)
btn2.config(text= '({}, {})'.format(xxx, yyy))
btn2.place(relx = xxx, rely = yyy)


win.mainloop() # 창 실행