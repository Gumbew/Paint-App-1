import tkinter
from tkinter import *
from config import *
from PIL import Image, ImageTk


def configureFrame(self, master):
    self.paperWidth = 1000
    self.paperHeight = 1000
    self.chooseColor = red
    self.bgColor = white
    self.pixelList = None
    self.defaultState = 0  # if zero is line can be free, otherwise the line will be straight
    self.fOpenName = None
    self.width = 3
    self.master = master
    self.frame = tkinter.Frame(self.master)
    self.figures = [ImageTk.PhotoImage(Image.new("RGB", (self.paperWidth, self.paperHeight), self.bgColor))]
    self.layers = [Image.new("RGB", (self.paperWidth, self.paperHeight), self.bgColor)]
    self.master.bind('<Control-z>', self.callRedo)
    self.master.bind('<Control-n>', self.callNegative)
    self.master.bind('<Control-b>', self.callBlur)
    self.master.bind('<Control-t>', self.callContour)

def initFrame(self):
    self.master.title("Paint")

    self.active_button = self.pencilBtn
    self.color_button = self.redBtn
    self.myCanvas = tkinter.Canvas(self.master, height=self.paperHeight, width=self.paperWidth, bg="white")
    self.myCanvas.pack(expand=True, fill=BOTH)
    self.frame.pack(expand=YES, fill=BOTH)

    self.myCanvas.configure(scrollregion=(0, 0, 400, 400))
    hbar = Scrollbar(self.frame, orient=HORIZONTAL)
    hbar.pack(side=BOTTOM, fill=X)
    hbar.config(command=self.myCanvas.xview)
    vbar = Scrollbar(self.frame, orient=VERTICAL)
    vbar.pack(side=RIGHT, fill=Y)
    vbar.config(command=self.myCanvas.yview)
    self.myCanvas.config(width=500, height=500)
    self.myCanvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
    self.myCanvas.pack(side=LEFT, expand=True, fill=BOTH)


def createIconImage(self, img, useImg, iconPath, size):
    self[img] = Image.open(iconPath).resize(size, Image.ANTIALIAS)
    self[useImg] = ImageTk.PhotoImage(self[img])


def initIconToolbar(self):
    createIconImage(self, 'img1', 'useImg1', newIconPic, (20, 20))
    createIconImage(self, 'img2', 'useImg2', loadIconPic, (20, 20))
    createIconImage(self, 'img3', 'useImg3', saveIconPic, (20, 20))
    createIconImage(self, 'img4', 'useImg4', quitIconPic, (20, 20))

    createIconImage(self, 'dark', 'useDark', darkIconPic, (20, 20))
    createIconImage(self, 'red', 'useRed', redIconPic, (20, 20))
    createIconImage(self, 'green', 'useGreen', greenIconPic, (20, 20))
    createIconImage(self, 'yellow', 'useYellow', yellowIconPic, (20, 20))
    createIconImage(self, 'orange', 'useOrange', orangeIconPic, (20, 20))
    createIconImage(self, 'purple', 'usePurple', purpleIconPic, (20, 20))
    createIconImage(self, 'blueMalibu', 'useBlueMalibu', blueMalibuIconPic, (20, 20))
    createIconImage(self, 'blueLight', 'useBlueLight', blueLightIconPic, (20, 20))
    createIconImage(self, 'pink', 'usePink', pinkIconPic, (20, 20))

    createIconImage(self, 'moveTool', 'useMoveTool', moveIconPic, (30, 30))
    createIconImage(self, 'rotateTool', 'useRotateTool', rotateIconPic, (30, 30))
    createIconImage(self, 'scaleTool', 'useScaleTool', scaleIconPic, (30, 30))
    createIconImage(self, 'flipVerticalTool', 'useFlipVerticalTool', flipVerticalIconPic, (30, 30))
    createIconImage(self, 'flipHorizontalTool', 'useFlipHorizontalTool', flipHorizontalIconPic, (30, 30))
    createIconImage(self, 'pencil', 'usePencil', pencilIconPic, (30, 30))
    createIconImage(self, 'circle', 'useCircle', circleIconPic, (30, 30))
    createIconImage(self, 'rectangle', 'useRectangle', rectangleIconPic, (30, 30))
    createIconImage(self, 'diamond', 'useDiamond', diamondIconPic, (30, 30))
    createIconImage(self, 'starFour', 'useStarFour', starFourIconPic, (30, 30))
    createIconImage(self, 'starSix', 'useStarSix', starSixIconPic, (30, 30))
    createIconImage(self, 'polygonFive', 'usePolygonFive', polygonFiveIconPic, (30, 30))
    createIconImage(self, 'polygonSix', 'usePolygonSix', polygonSixIconPic, (30, 30))
    createIconImage(self, 'star', 'useStar', starIconPic, (30, 30))
    createIconImage(self, 'triangle', 'useTriangle', triangleIconPic, (30, 30))
    createIconImage(self, 'triangleSquare', 'useTriangleSquare', triangleSquareIconPic, (30, 30))

    createIconImage(self, 'fill', 'useFill', fillIconPic, (30, 30))
    createIconImage(self, 'lineTool', 'useLineTool', lineIconPic, (30, 30))
    createIconImage(self, 'arrowRight', 'useArrowRight', arrowRightIconPic, (30, 30))
    createIconImage(self, 'eraser', 'useEraser', eraserIconPic, (30, 30))

    self.paper = Image.new("RGB", (self.paperWidth, self.paperHeight), self.bgColor)
    self.usePaper = ImageTk.PhotoImage(self.paper)


