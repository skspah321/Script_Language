# -*- coding:utf-8 -*-
import Func_search
from tkinter import *
from tkinter import ttk
import Global_data
import Tk_GetMap
import ctypes


maptitle = []
mapurl = []
mapdata1 = []
mapdata2 = []
mapdata3 = []
mapdata4 = []
mapdata5 = []

mapX = []
mapY = []


class MyFrame(Frame):
    def __init__(self, master):
        root.geometry("530x480")
        self.str = StringVar()
        self.Listbox()
        self.MoveButton()
        self.getvalue()
        self.Listbox2()

    def getvalue(self):  # button 이벤트인데 textbox값 전달해주는 함수
        maptitle.clear()
        mapurl.clear()
        mapdata1.clear()
        mapdata2.clear()
        mapdata3.clear()
        mapdata4.clear()
        mapdata5.clear()
        mapX.clear()
        mapY.clear()
        try:
            self.MapValue(Func_search.Search_Map(Global_data.Search_value,int(Global_data.Get_Num),Global_data.Get_Sort))  # json file 넘기기
            self.insertvalue(maptitle)
        except:
            ctypes.windll.user32.MessageBoxW(0, "키워드 검색을 먼저 해 주세요.", "오류!", 0)


    def onselect(self, evt):  # 리스트박스 이벤트
        w = evt.widget
        try:
            self.index = int(w.curselection()[0])
            self.value = w.get(self.index)
            self.listbox2.delete(0, 'end')
            self.listbox2.insert(0, "제목: " + str(maptitle[self.index]))
            self.listbox2.insert(1, "카테고리: " + str(mapdata1[self.index]))
            self.listbox2.insert(2, "설명: " + str(mapdata2[self.index]))
            self.listbox2.insert(3, "전화번호: " + str(mapdata3[self.index]))
            self.listbox2.insert(4, "지번주소: " + str(mapdata4[self.index]))
            self.listbox2.insert(5, "도로주소: " + str(mapdata5[self.index]))
        except: pass





    def Listbox(self):  # 검색값 보여주는 리스트박스
        self.label = Label(root, text=str(Global_data.Search_value)+"에 대한 지도 검색 결과입니다.").grid(column=0, row=0)
        self.listbox = Listbox(root, selectmode='extended', width=60, height=15, bd=4)
        self.listbox.grid(column=0, row=1)
        self.listbox.bind('<<ListboxSelect>>', self.onselect)

    def Listbox2(self):  # 정보값 보여주는 리스트박스
        self.label2 = Label(root, text="정보").grid(column=0, row=2)
        self.listbox2 = Listbox(root, selectmode='extended', width=60, height=10, bd=4)
        self.listbox2.grid(column=0, row=3)



    def insertvalue(self, str):  # button 이벤트인데 text값을 받아 리스트박스에 추가하는 부분 (*딕셔너리로 해야할꺼같음.)
        self.insertvalue2 = str
        self.aaa = len(self.insertvalue2)  # 리스트 길이
        self.listbox.delete(0, END)
        for x in range(self.aaa):
            try:
                self.listbox.insert(x, self.insertvalue2[x])
            except:
                ctypes.windll.user32.MessageBoxW(0, "List Error!", "오류!", 0)


    def GetMap(self):  # 이동 버튼 눌렀을 때
        try:
            Tk_GetMap.Open_Map(mapX,mapY,self.index)
        except:
            ctypes.windll.user32.MessageBoxW(0, "연결 할 지도가 없습니다.", "오류!", 0)


    def MoveButton(self):  # 이동 버튼
        self.faButton = ttk.Button(root, text="지도 보기", command=self.GetMap)
        self.faButton.place(x=430, y=100)


    def MapValue(self, jsonfile):
        for x in jsonfile["items"]:
            test1 = x["title"].replace('<b>', '').replace('</b>', '').replace('&amp', '')
            maptitle.append(test1)

        for x in jsonfile["items"]:
            test1 = x["link"]
            mapurl.append(test1)

        for x in jsonfile["items"]:
            test1 = x["category"]
            mapdata1.append(test1)

        for x in jsonfile["items"]:
            test1 = x["description"].replace('</b>','').replace('<b>','')
            mapdata2.append(test1)

        for x in jsonfile["items"]:
            test1 = x["telephone"]
            mapdata3.append(test1)

        for x in jsonfile["items"]:
            test1 = x["address"]
            mapdata4.append(test1)

        for x in jsonfile["items"]:
            test1 = x["roadAddress"]
            mapdata5.append(test1)

        for x in jsonfile["items"]:
            test1 = x["mapx"]
            mapX.append(test1)

        for x in jsonfile["items"]:
            test1 = x["mapy"]
            mapY.append(test1)



def main():
    global root
    root = Toplevel()
    root.title("맛집을 찾아라!! - 지도")
    myframe = MyFrame(root)
    root.mainloop()


if __name__ == '__main__':
    main()
