# 쇼핑몰의 상품 이름과 가격 가져오기

from tkinter import *
import requests
import bs4
from bs4 import BeautifulSoup
import re

win = Tk() # 창 생성하기

win.geometry('800x800') # 창 크기
win.title('title') # 창 제목
win.option_add('*Font', '궁서 15') # 폰트 설정
win.configure(bg='black') # 배경 색 설정

#----------입력창
ent = Entry(win) # 입력창 생성
ent.pack() # 입력창 배치

def lotto():
    url = 'https://onlyeco.co.kr/category/%EB%A6%AC%EB%B9%99/50/?page={}'.format(ent.get()) # get() 입력값 추출
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    t = []
    p = []

    # 상품 리스트
    items = soup.select('.box') # 아이템은 18개인데 찾은건 19개가 나옴
    i = 1
    for item in items:
        # 위에서 찾은 19개 중 마지막 데이터는 18번째 데이터와 중복됨
        if i <= 18:
            # 상품명
            title_text = item.select_one('.name')
            if isinstance(title_text, bs4.element.Tag):
                if ']' in title_text.text:
                    title = title_text.text.split(']')[1].strip()
                else:
                    title = title_text.text.split(':')[1].strip()
            # 상품가격
            price_text = item.select_one('[rel=판매가]')
            if isinstance(price_text, bs4.element.Tag):
                price = int(re.sub(r'판매가\s*:\s*|,|원', '', price_text.text))

            i += 1
        t.append(title)
        p.append(price)
        print(title, price)
    

#----------버튼
btn = Button(win) # 버튼 생성

btn.config(width = 20, height = 3) # 버튼 크기
btn.config(text = '1 ~ 10 중 하나 입력') # 버튼 내용    

btn.config(command = lotto) # 버튼 기능(함수)
btn.place(relx=0.5, rely=0.5, anchor='center') # 버튼 배치(중앙 설정)

win.mainloop() # 창 실행