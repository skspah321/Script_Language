# -*- coding:utf-8 -*-
import Func_search
from tkinter import*
from tkinter import ttk
import ctypes
import Send_Email
import Global_data

Email_ID = "skspah888@naver.com"
Email_Check = False

class MyFrame2(Frame):
    def __init__(self, master):
        root.geometry("300x50")
        self.str = StringVar()
        self.Search_box()

    def getvalue(self):  # button 이벤트인데 textbox값 전달해주는 함수
        global Email_ID, Email_Check
        try:
            Email_ID = self.str.get()  # 검색값
            Send_Email.Send_Text(Email_ID,Global_data.Favorite_All)

            ctypes.windll.user32.MessageBoxW(0, "즐겨찾기 목록에 있는 리스트를 해당 이메일로 전송하였습니다.", "성공!", 0)
        except:
            if not '@' in self.str.get():
                ctypes.windll.user32.MessageBoxW(0, "잘못된 이메일 형식입니다", "오류!", 0)



    def Search_box(self):  # 전송을
        self.textbox = ttk.Entry(root, width=30, textvariable=self.str)
        self.textbox.grid(column=0, row=1)

        self.textboxButton = ttk.Button(root, text="전송", command=self.getvalue)
        self.textboxButton.grid(column=1, row=1)




def main():
    global root
    root = Toplevel()
    root.title("이메일 보내기")
    myframe = MyFrame2(root)
    root.mainloop()


if __name__ == '__main__':
    main()
