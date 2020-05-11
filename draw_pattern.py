import math
from PIL import ImageTk, ImageDraw
import cv2



class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'


def eraseSelectedCropping(pixelList, bc, img):
    for i in pixelList:
        img.putpixel(i[0], bc)


def cropping(startPoint, endPoint, bc, img):
    pixelList = []

    x0 = startPoint[0]
    y0 = startPoint[1]
    x1 = endPoint[0]
    y1 = endPoint[1]

    if y0 > y1:
        y0, y1 = y1, y0
    if x0 > x1:
        x0, x1 = x1, x0

    for j in range(y0, y1):
        for i in range(x0, x1):
            if img.getpixel((i, j)) != bc:
                color = img.getpixel((i, j))
                pixelObj = ((i, j), color)
                pixelList.append(pixelObj)
                img.putpixel((i, j), bc)

    return pixelList


def scalling(pixelList, center, scale, img):
    centerX = center[0]
    centerY = center[1]

    # render new pattern based on coordinate of newPoint
    for i in range(0, len(pixelList) - 1):
        pixel = pixelList[i]

        x = centerX + int(round((pixel[0][0] - centerX) * scale[0]))
        y = centerY + int(round((pixel[0][1] - centerY) * scale[1]))

        img.putpixel((x, y), pixel[1])

    scaleImg = ImageTk.PhotoImage(img)
    return scaleImg


def ellipse(points, color, img, width):
    draw = ImageDraw.Draw(img)
    draw.ellipse(points, outline=color, width=width)
    ellipseImg = ImageTk.PhotoImage(img)
    return ellipseImg


def flipHorizontal(startPoint, endPoint, center, bc, img):
    pixelList = []

    x0 = startPoint[0]
    y0 = startPoint[1]
    x1 = endPoint[0]
    y1 = endPoint[1]

    if y0 > y1:
        y0, y1 = y1, y0
    if x0 > x1:
        x0, x1 = x1, x0

    for j in range(y0, y1):
        for i in range(x0, x1):
            if img.getpixel((i, j)) != bc:
                color = img.getpixel((i, j))
                pixelObj = ((i, j), color)
                pixelList.append(pixelObj)
                img.putpixel((i, j), bc)

    for i in range(0, len(pixelList) - 1):
        pixel = pixelList[i]
        x = pixel[0][0]
        y = 2 * center[1] - pixel[0][1]
        img.putpixel((x, y), pixel[1])

    flipVerticalImg = ImageTk.PhotoImage(img)
    return flipVerticalImg


def flipVertical(startPoint, endPoint, center, bc, img):
    pixelList = []

    x0 = startPoint[0]
    y0 = startPoint[1]
    x1 = endPoint[0]
    y1 = endPoint[1]

    if y0 > y1:
        y0, y1 = y1, y0
    if x0 > x1:
        x0, x1 = x1, x0

    for j in range(y0, y1):
        for i in range(x0, x1):
            if img.getpixel((i, j)) != bc:
                color = img.getpixel((i, j))
                pixelObj = ((i, j), color)
                pixelList.append(pixelObj)
                img.putpixel((i, j), bc)

    for i in range(0, len(pixelList) - 1):
        pixel = pixelList[i]
        x = 2 * center[0] - pixel[0][0]
        y = pixel[0][1]
        img.putpixel((x, y), pixel[1])

    flipVerticalImg = ImageTk.PhotoImage(img)
    return flipVerticalImg

def moveRotation(pixelList, center, alpha, bc, img):
    for i in range(0, len(pixelList) - 1):
        pixel = pixelList[i]

        centerX = center[0]
        centerY = center[1]

        x = centerX + int(math.cos(alpha) * (pixel[0][0] - centerX) - math.sin(alpha) * (pixel[0][1] - centerY))
        y = centerY + int(math.sin(alpha) * (pixel[0][0] - centerX) + math.cos(alpha) * (pixel[0][1] - centerY))

        img.putpixel((x, y), pixel[1])

    roateImg = ImageTk.PhotoImage(img)
    return roateImg