def initMenubar(self):
    menubar = tkinter.Menu(self.master)

    fileMenu = tkinter.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="File", menu=fileMenu)
    fileMenu.add_command(label="New", command=self.callNew)
    fileMenu.add_command(label="Open", command=self.callOpenImage)
    fileMenu.add_command(label="Save", command=self.callSaveImage)
    fileMenu.add_command(label="Save as...", command=self.callSaveAsImage)
    fileMenu.add_command(label="Exit", command=self.frame.quit)

    menubar.add_command(label="About", command=self.callAbout)
    self.master.config(menu=menubar)


def initToolbar(self):
    self.toolbar = tkinter.Frame(self.master, borderwidth=2, relief='raised')

    newBtn = tkinter.Button(self.toolbar, image=self.useImg1, command=self.callNew)
    newBtn.pack(side=LEFT, fill=X)
    loadBtn = tkinter.Button(self.toolbar, image=self.useImg2, command=self.callOpenImage)
    loadBtn.pack(side=LEFT, fill=X)
    saveBtn = tkinter.Button(self.toolbar, image=self.useImg3, command=self.callSaveImage)
    saveBtn.pack(side=LEFT, fill=X)
    quitBtn = tkinter.Button(self.toolbar, image=self.useImg4, command=self.frame.quit)
    quitBtn.pack(side=LEFT, fill=X)

    self.toolbar.pack(side=TOP, fill=X)


def on_enter(self, event, nameButton):
    content = buttonDescription[nameButton]
    showText = content['title'] + '\n' + content['desc']
    self.descrpBtn.configure(text=showText)


def on_leave(self, enter):
    self.descrpBtn.configure(text="")


def createIconLayout(self, toolbar, img, nameButton, commandFunction):
    self[nameButton] = tkinter.Button(toolbar, image=img, command=commandFunction)

    self[nameButton].bind("<Enter>", lambda event: on_enter(self, event, nameButton))
    self[nameButton].bind("<Leave>", lambda event: on_leave(self, event))

    self[nameButton].pack(side=LEFT, fill=X)


