from tkinter import *
from datetime import datetime

win = Tk() # 창 생성하기

win.geometry('800x800') # 창 크기
win.title('title') # 창 제목
win.option_add('*Font', '맑은고딕 15') # 폰트 설정
win.configure(bg='black') # 배경 색 설정

#----------버튼
btn = Button(win) # 버튼 생성

btn.config(width = 10, height = 3) # 버튼 크기
btn.config(text = '현재 시각') # 버튼 내용

def time():
    print(datetime.now().strftime("%Y년 %m월 %d일 %H시 %M분 %S.%f초"))
    
btn.config(command = time) # 버튼 기능(함수)
btn.place(relx=0.5, rely=0.5, anchor='center') # 버튼 배치(중앙 설정)

win.mainloop() # 창 실행