def moveTransition(pixelList, newPoint, bc, img):
    deltaX = newPoint[0] - pixelList[0][0][0]
    deltaY = newPoint[1] - pixelList[0][0][1]

    for i in range(0, len(pixelList) - 1):
        pixel = pixelList[i]
        img.putpixel((pixel[0][0] + deltaX, pixel[0][1] + deltaY), pixel[1])

    transitImg = ImageTk.PhotoImage(img)
    return transitImg


def pencil(previousPoint, pointNow, color, img, width):
    draw = ImageDraw.Draw(img)
    draw.line((previousPoint, pointNow), color, width=width)

    pencilImg = ImageTk.PhotoImage(img)
    return pencilImg


def eraser(previousPoint, pointNow, color, img, width):
    draw = ImageDraw.Draw(img)
    draw.rectangle([previousPoint, pointNow], fill=color, width=width)

    eraserImg = ImageTk.PhotoImage(img)
    return eraserImg


def diamond(startPoint, endPoint, color, img, defaultState, width):
    a = (endPoint[1] - startPoint[1]) / float(2)
    b = (endPoint[0] - startPoint[0]) / float(2)

    A = (int(startPoint[0] + b), int(startPoint[1]))
    B = (int(startPoint[0]), int(startPoint[1] + a))
    C = (int(startPoint[0] + b), int(startPoint[1]) + 2 * a)
    D = (int(startPoint[0] + 2 * b), int(startPoint[1] + a))

    draw = ImageDraw.Draw(img)
    points = (A, B, C, D, A)

    draw.line(points, color, width)
    smooth_corners(points, draw, width, color, n=2.3)

    triangleImg = ImageTk.PhotoImage(img)
    return triangleImg


def polygonFive(startPoint, endPoint, color, img, defaultState, width):
    a = (endPoint[1] - startPoint[1]) / float(2)
    b = (endPoint[0] - startPoint[0]) / float(2)

    A = (int(startPoint[0] + b), int(startPoint[1]))
    B = (int(startPoint[0]), int(startPoint[1] + a))
    C = (int(startPoint[0] + b / 2), int(startPoint[1]) + 2 * a)
    D = (int(startPoint[0] + 3 * b / 2), int(startPoint[1] + 2 * a))
    E = (int(startPoint[0] + 2 * b), int(startPoint[1] + a))

    draw = ImageDraw.Draw(img)
    points = (A, B, C, D, E, A)
    draw.line(points, color, width)
    smooth_corners(points, draw, width, color, n=2.3)

    triangleImg = ImageTk.PhotoImage(img)
    return triangleImg


def polygonSix(startPoint, endPoint, color, img, defaultState, width):
    a = (endPoint[1] - startPoint[1]) / float(2)
    b = (endPoint[0] - startPoint[0]) / float(2)

    A = (int(startPoint[0] + b), int(startPoint[1]))
    B = (int(startPoint[0]), int(startPoint[1] + a / 2))
    C = (int(startPoint[0]), int(startPoint[1]) + 3 * a / 2)
    D = (int(startPoint[0] + b), int(startPoint[1] + 2 * a))
    E = (int(startPoint[0] + 2 * b), int(startPoint[1] + 3 * a / 2))
    F = (int(startPoint[0] + 2 * b), int(startPoint[1] + a / 2))

    draw = ImageDraw.Draw(img)
    points = (A, B, C, D, E, F, A)
    draw.line(points, color, width)
    smooth_corners(points, draw, width, color, n=2.3)

    triangleImg = ImageTk.PhotoImage(img)
    return triangleImg


