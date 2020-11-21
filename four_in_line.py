import numpy as np
import random

class Game:

    def __init__(self, h = 6, w = 7):
        self.h = h
        self.w = w
        self.turn = random.randrange(-1,2,2)
        self.board = np.zeros(shape = (h,w))
        self.cache = np.ones(shape = (w,), dtype=np.int8)*(h-1)

    def insert(self, c = None):
        if c == None or c < 1 or c > self.w:
            return
        if self.cache[c-1] < 0:
            return
        c -= 1
        self.board[self.cache[c],c] = self.turn
        self.check(self.cache[c], c, self.turn)
        self.turn *= -1
        self.cache[c] -= 1

    def check(self, r, c, turn):
        score_row = 0
        score_col = 0
        score_down_up = 0
        score_up_down = 0
        
        row = self.board[r,max(c-3,0):min(c+4,self.w)]
        col = self.board[max(0,r-3):min(r+4,self.h),c]

        # for i in range(1,4):
        #     if c-i > -1 and self.board[r,c-i] == turn:
        #         score_col += 1
        #     else: break
        #         # if r-i > -1 and self.board[r-i,c-i] == turn:
        #         #     score_down_up += 1 
        # for i in range(1,4):
        #     if c+i < self.w and self.board[r,c+i] == turn:
        #         score_col += 1
        #     else: break
        #         # if r+i < self.h and self.board[r+i,c+i] == turn:
        #         #     score_down_up += 1
        # for i in range(1,4):
        #     if r-i > -1 and self.board[r-i,c] == turn:
        #         score_row += 1
        #     else: break
        #         # if c+i < self.w and self.board[r-i,c+i] == turn:
        #         #     score_up_down += 1
        # for i in range(1,4):
        #     if r+i < self.h and self.board[r+i,c] == turn:
        #         score_row += 1
        #     else:break
                # if c-i > -1 and self.board[r+i,c-i] == turn:
                #     score_up_down += 1
        # print(score_row,score_col,score_down_up,score_up_down) 


four_in_line = Game()

while True:
    c = int(input("Escriba su jugada: "))
    four_in_line.insert(c)
    print(four_in_line.board)