def initDrawToolbar(self):
    self.drawToolbar = tkinter.Frame(self.master, borderwidth=2, relief='raised')

    iv = IntVar()
    L1 = Label(text="Line width:")
    L1.pack()
    iv.trace('w', lambda name, index, mode, iv=iv: change_width(self, iv))
    E1 = Entry(textvariable=iv, bd=5, width=3, )
    iv.set(1)
    E1.pack()

    createIconLayout(self, self.drawToolbar, self.useMoveTool, 'moveToolBtn', self.transitionTool)
    createIconLayout(self, self.drawToolbar, self.useRotateTool, 'rotateToolBtn', self.rotationTool)
    createIconLayout(self, self.drawToolbar, self.useScaleTool, 'scaleToolBtn', self.scalingTool)
    createIconLayout(self, self.drawToolbar, self.useFlipVerticalTool, 'flipVeticalToolBtn', self.flippingVerticalTool)
    createIconLayout(self, self.drawToolbar, self.useFlipHorizontalTool, 'flipHorizonToolBtn',
                     self.flippingHorizontalTool)
    createIconLayout(self, self.drawToolbar, self.usePencil, 'pencilBtn', self.drawPencilTool)
    createIconLayout(self, self.drawToolbar, self.useEraser, 'eraserBtn', self.eraserTool)
    createIconLayout(self, self.drawToolbar, self.useLineTool, 'lineToolBtn', self.drawLineTool)
    createIconLayout(self, self.drawToolbar, self.useCircle, 'circleBtn', self.drawCircleTool)
    createIconLayout(self, self.drawToolbar, self.useRectangle, 'rectangleBtn', self.drawRectangleTool)
    createIconLayout(self, self.drawToolbar, self.useDiamond, 'diamondBtn', self.drawDiamondTool)
    createIconLayout(self, self.drawToolbar, self.usePolygonFive, 'polygonFiveBtn', self.drawPolygonFiveTool)
    createIconLayout(self, self.drawToolbar, self.usePolygonSix, 'polygonSixBtn', self.drawPolygonSixTool)
    createIconLayout(self, self.drawToolbar, self.useStarFour, 'starFourBtn', self.drawStarFourTool)
    createIconLayout(self, self.drawToolbar, self.useStar, 'starBtn', self.drawStarTool)
    createIconLayout(self, self.drawToolbar, self.useStarSix, 'starSixBtn', self.drawStarSixTool)
    createIconLayout(self, self.drawToolbar, self.useArrowRight, 'arrowRightBtn', self.drawArrowRightTool)
    createIconLayout(self, self.drawToolbar, self.useTriangle, 'triangleBtn', self.drawTriangleTool)
    createIconLayout(self, self.drawToolbar, self.useTriangleSquare, 'triangleSquareBtn', self.drawTriangleSquareTool)
    createIconLayout(self, self.drawToolbar, self.useFill, 'fillBtn', self.fillColorTool)

    self.descrpBtn = tkinter.Label(self.drawToolbar, text="", width=40)
    self.descrpBtn.pack(side="top", fill="x")

    self.drawToolbar.pack(side=TOP, fill=X)


def initColorToolbar(self):
    self.colorToolbar = tkinter.Frame(self.master, borderwidth=2, relief='raised')

    createIconLayout(self, self.colorToolbar, self.useDark, 'darkBtn', lambda: self.onChangeColor(dark, 'darkBtn'))
    createIconLayout(self, self.colorToolbar, self.useRed, 'redBtn', lambda: self.onChangeColor(red, 'redBtn'))
    createIconLayout(self, self.colorToolbar, self.useGreen, 'greenBtn', lambda: self.onChangeColor(green, 'greenBtn'))
    createIconLayout(self, self.colorToolbar, self.useYellow, 'yellowBtn',
                     lambda: self.onChangeColor(yellow, 'yellowBtn'))
    createIconLayout(self, self.colorToolbar, self.useOrange, 'orangeBtn',
                     lambda: self.onChangeColor(orange, 'orangeBtn'))
    createIconLayout(self, self.colorToolbar, self.usePink, 'pinkBtn', lambda: self.onChangeColor(pink, 'pinkBtn'))
    createIconLayout(self, self.colorToolbar, self.useBlueLight, 'blueLightBtn',
                     lambda: self.onChangeColor(blueLight, 'blueLightBtn'))
    createIconLayout(self, self.colorToolbar, self.useBlueMalibu, 'blueMalibuBtn',
                     lambda: self.onChangeColor(blueMalibu, 'blueMalibuBtn'))
    createIconLayout(self, self.colorToolbar, self.usePurple, 'purpleBtn',
                     lambda: self.onChangeColor(purple, 'purpleBtn'))

    self.colorToolbar.pack(side=BOTTOM, fill=X)


def change_width(self, iv):
    self.width = iv.get()