def starFour(startPoint, endPoint, color, img, defaultState, width):
    a = (endPoint[1] - startPoint[1]) / float(2)
    b = (endPoint[0] - startPoint[0]) / float(2)

    A = (int(startPoint[0] + b), int(startPoint[1]))
    B = (int(startPoint[0] + 3 * b / 4), int(startPoint[1] + 3 * a / 4))
    C = (int(startPoint[0]), int(startPoint[1]) + a)
    D = (int(startPoint[0] + 3 * b / 4), int(startPoint[1] + 1.25 * a))
    E = (int(startPoint[0] + b), int(startPoint[1] + 2 * a))
    F = (int(startPoint[0] + 1.25 * b), int(startPoint[1] + 1.25 * a))
    G = (int(startPoint[0] + 2 * b), int(startPoint[1] + a))
    H = (int(startPoint[0] + 1.25 * b), int(startPoint[1] + 3 * a / 4))

    draw = ImageDraw.Draw(img)
    points = (A, B, C, D, E, F, G, H, A)
    draw.line(points, color, width)
    smooth_corners(points, draw, width, color, n=2.3)

    triangleImg = ImageTk.PhotoImage(img)
    return triangleImg


def starSix(startPoint, endPoint, color, img, defaultState, width):
    a = (endPoint[1] - startPoint[1]) / float(2)
    b = (endPoint[0] - startPoint[0]) / float(2)

    A = (int(startPoint[0] + b), int(startPoint[1]))
    B = (int(startPoint[0] + 3 * b / 4), int(startPoint[1] + a / 2))
    C = (int(startPoint[0]), int(startPoint[1]) + a / 2)
    D = (int(startPoint[0] + b / 2), int(startPoint[1] + a))
    E = (int(startPoint[0]), int(startPoint[1] + 1.5 * a))
    F = (int(startPoint[0] + 3 * b / 4), int(startPoint[1] + 1.5 * a))
    G = (int(startPoint[0] + b), int(startPoint[1] + 2 * a))
    H = (int(startPoint[0] + 1.25 * b), int(startPoint[1] + 1.5 * a))
    I = (int(startPoint[0] + 2 * b), int(startPoint[1] + 1.5 * a))
    J = (int(startPoint[0] + 1.5 * b), int(startPoint[1] + a))
    K = (int(startPoint[0] + 2 * b), int(startPoint[1] + a / 2))
    L = (int(startPoint[0] + 1.25 * b), int(startPoint[1] + a / 2))

    draw = ImageDraw.Draw(img)
    points = (A, B, C, D, E, F, G, H, I, J, K, L, A)
    draw.line(points, color, width)
    smooth_corners(points, draw, width, color, n=2.3)

    triangleImg = ImageTk.PhotoImage(img)
    return triangleImg


def triangle(startPoint, endPoint, color, img, width):
    b = (endPoint[0] - startPoint[0]) / float(2)

    A = (int(startPoint[0]), int(endPoint[1]))
    B = (int(endPoint[0]), int(endPoint[1]))
    C = (int(startPoint[0] + b), int(startPoint[1]))

    points = (A, B, C, A)
    draw = ImageDraw.Draw(img)

    draw.line(points, color, width)
    smooth_corners(points, draw, width, color)

    triangleImg = ImageTk.PhotoImage(img)
    return triangleImg


def triangleSquare(startPoint, endPoint, color, img, defaultState, width):
    A = (int(startPoint[0]), int(startPoint[1]))
    B = (int(startPoint[0]), int(endPoint[1]))
    C = (int(endPoint[0]), int(endPoint[1]))

    points = (A, B, C, A)
    draw = ImageDraw.Draw(img)

    draw.line(points, color, width)

    smooth_corners(points, draw, width, color)
    triangleSquareImg = ImageTk.PhotoImage(img)


    return triangleSquareImg


