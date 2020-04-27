from tkinter import *
from tkinter.filedialog import *
from tkinter.simpledialog import *

def loadbasicImage(fname) :
    global inImage
    fp = open(fname, 'rb')

    for i in range(0, XSIZE) :
        tmpList = []
        for k in range(0, YSIZE) :
            data = int(ord(fp.read(1)))
            tmpList.append(data)
        inImage.append(tmpList)

    fp.close()

def loadNewImage() :
    filename = askopenfilename(parent=window, filetypes = (("RAW 파일", "*.raw"), ("모든 파일", "*,*")))
    fp = open(filename, 'rb')

    for i in range(0, XSIZE) :
        tmpList = []
        for k in range(0, YSIZE) :
            data = int(ord(fp.read(1)))
            tmpList.append(data)
        inImage.append(tmpList)

    fp.close()

def displayImage(image) :
    rgbString = ""
    for i in range(0, XSIZE):
        tmpString = ""
        for k in range(0, YSIZE):
            data = image[i][k]
            tmpString += "#%02x%02x%02x " % (data, data, data)
        rgbString += "{" + tmpString + "} "
    paper.put(rgbString)

def func_exit() :
    window.quit()
    window.destroy()

def toBright(image) :
    rgbString = ""
    for i in range(0, XSIZE) :
        tmpString = ""
        for k in range(0, YSIZE) :
            data = image[i][k]
            tmpString += "#%02x%02x%02x " % (data+5,data+5,data+5)
        rgbString += "{" + tmpString + "} "
    paper.put(rgbString)

def toDark(image) :
    global XSIZE, YSIZE


def toReverse(image) :
    global XSIZE, YSIZE

window = None
canvas = None
XSIZE, YSIZE = 256, 256
inImage = []

window = Tk()
window.title("흑백 사진 보기")
canvas = Canvas(window, height = XSIZE, width = YSIZE)
paper = PhotoImage(width = XSIZE, height = YSIZE)
canvas.create_image((XSIZE/2, YSIZE/2), image = paper, state = "normal")

filename = "D:\수업\오픈소스기초프로젝트\\tree.raw"
loadbasicImage(filename)

mainMenu = Menu(window)
window.config(menu=mainMenu)
fileMenu = Menu(window)
mainMenu.add_cascade(label = "파일", menu = fileMenu)
fileMenu.add_command(label = "파일 열기", command = loadNewImage)
fileMenu.add_separator()
fileMenu.add_command(label = "프로그램 종료", command = func_exit)

imageEffectMenu = Menu(window)
mainMenu.add_cascade(label = "사진효과", menu = imageEffectMenu)
imageEffectMenu.add_command(label = "밝게하기", command = toBright(inImage))
imageEffectMenu.add_separator()
imageEffectMenu.add_command(label = "어둡게하기", command = toDark(inImage))
imageEffectMenu.add_separator()
imageEffectMenu.add_command(label = "반전 이미지", command = toReverse(inImage))

displayImage(inImage)

canvas.pack()
window.mainloop()