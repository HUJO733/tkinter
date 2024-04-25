# 4 x 3 버튼 array 만들기

from tkinter import *

win = Tk() # 창 생성하기

win.geometry('550x550') # 창 크기
win.title('title') # 창 제목
win.option_add('*Font', '맑은고딕 25') # 폰트 설정

btn_list = []
col_num = 4
row_num = 3

for i in range(0, col_num):
    for j in range(0, row_num):
        btn = Button(win)
        btn.config(text= '({}, {})'.format(i, j))
        btn.grid(column = i, row = j, padx = 10, pady = 10)
        btn_list.append(btn)

win.mainloop() # 창 실행