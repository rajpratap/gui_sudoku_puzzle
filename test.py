# DEVELOPED BY RAJ PRATAP SINGH

import random
import tkinter.messagebox as tmsg
from tkinter import *
root = Tk()
sudoku=[
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]]
def gen(board):
    find = find_empty(board)
    if not find:
        return True
    else:
        row,col = find
    l = random.sample(range(1, 10), 9)
    for i in l:
        if valid(board, i, (row, col)):
            board[row][col] = i
            if gen(board):
                return True
            board[row][col] = 0
    return False
def valid(board, num, pos):
    #check for row
    for i in range(9):
        if board[pos[0]][i] == num and pos[1] != i:
            return False
    #check for column
    for i in range(9):
        if board[i][pos[1]] == num and pos[0] != i:
            return False
    #check for box
    box_x = pos[1]//3
    box_y = pos[0]//3
    for i in range(box_y*3, box_y*3+3):
        for j in range(box_x*3, box_x*3+3):
            if board[i][j] == num and (i, j) != pos:
                return False
    return True
def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None
def puzzle(board):
    x=[]
    for i in board:
        for j in i:
            x.append(j)
    x1 = random.sample(range(81), random.choice(range(35,50)))
    for i in x1:
        x[i] = ""
    board=[]
    t = 0
    for i in range(9):
        temp = []
        for j in range(9):
            temp.append(x[t])
            t += 1
        board.append(temp)
    return board
# GUI work
def canvas():
    c = Canvas(root)
    c.pack(fill=BOTH, expand=1)
    c.create_line(20, 50, 20, 410, 380, 410, 380, 50, 20, 50, width=3)
    c.create_line(140, 50, 140, 410, width=3)
    c.create_line(260, 50, 260, 410, width=3)
    c.create_line(20, 290, 380, 290, width=3)
    c.create_line(20, 170, 380, 170, width=3)
    c.create_line(20, 90, 380, 90, width=1)
    c.create_line(20, 130, 380, 130, width=1)
    c.create_line(20, 210, 380, 210, width=1)
    c.create_line(20, 250, 380, 250, width=1)
    c.create_line(20, 330, 380, 330, width=1)
    c.create_line(20, 370, 380, 370, width=1)
    c.create_line(60, 50, 60, 410, width=1)
    c.create_line(100, 50, 100, 410, width=1)
    c.create_line(180, 50, 180, 410, width=1)
    c.create_line(220, 50, 220, 410, width=1)
    c.create_line(300, 50, 300, 410, width=1)
    c.create_line(340, 50, 340, 410, width=1)
def clicked():
    global lst
    global lst1
    lst1 = []
    lst = [txt1.get(), txt2.get(), txt3.get(), txt4.get(), txt5.get(), txt6.get(),
         txt7.get(), txt8.get(), txt9.get(), txt10.get(), txt11.get(), txt12.get(),
         txt13.get(), txt14.get(), txt15.get(), txt16.get(), txt17.get(), txt18.get(),
         txt19.get(), txt20.get(), txt21.get(), txt22.get(), txt23.get(), txt24.get(),
         txt25.get(), txt26.get(), txt27.get(), txt28.get(), txt29.get(), txt30.get(),
         txt31.get(), txt32.get(), txt33.get(), txt34.get(), txt35.get(), txt36.get(),
         txt37.get(), txt38.get(), txt39.get(), txt40.get(), txt41.get(), txt42.get(),
         txt43.get(), txt44.get(), txt45.get(), txt46.get(), txt47.get(), txt48.get(),
         txt49.get(), txt50.get(), txt51.get(), txt52.get(), txt53.get(), txt54.get(),
         txt55.get(), txt56.get(), txt57.get(), txt58.get(), txt59.get(), txt60.get(),
         txt61.get(), txt62.get(), txt63.get(), txt64.get(), txt65.get(), txt66.get(),
         txt67.get(), txt68.get(), txt69.get(), txt70.get(), txt71.get(), txt72.get(),
         txt73.get(), txt74.get(), txt75.get(), txt76.get(), txt77.get(), txt78.get(),
         txt79.get(), txt80.get(), txt81.get()]
    try:
        for i in range(len(lst)):
            lst[i]=int(lst[i])
    except ValueError:
        pass
    for i in sudoku:
        for j in i:
            lst1.append(j)
    if lst1 == lst:
        tmsg.showinfo("Sudoku", "You Won")
    else:
        tmsg.showwarning("OOPS!", "Try Again")
