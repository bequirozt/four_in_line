import numpy as np
import random
import itertools

class Game:

    def __init__(self, h = 6, w = 7):
        """
        Crea el tablero asignando el orden de juego

        parametros: 
            h, w --> dimenciones del tablero, alto y ancho
        """
        self.h = h
        self.w = w
        self.turn = random.randrange(-1,2,2)
        self.board = np.zeros(shape = (h,w))
        self.cache = np.ones(shape = (w,), dtype=np.int8)*(h-1)

    def insert(self, c = None):
        """
        Inserta la ficha en la columna asignada en la primera posición vacia 
        en la columna, si la jugada es ganadora activa la bandera "winner"

        parametros:
            c --> columna a la que se desea asignar el punto
        """
        if c == None or c < 1 or c > self.w:
            return
        if self.cache[c-1] < 0:
            return
        c -= 1
        self.board[self.cache[c],c] = self.turn
        if self.check(self.cache[c], c, self.turn):
            return True
        self.turn *= -1
        self.cache[c] -= 1
        return False

    def check(self, r, c, turn):
        """
        Determina si una jugada es ganadora
        
        parametros:
            r, c --> fila y columna en la que se encuentra la jugada actual
            turn --> turno actual
        """
        score_row = 0
        score_col = 0
        score_down_up = 0
        score_up_down = 0
        
        row = self.board[r,max(c-3,0):min(c+4,self.w)]
        col = self.board[max(0,r-3):min(r+4,self.h),c]
        up_left = [self.board[i,j] for (i, j) in zip(
            range(r-1,max(0,r-3)-1,-1),range(c-1,max(0,c-3)-1,-1))]
        down_lef = [self.board[i,j] for (i, j) in zip(
            range(r+1,min(self.h,r+3+1)),range(c-1,max(0,c-3)-1,-1))]
        up_right  = [self.board[i,j] for (i, j) in zip(
            range(r,max(0,r-3)-1,-1),range(c,min(self.w,c+3+1)))]
        down_right = [self.board[i,j] for (i, j) in zip(
            range(r,min(self.h,r+3+1)),range(c,min(self.w,c+3+1)))]
        up_down = np.concatenate((np.array(up_left),np.array(down_right)))
        down_up = np.concatenate((np.array(down_lef),np.array(up_right)))

        for r_,c_,u_d,d_u in itertools.zip_longest(row, col, up_down, down_up):
            if r_ != None:
                if r_ == self.turn:
                    score_row += 1
                    if score_row == 4:
                        return True
                else:
                    score_row = 0
            if c_ != None:
                if c_ == self.turn:
                    score_col += 1
                    if score_col == 4:
                        return True
                else:
                    score_col= 0
            if u_d != None:
                if u_d == self.turn:
                    score_up_down += 1
                    if score_up_down == 4:
                        return True
                else:
                    score_up_down = 0
            if d_u != None:
                if d_u == self.turn:
                    score_down_up += 1
                    if score_down_up == 4:
                        return True
                else:
                    score_down_up = 0
        return False

four_in_line = Game()

while True:
    c = int(input("Escriba su jugada: "))
    print(four_in_line.board)
    if four_in_line.insert(c): 
        print("YOU WIN!!!")
        break
    
    