def star(startPoint, endPoint, color, img, defaultState, width):
    a = (endPoint[1] - startPoint[1]) / float(2)
    b = (endPoint[0] - startPoint[0]) / float(2)

    A = (int(startPoint[0] + b), int(startPoint[1]))
    A1 = (int(startPoint[0] + 3 * b / 4), int(startPoint[1] + 3 * a / 4))
    A2 = (int(startPoint[0]), int(0.8 * a + startPoint[1]))
    A3 = (int(startPoint[0] + b * 0.65), int(startPoint[1] + 1.25 * a))
    A4 = (int(startPoint[0] + b / 2), int(startPoint[1] + 2 * a))

    B = (int(startPoint[0] + b), int(1.25 * a + startPoint[1]))
    B1 = (int(startPoint[0] + 1.5 * b), int(2 * a + startPoint[1]))
    B2 = (int(startPoint[0] + 1.35 * b), int(1.25 * a + startPoint[1]))
    B3 = (int(startPoint[0] + 2 * b), int(0.8 * a + startPoint[1]))
    B4 = (int(startPoint[0] + 1.25 * b), int(3 * a / 4 + startPoint[1]))

    draw = ImageDraw.Draw(img)
    points = (A, A1, A2, A3, A4, B, B1, B2, B3, B4, A)
    draw.line(points, color, width)
    smooth_corners(points, draw, width, color, n=2.3)
    starImg = ImageTk.PhotoImage(img)
    return starImg


def arrowRight(startPoint, endPoint, color, img, defaultState, width):
    a = (endPoint[1] - startPoint[1]) / float(2)
    b = (endPoint[0] - startPoint[0]) / float(2)

    A1 = (int(startPoint[0]), int(a / 2 + startPoint[1]))
    A2 = (int(startPoint[0] + 4 * b / 3), int(a / 2 + startPoint[1]))
    A3 = (int(startPoint[0] + 4 * b / 3), int(startPoint[1]))

    B1 = (int(startPoint[0]), int(3 * a / 2 + startPoint[1]))
    B2 = (int(startPoint[0] + 4 * b / 3), int(3 * a / 2 + startPoint[1]))
    B3 = (int(startPoint[0] + 4 * b / 3), int(2 * a + startPoint[1]))

    C = (int(startPoint[0] + 2 * b), int(a + startPoint[1]))

    draw = ImageDraw.Draw(img)
    points = (A1, A2, A3, C, B3, B2, B1, A1)
    draw.line(points, color, width)

    smooth_corners(points, draw, width, color)
    arrowRightImg = ImageTk.PhotoImage(img)
    return arrowRightImg


def rectangle(pointA, pointB, color, img, defaultState, width):
    draw = ImageDraw.Draw(img)
    if defaultState:  # draw square
        edge = abs(pointB[0] - pointA[0])
        if pointB[1] > pointA[1]:
            pointB = (pointB[0], edge + pointA[1])
        else:
            pointB = (pointB[0], abs(pointA[1] - edge))
        draw.rectangle([pointA, pointB], None, color, width=width)
    else:
        draw.rectangle([pointA, pointB], None, color, width=width)

    rectangleImg = ImageTk.PhotoImage(img)
    return rectangleImg


def line(startPoint, endPoint, color, img, defaultState, width):
    draw = ImageDraw.Draw(img)

    dx = endPoint.x - startPoint.x
    dy = endPoint.y - startPoint.y

    if defaultState == 1:
        if abs(dx) > abs(dy):
            endPoint.y = startPoint.y
        else:
            endPoint.x = startPoint.x

    draw.line([(startPoint.x, startPoint.y), (endPoint.x, endPoint.y)], color, width)
    lineImg = ImageTk.PhotoImage(img)
    return lineImg


def fillColor(img, center, bc, newColor, paperWidth, paperHeight):
    print('center ', center)

    oldColor = img.getpixel(center)
    if oldColor == newColor:
        return

    listSeed = []
    listSeed.append(center)
    while listSeed:
        seed = listSeed.pop(0)
        try:
            seedColor = img.getpixel(seed)
        except IndexError:
            seedColor = None
        if seedColor == oldColor:
            img.putpixel(seed, newColor)
            x, y = seed[0], seed[1]
            listSeed.append((x + 1, y))
            listSeed.append((x - 1, y))
            listSeed.append((x, y + 1))
            listSeed.append((x, y - 1))

    filledImg = ImageTk.PhotoImage(img)
    return filledImg


def smooth_corners(corners, draw, width, color, n=2):
    for corner in corners:
        draw.ellipse((corner[0] - width / n, corner[1] - width / n, corner[0] + width / n, corner[1] + width / n),
                     color)
