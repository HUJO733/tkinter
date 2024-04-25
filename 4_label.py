# 다음 카카오로그인 gui 만들기

from tkinter import *
from selenium.webdriver import ChromeOptions
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# 브라우저 꺼짐 방지 옵션
options = ChromeOptions()
options.add_experimental_option("detach", True)
# 불필요한 에러 메시지 삭제
options.add_experimental_option("excludeSwitches", ["enable-logging"])
# 크롬 드라이버 최신 버전 설정
service = ChromeService(ChromeDriverManager().install())


#----------창 생성
win = Tk() # 창 생성하기

win.geometry('400x400') # 창 크기
win.title('title') # 창 제목
win.option_add('*Font', '맑은고딕 15') # 폰트 설정

# 구글 로고 이미지
labg = Label(win) # 라벨 생성
img = PhotoImage(file = 'daum_logo.png', master = win) # 이미지 지정
labg.config(image = img) # 이미지 설정
labg.pack() # 라벨 배치

#----------ID
lab1 = Label(win) # 라벨 생성
lab1.config(text = 'ID') # 라벨명 설정
lab1.pack() # 라벨 배치

ent1 = Entry(win) # 입력창 생성
ent1.insert(0, 'abc@abc.com')

def clear(e):
    if ent1.get() == 'abc@abc.com': # 처음 클릭했을때만 지워지게
        ent1.delete(0, len(ent1.get())) # 내용 지우기
    
ent1.bind('<Button-1>', clear) # 마우스 좌클릭시 clear 함수 실행
ent1.pack() # 입력창 배치

#----------PW
lab2 = Label(win)
lab2.config(text = 'PW')
lab2.pack()

ent2 = Entry(win)
ent2.config(show = '*') # 텍스트를 * 로 보이게함
ent2.pack()

#----------버튼
btn = Button(win) # 버튼 생성

btn.config(width = 10, height = 3) # 버튼 크기
btn.config(text = '로그인') # 버튼 내용

def login():
    # 웹 드라이버 설정
    driver = webdriver.Chrome(service=service, options=options)
    
    url = 'https://accounts.kakao.com/login/?continue=https%3A%2F%2Faccounts.kakao.com%2Fweblogin%2Faccount#login'
    driver.get(url)
    driver.implicitly_wait(5) # 로딩을 5초 기다림, 5초 내로 로딩되면 다음 실행

    id_xp = '//*[@id="loginId--1"]'
    driver.find_element(By.XPATH, id_xp).send_keys(ent1.get())
    driver.implicitly_wait(5)

    pw_xp = '//*[@id="password--2"]'
    driver.find_element(By.XPATH, pw_xp).send_keys(ent2.get().strip())
    driver.implicitly_wait(5)

    login_btn_xp = '//*[@id="mainContent"]/div/div/form/div[4]/button[1]'
    driver.find_element(By.XPATH, login_btn_xp).click()
    
    lab3.config(text = '로그인 성공!!')
    
    print(ent1.get(), ent2.get())
        
btn.config(command = login) # 버튼 기능(함수)
btn.pack() # 버튼 배치(중앙 설정)

# 로그인 메세지 라벨
lab3 = Label(win)
lab3.pack()

win.mainloop() # 창 실행