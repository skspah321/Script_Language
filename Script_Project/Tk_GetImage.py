from tkinter import*
from io import BytesIO
import urllib.request
from PIL import Image, ImageTk

def Open_Image(jsonfile,num):
    root2 = Toplevel()
    i = int(num)
    root2.title('이미지')
    height = jsonfile['items'][i]['sizeheight']
    width = jsonfile['items'][i]['sizewidth']
    root2.geometry('600x600')

    # openapi로 이미지 url을 가져옴.
    url = jsonfile['items'][i]['link']
    with urllib.request.urlopen(url) as u:
        raw_data = u.read()

    im = Image.open(BytesIO(raw_data))
    im2 = im.resize((600, 600), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(im2)

    label = Label(root2, image=image)  #height=height, width=width
    label.pack()
    label.place(x=0, y=0)
    root2.mainloop()



