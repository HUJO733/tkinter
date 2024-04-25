# 입력값에 따른 버튼 패딩값 변경
# .pack(pady = 숫자)

from tkinter import *

win = Tk() # 창 생성하기

win.geometry('500x500') # 창 크기
win.title('title') # 창 제목
win.option_add('*Font', '맑은고딕 25') # 폰트 설정

ent = Entry(win)
ent.pack()

btn = Button(win)
btn.config(text= '버튼1')

def move():
    btn.pack(pady = ent.get())

btn.config(command = move)
btn.pack()

btn2 = Button(win)
btn2.config(text= '버튼2')
btn2.pack()

win.mainloop() # 창 실행