# -*- coding:utf-8 -*-
import Func_search
from tkinter import *
from tkinter import ttk
import ctypes
import Enter_Webbrowser
import GUI_Email
import Global_data
import Tk_GetImage
import GUI_Image
import GUI_Map

favoriteDict = {}

blogtitle = []
blogurl = []

cafetitle = []
cafeurl = []

alltitle = []
allurl = []

data_sort = 'sim'   # 최신순 or 정확도순
Search_number = 10   # 검색 개수 설정


class MyFrame(Frame):
    def __init__(self, master):
        root.geometry("600x500")
        self.ComboBox()
        self.str = StringVar()
        self.Search_box()
        self.Listbox()
        self.favoriteCombobox()
        self.favoriteButton()
        self.favoriteMoveButton()
        self.EmailButton()
        self.MapButton()
        self.ImageButton()
        self.EnterSite()

    def ComboBox(self):  # 검색 종류 분류해줌
        self.Box_value = StringVar()
        self.boxlist = ['통합검색', '블로그', '카페']
        self.Box = ttk.Combobox(root, textvariable=self.Box_value, values=self.boxlist)
        self.Box.grid(column=0, row=0)
        self.Box.current(0)
        self.Box.bind("<<ComboboxSelected>>", self.comboboxtest)

        self.Box_value2 = StringVar()
        self.boxlist2 = ['정확도순', '최신순']
        self.Box2 = ttk.Combobox(root, textvariable=self.Box_value2, values=self.boxlist2, width=9)
        self.Box2.place(x=336,y=0)
        self.Box2.current(0)
        self.Box2.bind("<<ComboboxSelected>>", self.comboboxtest)

        self.Box_value3 = StringVar()
        self.boxlist3 = ['10', '20', '30', '40', '50']
        self.Box3 = ttk.Combobox(root, textvariable=self.Box_value3, values=self.boxlist3, width=7)
        self.Box3.place(x=426,y=0)
        self.Box3.current(0)
        self.Box3.bind("<<ComboboxSelected>>", self.comboboxtest)

    def comboboxtest(self, *args):  # 콤보박스 선택시 이벤트 (검색 항목 선택)
        if self.Box_value.get() == self.boxlist[0]:  # 통합검색 일때
            if type(alltitle) == list and len(alltitle) != 0:  # 리스트 목록 초기화
                alltitle.clear()
                allurl.clear()

        elif self.Box_value.get() == self.boxlist[1]:  # 블로그 일때
            if type(blogtitle) == list and len(blogtitle) != 0:  # 리스트 목록 초기화
                blogtitle.clear()
                blogurl.clear()

        else:  # 카페일때
            if type(cafetitle) == list and len(cafetitle) != 0:  # 리스트 목록 초기화
                cafetitle.clear()
                cafeurl.clear()

    def getvalue(self):  # button 이벤트인데 textbox값 전달해주는 함수
        global blogtitle,alltitle,cafetitle
        self.comboboxtest()
        if self.Box_value2.get() == '최신순':
            self.GetLine = 'date'

        if self.Box_value2.get() == '정확도순':
            self.GetLine = 'sim'

        self.GetNum = str(self.Box_value3.get())
        self.Getstr = self.str.get()  # 검색값
        Global_data.Search_value = self.Getstr
        Global_data.Get_Sort = self.GetLine
        Global_data.Get_Num = self.GetNum

        try:
            if self.Box_value.get() == self.boxlist[0]:  # 통합검색 일때
                self.AllValue(Func_search.Search_All(self.Getstr,int(self.GetNum)//2,self.GetLine))  # json file 넘기기
                self.insertvalue(alltitle)

            elif self.Box_value.get() == self.boxlist[1]:  # 블로그 일때
                self.BlogValue(Func_search.Search_Blog(self.Getstr,self.GetNum,self.GetLine))  # json file 넘기기
                self.insertvalue(blogtitle)

            else:  # 카페 일때
                self.CafeValue(Func_search.Search_Cafe(self.Getstr,self.GetNum,self.GetLine))  # json file 넘기기
                self.insertvalue(cafetitle)
        except:
            ctypes.windll.user32.MessageBoxW(0, "키워드를 입력해주세요.", "경고!", 0)

    def insertvalue(self, str):  # button 이벤트인데 text값을 받아 리스트박스에 추가하는 부분 (*딕셔너리로 해야할꺼같음.)
        self.insertvalue2 = str
        self.aaa = len(self.insertvalue2)  # 리스트 길이
        self.listbox.delete(0, END)
        for x in range(self.aaa):
            try:
                self.listbox.insert(x, self.insertvalue2[x])
            except:
                ctypes.windll.user32.MessageBoxW(0, "List Error!", "오류!", 0)


    def onselect(self, evt):  # 리스트박스 이벤트
        w = evt.widget
        try:
            self.index = int(w.curselection()[0])
            self.value = w.get(self.index)
        except: pass
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
        self.faButton = ttk.Button(root, text="즐겨찾기 추가", command=self.favoriteAppend)
        self.faButton.place(x=500,y=349)

    def favoriteAppend(self):  # 즐겨찾기 목록 최근검색 순으로 눈에보임.
        global favoriteDict
        try:
            if self.Box_value.get() == self.boxlist[0]:  # 통합검색 일때
                favoriteDict[alltitle[self.index]] = allurl[self.index]  # onselect 의 self.value

            elif self.Box_value.get() == self.boxlist[1]:  # 블로그 일때
                favoriteDict[blogtitle[self.index]] = blogurl[self.index]  # onselect 의 self.value

            else:  # 카페 일때
                favoriteDict[cafetitle[self.index]] = cafeurl[self.index]  # onselect 의 self.value
        except:
            ctypes.windll.user32.MessageBoxW(0, "추가할 데이터를 선택 해 주세요.", "오류!", 0)

        self.test123 = []

        for x in favoriteDict.keys():
            self.test123.insert(0, x)

        self.faBox.config(values=self.test123)
        try:
            self.faBox.current(0)
        except: pass
        Global_data.Favorite_All = favoriteDict

    def SendEmail(self):  # 이메일 보내기 버튼 눌렀을 때
        GUI_Email.main()
        return 0

    def favoriteMove(self):  # 즐겨찾기 이동 버튼 눌렀을 때
        #print(self.faBox_value.get())
        self.fastr = self.faBox_value.get()
        try:
            Enter_Webbrowser.Open_Webbrowser(favoriteDict[self.fastr])
        except:
            ctypes.windll.user32.MessageBoxW(0, "연결할 데이터가 없습니다.", "오류!", 0)

    def GetImage(self):  # 이미지 버튼 눌렀을 때
        #print(self.Getstr, self.index)
        #Tk_GetImage.Open_Image(Func_search.Search_Image(self.Getstr, self.GetNum, self.GetLine),self.index)
        GUI_Image.main()




    def GetMap(self):  # 지도 버튼 눌렀을 때
        GUI_Map.main()

    def favoriteMoveButton(self):  # URL로 연결하기
        self.faButton = ttk.Button(root, text="이동", command=self.favoriteMove)
        self.faButton.grid(column=1, row=6)

    def EmailButton(self):  # 이메일 버튼
        self.Button = ttk.Button(root, text="이메일보내기", command=self.SendEmail)
        self.Button.grid(column=1, row=7)

    def ImageButton(self):  # 이미지 버튼
        self.Button = ttk.Button(root, text="이미지", command=self.GetImage)
        #self.Button.grid(column=1, row=4)
        self.Button.place(x=500, y=270)

    def MapButton(self):  # 지도 버튼
        self.Button = ttk.Button(root, text="지도", command=self.GetMap)
        #self.Button.grid(column=2, row=4)
        self.Button.place(x=500, y=300)

    def EnterSite(self):  # 사이트로 이동 버튼
        self.Button = ttk.Button(root, text="사이트 이동", command=self.Open_URL)
        #self.Button.grid(column=1, row=3)
        self.Button.place(x=500,y=100)

    def Open_URL(self):
        try:
            if self.Box_value.get() == self.boxlist[0]:  # 통합검색 일때
                Enter_Webbrowser.Open_Webbrowser(allurl[self.index])

            elif self.Box_value.get() == self.boxlist[1]:  # 블로그 일때
                Enter_Webbrowser.Open_Webbrowser(blogurl[self.index])

            else:  # 카페 일때
                Enter_Webbrowser.Open_Webbrowser(cafeurl[self.index])
        except:
            ctypes.windll.user32.MessageBoxW(0, "연결할 데이터가 없습니다.", "오류!", 0)

    def BlogValue(self, jsonfile):
        for x in jsonfile["items"]:
            test1 = x["title"].replace('<b>', '').replace('</b>', '').replace('&amp', '').replace('quot', '')
            blogtitle.append(test1)

        for x in jsonfile["items"]:
            test1 = x["link"].replace("?Redirect=Log&amp;logNo=", "/")
            blogurl.append(test1)

    def CafeValue(self, jsonfile):
        for x in jsonfile["items"]:
            test1 = x["title"].replace('<b>', '').replace('</b>', '').replace('&amp', '').replace('quot', '')
            cafetitle.append(test1)

        for x in jsonfile["items"]:
            test1 = x["link"].replace("?Redirect=Log&amp;logNo=", "/")
            cafeurl.append(test1)

    def AllValue(self, jsonfile):
        #and range(len(jsonfile[1])//2)
        for x in jsonfile[0]["items"]:
            test1 = x["title"].replace('<b>', '').replace('</b>', '').replace('&amp', '').replace('quot', '')
            alltitle.append(test1)

        for x in jsonfile[1]["items"]:
            test1 = x["title"].replace('<b>', '').replace('</b>', '').replace('&amp', '').replace('quot', '')
            alltitle.append(test1)

        for x in jsonfile[0]["items"]:
            test1 = x["link"].replace("?Redirect=Log&amp;logNo=", "/")
            allurl.append(test1)

        for x in jsonfile[1]["items"]:
            test1 = x["link"].replace("?Redirect=Log&amp;logNo=", "/")
            allurl.append(test1)


def main():
    global root
    root = Tk()
    root.title("맛집을 찾아라!!")
    myframe = MyFrame(root)
    root.mainloop()


if __name__ == '__main__':
    main()
