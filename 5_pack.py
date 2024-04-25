# 입력값에 따른 버튼 위치 변경
# .pack(side = ['left', 'right', 'top', 'bottom'])

from tkinter import *

win = Tk() # 창 생성하기

win.geometry('500x500') # 창 크기
win.title('title') # 창 제목
win.option_add('*Font', '맑은고딕 25') # 폰트 설정

ent = Entry(win)
ent.pack(side = 'top') # left, right, top, bottom

btn = Button(win)
btn.config(text= '버튼')

def move():
    btn.pack(side = ent.get())

btn.config(command = move)
btn.pack()

win.mainloop() # 창 실행