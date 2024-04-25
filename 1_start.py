from tkinter import *

win = Tk() # 창 생성하기

win.geometry('800x800') # 창 크기
win.title('title') # 창 제목
win.option_add('*Font', '맑은고딕 25') # 폰트 설정
win.configure(bg='red') # 배경 색 설정

win.mainloop() # 창 실행