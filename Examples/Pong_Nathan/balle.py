import pygame
from pygame import locals as const

class balletest:
    def __init__(self, pos):
        self.pos_x, self.pos_y = pos
        self.v_x = 2
        self.v_y = 2

    def mx(self):
        self.v_x = -self.v_x
    def my(self):
        self.v_y = -self.v_y
    def mouv(self):
        self.pos_x += self.v_x
        self.pos_y += self.v_y
    def reset(self, pos):
        self.pos_x, self.pos_y = pos