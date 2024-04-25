from tkinter import *
import random
from datetime import datetime

win = Tk() # 창 생성하기

win.geometry('550x150') # 창 크기
win.title('AIM_GAME') # 창 제목
win.option_add('*Font', '맑은고딕 20') # 폰트 설정

# 라벨
lab = Label(win)
lab.config(text = '표적 개수')
lab.grid(column=0, row=0, padx=20, pady=20)

# 입력창
ent = Entry(win)
ent.grid(column=1, row=0, padx=20, pady=20)

count = 1

# 랜덤으로 생성된 버튼 클릭
def click():
    global count
    if count < num_t:
        count += 1
        btn.destroy()
        ran_btn()
    else:
        fin = datetime.now()
        dif_sec = (fin - start).total_seconds()
        btn.destroy()
        lab = Label(win)
        lab.config(text = 'clear ' + str(dif_sec) + ' 초')
        lab.pack(pady = 230)
        
# 버튼 랜덤위치 생성
def ran_btn():
    global btn
    btn = Button(win)
    btn.config(bg='red')
    btn.config(command = click)
    btn.config(text = count)
    btn.place(relx=random.random() * 0.9, rely=random.random() * 0.9)

# 버튼
def btn_f():
    global num_t # 전역변수 설정
    global start
    num_t = int(ent.get())
    
    for wg in win.grid_slaves(): # win.grid_slaves() = 위젯 리스트
        wg.destroy() # 요소 제거
    
    win.geometry('500x500') # 창 크기 변경
    ran_btn()

    start = datetime.now()

btn = Button(win)
btn.config(text = '시작')
btn.grid(column=0, row=1, columnspan=2)
btn.config(command = btn_f)

win.mainloop() # 창 실행