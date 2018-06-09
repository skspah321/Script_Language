# -*- coding:utf-8 -*-
import Func_search
from tkinter import*
from tkinter import ttk
import ctypes
import Enter_Webbrowser


favoriteDict = {}


blogtitle = []
blogurl = []





class MyFrame(Frame):
    def __init__(self, master):
        root.geometry("700x500")
        self.ComboBox()
        self.str = StringVar()
        self.Search_box()
        self.Listbox()
        self.favoriteCombobox()
        self.favoriteButton()
        self.favoriteMoveButton()
        self.emailButton()

    def ComboBox(self):  # 검색 종류 분류해줌
        self.Box_value = StringVar()
        self.boxlist = ['통합검색', '블로그', '카페']
        self.Box = ttk.Combobox(root, textvariable=self.Box_value, values=self.boxlist)
        # self.Box['values'] = ('통합검색', '블로그', '카페')
        self.Box.grid(column=0, row=0)
        self.Box.current(0)
        self.Box.bind("<<ComboboxSelected>>", self.comboboxtest)

    def comboboxtest(self, *args):  # 콤보박스 선택시 이벤트 (검색 항목 선택)
        if self.Box_value.get() == self.boxlist[0]: # 통합검색 일때
            print("통합검색")
            if type(blogtitle) == list and len(blogtitle) != 0:  # 리스트 목록 초기화
                blogtitle.clear()
                blogurl.clear()

            self.BlogValue(Func_search.Search_Blog(self.Getstr))  # json file 넘기기

        elif self.Box_value.get() == self.boxlist[1]:  # 블로그 일때
            print("블로그")
            if type(blogtitle) == list and len(blogtitle) != 0:  # 리스트 목록 초기화
                blogtitle.clear()
                blogurl.clear()

            self.BlogValue(Func_search.Search_Blog(self.Getstr))  # json file 넘기기

        else:   # 카페일때
            print("페")
            if type(blogtitle) == list and len(blogtitle) != 0:  # 리스트 목록 초기화
                blogtitle.clear()
                blogurl.clear()

            self.BlogValue(Func_search.Search_Blog(self.Getstr))  # json file 넘기기

    def getvalue(self):  # button 이벤트인데 textbox값 전달해주는 함수
        global blogtitle

        if not "맛집" in self.str.get():
            ctypes.windll.user32.MessageBoxW(0, "키워드에 '맛집'을 추가해주세요", "경고!", 1)
            return 0

        self.Getstr = self.str.get() # 검색값

        if self.Box_value.get() == self.boxlist[0]:  # 통합검색 일때
            self.insertvalue(blogtitle)
            print("통합검색")

        elif self.Box_value.get() == self.boxlist[1]:  # 블로그 일때
            self.insertvalue(blogtitle)
            print("블로그")

        else: # 통합검색 일때
            self.insertvalue(blogtitle)
            print("카페")


    def insertvalue(self, str):  # button 이벤트인데 text값을 받아 리스트박스에 추가하는 부분 (*딕셔너리로 해야할꺼같음.)
        self.insertvalue2 = str
        self.aaa = len(self.insertvalue2) # 리스트 길이
        self.listbox.delete(0, END)
        for x in range(self.aaa):
            try:
                self.listbox.insert(x, self.insertvalue2[x])
            except:
                print("List Error")

    def onselect(self, evt):  # 리스트박스 이벤트
        w = evt.widget
        self.index = int(w.curselection()[0])
        self.value = w.get(self.index)

        #if 블로그 일때,카페일때, 통합검색일때
        #Enter_Webbrowser.Open_Webbrowser(blogurl[self.index])
        #print('u selected item %d:"%s"' % (self.index, self.value))


    def Search_box(self):  # 검색 창
        self.textbox = ttk.Entry(root, width=70, textvariable=self.str)
        self.textbox.grid(column=0, row=1)

        self.textboxButton = ttk.Button(root, text="검색", command=self.getvalue)
        self.textboxButton.grid(column=1, row=1)

    def Listbox(self):  # 검색값 보여주는 리스트박스
        self.listbox = Listbox(root, selectmode='extended', width=70, height=20, bd=4)
        self.listbox.grid(column=0, row=3)
        self.listbox.bind('<<ListboxSelect>>', self.onselect)

    def favoriteCombobox(self):
        self.faBox_value = StringVar()
        self.faBox = ttk.Combobox(root, textvariable=self.faBox_value, values=favoriteDict, width=65)
        self.label = Label(root, text="즐겨찾기 목록").grid(column=0, row=5)
        self.faBox.grid(column=0, row=6)


    def favoriteButton(self):
        self.faButton = ttk.Button(root, text="favorite", command=self.favoriteAppend)
        self.faButton.grid(column=0, row=4)

        self.faButton2 = ttk.Button(root, text="이미지", command=self.favoriteAppend)
        self.faButton2.grid(column=1, row=4)

        self.faButton3 = ttk.Button(root, text="지도", command=self.favoriteAppend)
        self.faButton3.grid(column=2, row=4)


    def favoriteAppend(self):  # 즐겨찾기 목록 최근검색 순으로 눈에보임.
        global favoriteDict

        #질문: 지금은 블로그일때 저장하는건데 카페나 통합검색일땐=
        favoriteDict[blogtitle[self.index]] = blogurl[self.index]  # onselect 의 self.value
        self.test123 = []

        for x in favoriteDict.keys():
            self.test123.insert(0,x)

        self.faBox.config(values=self.test123)
        self.faBox.current(0)

    def favoriteMoveButton(self):
        self.faButton = ttk.Button(root, text="이동", command=self.favoriteAppend)
        self.faButton.grid(column=1, row=6)

    def emailButton(self):
        self.faButton = ttk.Button(root, text="이메일보내기", command=self.favoriteAppend)
        self.faButton.grid(column=1, row=7)



    def BlogValue(self, jsonfile):
        for x in jsonfile["items"]:
            test1 = x["title"].replace('<b>', '').replace('</b>', '').replace('&amp','')
            blogtitle.append(test1)

        for x in jsonfile["items"]:
            test1 = x["link"].replace("?Redirect=Log&amp;logNo=", "/")
            blogurl.append(test1)


def main():
    global root
    root = Tk()
    myframe = MyFrame(root)
    root.mainloop()


if __name__ == '__main__':
    main()