def fill_canvas(p):
    global txt1,txt2,txt3,txt4,txt5,txt6,txt7,txt8,txt9,txt10,txt11,txt12,txt13,txt14,txt15,txt16,txt17,txt18,txt19,txt20,txt21,txt22,txt23,txt24,txt25,txt26,txt27,txt28,txt29,txt30,txt31,txt32,txt33,txt34,txt35,txt36,txt37,txt38,txt39,txt40,txt41,txt42,txt43,txt44,txt45,txt46,txt47,txt48,txt49,txt50,txt51,txt52,txt53,txt54,txt55,txt56,txt57,txt58,txt59,txt60,txt61,txt62,txt63,txt64,txt65,txt66,txt67,txt68,txt69,txt70,txt71,txt72,txt73,txt74,txt75,txt76,txt77,txt78,txt79,txt80,txt81
    txt1 = Entry(root, width=2, font="Times 21", justify="center")
    txt2 = Entry(root, width=2, font="Times 21", justify="center")
    txt3 = Entry(root, width=2, font="Times 21", justify="center")
    txt4 = Entry(root, width=2, font="Times 21", justify="center")
    txt5 = Entry(root, width=2, font="Times 21", justify="center")
    txt6 = Entry(root, width=2, font="Times 21", justify="center")
    txt7 = Entry(root, width=2, font="Times 21", justify="center")
    txt8 = Entry(root, width=2, font="Times 21", justify="center")
    txt9 = Entry(root, width=2, font="Times 21", justify="center")
    txt10 = Entry(root, width=2, font="Times 21", justify="center")
    txt11 = Entry(root, width=2, font="Times 21", justify="center")
    txt12 = Entry(root, width=2, font="Times 21", justify="center")
    txt13 = Entry(root, width=2, font="Times 21", justify="center")
    txt14 = Entry(root, width=2, font="Times 21", justify="center")
    txt15 = Entry(root, width=2, font="Times 21", justify="center")
    txt16 = Entry(root, width=2, font="Times 21", justify="center")
    txt17 = Entry(root, width=2, font="Times 21", justify="center")
    txt18 = Entry(root, width=2, font="Times 21", justify="center")
    txt19 = Entry(root, width=2, font="Times 20", justify="center")
    txt20 = Entry(root, width=2, font="Times 20", justify="center")
    txt21 = Entry(root, width=2, font="Times 20", justify="center")
    txt22 = Entry(root, width=2, font="Times 20", justify="center")
    txt23 = Entry(root, width=2, font="Times 20", justify="center")
    txt24 = Entry(root, width=2, font="Times 20", justify="center")
    txt25 = Entry(root, width=2, font="Times 20", justify="center")
    txt26 = Entry(root, width=2, font="Times 20", justify="center")
    txt27 = Entry(root, width=2, font="Times 20", justify="center")
    txt28 = Entry(root, width=2, font="Times 21", justify="center")
    txt29 = Entry(root, width=2, font="Times 21", justify="center")
    txt30 = Entry(root, width=2, font="Times 21", justify="center")
    txt31 = Entry(root, width=2, font="Times 21", justify="center")
    txt32 = Entry(root, width=2, font="Times 21", justify="center")
    txt33 = Entry(root, width=2, font="Times 21", justify="center")
    txt34 = Entry(root, width=2, font="Times 21", justify="center")
    txt35 = Entry(root, width=2, font="Times 21", justify="center")
    txt36 = Entry(root, width=2, font="Times 21", justify="center")
    txt37 = Entry(root, width=2, font="Times 21", justify="center")
    txt38 = Entry(root, width=2, font="Times 21", justify="center")
    txt39 = Entry(root, width=2, font="Times 21", justify="center")
    txt40 = Entry(root, width=2, font="Times 21", justify="center")
    txt41 = Entry(root, width=2, font="Times 21", justify="center")
    txt42 = Entry(root, width=2, font="Times 21", justify="center")
    txt43 = Entry(root, width=2, font="Times 21", justify="center")
    txt44 = Entry(root, width=2, font="Times 21", justify="center")
    txt45 = Entry(root, width=2, font="Times 21", justify="center")
    txt46 = Entry(root, width=2, font="Times 20", justify="center")
    txt47 = Entry(root, width=2, font="Times 20", justify="center")
    txt48 = Entry(root, width=2, font="Times 20", justify="center")
    txt49 = Entry(root, width=2, font="Times 20", justify="center")
    txt50 = Entry(root, width=2, font="Times 20", justify="center")
    txt51 = Entry(root, width=2, font="Times 20", justify="center")
    txt52 = Entry(root, width=2, font="Times 20", justify="center")
    txt53 = Entry(root, width=2, font="Times 20", justify="center")
    txt54 = Entry(root, width=2, font="Times 20", justify="center")
    txt55 = Entry(root, width=2, font="Times 21", justify="center")
    txt56 = Entry(root, width=2, font="Times 21", justify="center")
    txt57 = Entry(root, width=2, font="Times 21", justify="center")
    txt58 = Entry(root, width=2, font="Times 21", justify="center")
    txt59 = Entry(root, width=2, font="Times 21", justify="center")
    txt60 = Entry(root, width=2, font="Times 21", justify="center")
    txt61 = Entry(root, width=2, font="Times 21", justify="center")
    txt62 = Entry(root, width=2, font="Times 21", justify="center")
    txt63 = Entry(root, width=2, font="Times 21", justify="center")
    txt64 = Entry(root, width=2, font="Times 21", justify="center")
    txt65 = Entry(root, width=2, font="Times 21", justify="center")
    txt66 = Entry(root, width=2, font="Times 21", justify="center")
    txt67 = Entry(root, width=2, font="Times 21", justify="center")
    txt68 = Entry(root, width=2, font="Times 21", justify="center")
    txt69 = Entry(root, width=2, font="Times 21", justify="center")
    txt70 = Entry(root, width=2, font="Times 21", justify="center")
    txt71 = Entry(root, width=2, font="Times 21", justify="center")
    txt72 = Entry(root, width=2, font="Times 21", justify="center")
    txt73 = Entry(root, width=2, font="Times 20", justify="center")
    txt74 = Entry(root, width=2, font="Times 20", justify="center")
    txt75 = Entry(root, width=2, font="Times 20", justify="center")
    txt76 = Entry(root, width=2, font="Times 20", justify="center")
    txt77 = Entry(root, width=2, font="Times 20", justify="center")
    txt78 = Entry(root, width=2, font="Times 20", justify="center")
    txt79 = Entry(root, width=2, font="Times 20", justify="center")
    txt80 = Entry(root, width=2, font="Times 20", justify="center")
    txt81 = Entry(root, width=2, font="Times 20", justify="center")

    txt1.insert(INSERT, p[0][0])
    txt2.insert(INSERT, p[0][1])
    txt3.insert(INSERT, p[0][2])
    txt4.insert(INSERT, p[0][3])
    txt5.insert(INSERT, p[0][4])
    txt6.insert(INSERT, p[0][5])
    txt7.insert(INSERT, p[0][6])
    txt8.insert(INSERT, p[0][7])
    txt9.insert(INSERT, p[0][8])
    txt10.insert(INSERT, p[1][0])
    txt11.insert(INSERT, p[1][1])
    txt12.insert(INSERT, p[1][2])
    txt13.insert(INSERT, p[1][3])
    txt14.insert(INSERT, p[1][4])
    txt15.insert(INSERT, p[1][5])
    txt16.insert(INSERT, p[1][6])
    txt17.insert(INSERT, p[1][7])
    txt18.insert(INSERT, p[1][8])
    txt19.insert(INSERT, p[2][0])
    txt20.insert(INSERT, p[2][1])
    txt21.insert(INSERT, p[2][2])
    txt22.insert(INSERT, p[2][3])
    txt23.insert(INSERT, p[2][4])
    txt24.insert(INSERT, p[2][5])
    txt25.insert(INSERT, p[2][6])
    txt26.insert(INSERT, p[2][7])
    txt27.insert(INSERT, p[2][8])
    txt28.insert(INSERT, p[3][0])
    txt29.insert(INSERT, p[3][1])
    txt30.insert(INSERT, p[3][2])
    txt31.insert(INSERT, p[3][3])
    txt32.insert(INSERT, p[3][4])
    txt33.insert(INSERT, p[3][5])
    txt34.insert(INSERT, p[3][6])
    txt35.insert(INSERT, p[3][7])
    txt36.insert(INSERT, p[3][8])
    txt37.insert(INSERT, p[4][0])
    txt38.insert(INSERT, p[4][1])
    txt39.insert(INSERT, p[4][2])
    txt40.insert(INSERT, p[4][3])
    txt41.insert(INSERT, p[4][4])
    txt42.insert(INSERT, p[4][5])
    txt43.insert(INSERT, p[4][6])
    txt44.insert(INSERT, p[4][7])
    txt45.insert(INSERT, p[4][8])
    txt46.insert(INSERT, p[5][0])
    txt47.insert(INSERT, p[5][1])
    txt48.insert(INSERT, p[5][2])
    txt49.insert(INSERT, p[5][3])
    txt50.insert(INSERT, p[5][4])
    txt51.insert(INSERT, p[5][5])
    txt52.insert(INSERT, p[5][6])
    txt53.insert(INSERT, p[5][7])
    txt54.insert(INSERT, p[5][8])
    txt55.insert(INSERT, p[6][0])
    txt56.insert(INSERT, p[6][1])
    txt57.insert(INSERT, p[6][2])
    txt58.insert(INSERT, p[6][3])
    txt59.insert(INSERT, p[6][4])
    txt60.insert(INSERT, p[6][5])
    txt61.insert(INSERT, p[6][6])
    txt62.insert(INSERT, p[6][7])
    txt63.insert(INSERT, p[6][8])
    txt64.insert(INSERT, p[7][0])
    txt65.insert(INSERT, p[7][1])
    txt66.insert(INSERT, p[7][2])
    txt67.insert(INSERT, p[7][3])
    txt68.insert(INSERT, p[7][4])
    txt69.insert(INSERT, p[7][5])
    txt70.insert(INSERT, p[7][6])
    txt71.insert(INSERT, p[7][7])
    txt72.insert(INSERT, p[7][8])
    txt73.insert(INSERT, p[8][0])
    txt74.insert(INSERT, p[8][1])
    txt75.insert(INSERT, p[8][2])
    txt76.insert(INSERT, p[8][3])
    txt77.insert(INSERT, p[8][4])
    txt78.insert(INSERT, p[8][5])
    txt79.insert(INSERT, p[8][6])
    txt80.insert(INSERT, p[8][7])
    txt81.insert(INSERT, p[8][8])
    

    btn = Button(root, width=10, text="Done!", font="Times 25 bold", bg="Yellow", command=clicked)
    
    txt1.place(x=24,y=83)
    txt2.place(x=64, y=83)
    txt3.place(x=104, y=83)
    txt4.place(x=144, y=83)
    txt5.place(x=184, y=83)
    txt6.place(x=224, y=83)
    txt7.place(x=264, y=83)
    txt8.place(x=304, y=83)
    txt9.place(x=344, y=83)
    txt10.place(x=24, y=123)
    txt11.place(x=64, y=123)
    txt12.place(x=104, y=123)
    txt13.place(x=144, y=123)
    txt14.place(x=184, y=123)
    txt15.place(x=224, y=123)
    txt16.place(x=264, y=123)
    txt17.place(x=304, y=123)
    txt18.place(x=344, y=123)
    txt19.place(x=24, y=163)
    txt20.place(x=64, y=163)
    txt21.place(x=104, y=163)
    txt22.place(x=144, y=163)
    txt23.place(x=184, y=163)
    txt24.place(x=224, y=163)
    txt25.place(x=264, y=163)
    txt26.place(x=304, y=163)
    txt27.place(x=344, y=163)
    txt28.place(x=24, y=203)
    txt29.place(x=64, y=203)
    txt30.place(x=104, y=203)
    txt31.place(x=144, y=203)
    txt32.place(x=184, y=203)
    txt33.place(x=224, y=203)
    txt34.place(x=264, y=203)
    txt35.place(x=304, y=203)
    txt36.place(x=344, y=203)
    txt37.place(x=24, y=243)
    txt38.place(x=64, y=243)
    txt39.place(x=104, y=243)
    txt40.place(x=144, y=243)
    txt41.place(x=184, y=243)
    txt42.place(x=224, y=243)
    txt43.place(x=264, y=243)
    txt44.place(x=304, y=243)
    txt45.place(x=344, y=243)
    txt46.place(x=24, y=283)
    txt47.place(x=64, y=283)
    txt48.place(x=104, y=283)
    txt49.place(x=144, y=283)
    txt50.place(x=184, y=283)
    txt51.place(x=224, y=283)
    txt52.place(x=264, y=283)
    txt53.place(x=304, y=283)
    txt54.place(x=344, y=283)
    txt55.place(x=24, y=323)
    txt56.place(x=64, y=323)
    txt57.place(x=104, y=323)
    txt58.place(x=144, y=323)
    txt59.place(x=184, y=323)
    txt60.place(x=224, y=323)
    txt61.place(x=264, y=323)
    txt62.place(x=304, y=323)
    txt63.place(x=344, y=323)
    txt64.place(x=24, y=363)
    txt65.place(x=64, y=363)
    txt66.place(x=104, y=363)
    txt67.place(x=144, y=363)
    txt68.place(x=184, y=363)
    txt69.place(x=224, y=363)
    txt70.place(x=264, y=363)
    txt71.place(x=304, y=363)
    txt72.place(x=344, y=363)
    txt73.place(x=24, y=403)
    txt74.place(x=64, y=403)
    txt75.place(x=104, y=403)
    txt76.place(x=144, y=403)
    txt77.place(x=184, y=403)
    txt78.place(x=224, y=403)
    txt79.place(x=264, y=403)
    txt80.place(x=304, y=403)
    txt81.place(x=344, y=403)

    btn.place(x=90, y=450)

def clicked2():
    fill_canvas(sudoku)
def clicked1():
    global sudoku
    sudoku = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    gen(sudoku)
    p = puzzle(sudoku)
    fill_canvas(p)
root.title("Sudoku")
root.geometry("405x550")
ico=PhotoImage(file="ab.PNG")
root.iconphoto(False,ico)
lbl = Label(root, text="Sudoku Puzzle",fg="red", font="Times 16 bold").pack()
canvas()
gen(sudoku)
p = puzzle(sudoku)
fill_canvas(p)
btn2 = Button(root, text="[Reset]", font="Times 12 bold", fg="Red", command=clicked1)
btn1 = Button(root, text="[Solution]", font="Times 12 bold", fg="Red", command=clicked2)
btn1.place(x=310, y=470)
btn2.place(x=20, y=470)
lbl1=Label(root,text="Developed by: Raj Pratap Singh").pack(side=RIGHT)
root.mainloop()
