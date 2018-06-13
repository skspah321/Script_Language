# -*- coding:utf-8 -*-
import Func_search
from tkinter import *
from tkinter import ttk
import Global_data
import Tk_GetImage
import ctypes


data_sort = 'sim'   # 최신순 or 정확도순
Search_number = 10   # 검색 개수 설정

imagetitle = []
imageurl = []

class MyFrame(Frame):
    def __init__(self, master):
        root.geometry("530x380")
        self.str = StringVar()
        self.Listbox()
        self.MoveButton()
        self.getvalue()


    def getvalue(self):  # button 이벤트인데 textbox값 전달해주는 함수
        imagetitle.clear()
        imageurl.clear()
        try:
            self.ImageValue(Func_search.Search_Image(Global_data.Search_value,int(Global_data.Get_Num),Global_data.Get_Sort))  # json file 넘기기
            self.insertvalue(imagetitle)
        except:
            ctypes.windll.user32.MessageBoxW(0, "키워드 검색을 먼저 해 주세요.", "오류!", 0)


    def onselect(self, evt):  # 리스트박스 이벤트
        w = evt.widget
        try:
            self.index = int(w.curselection()[0])
            self.value = w.get(self.index)
        except: pass

    def Listbox(self):  # 검색값 보여주는 리스트박스
        self.label = Label(root, text=str(Global_data.Search_value)+"에 대한 이미지 검색 결과입니다.").grid(column=0, row=0)
        self.listbox = Listbox(root, selectmode='extended', width=60, height=20, bd=4)
        self.listbox.grid(column=0, row=1)
        self.listbox.bind('<<ListboxSelect>>', self.onselect)

    def insertvalue(self, str):  # button 이벤트인데 text값을 받아 리스트박스에 추가하는 부분 (*딕셔너리로 해야할꺼같음.)
        self.insertvalue2 = str
        self.aaa = len(self.insertvalue2)  # 리스트 길이
        self.listbox.delete(0, END)
        for x in range(self.aaa):
            try:
                self.listbox.insert(x, self.insertvalue2[x])
            except:
                pass
                #print("List Error")

    def GetImage(self):  # 이동 버튼 눌렀을 때
        try:
            Tk_GetImage.Open_Image(Func_search.Search_Image(Global_data.Search_value, Global_data.Get_Num, Global_data.Get_Sort),self.index)
        except:
            ctypes.windll.user32.MessageBoxW(0, "연결 할 이미지가 없습니다", "오류!", 0)


    def MoveButton(self):  # 이동 버튼
        self.faButton = ttk.Button(root, text="이미지 보기", command=self.GetImage)
        self.faButton.grid(column=1, row=1)

    def ImageValue(self, jsonfile):
        for x in jsonfile["items"]:
            test1 = x["title"].replace('<b>', '').replace('</b>', '').replace('&amp', '')
            imagetitle.append(test1)

        for x in jsonfile["items"]:
            test1 = x["link"]
            imageurl.append(test1)


def main():
    global root
    root = Toplevel()
    root.title("맛집을 찾아라!! - 이미지")
    myframe = MyFrame(root)
    root.mainloop()


if __name__ == '__main__':
    main()
