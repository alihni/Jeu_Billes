class Pos2D:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return other.x == self.x and other.y == self.y


class Box:
    def __init__(self, bas_gauchex, bas_gauchey, haut_droitex, haut_droitey,
                 bas_droitex, bas_droitey, haut_gauchex, haut_gauchey, long, larg):
        self.long = long
        self.larg = larg
        self.bas_gauche = Pos2D(bas_gauchex, bas_gauchey)
        self.bas_droite = Pos2D(bas_droitex, bas_droitey)
        self.haut_gauche = Pos2D(haut_gauchex, haut_gauchey)
        self.haut_droite = Pos2D(haut_droitex, haut_droitey)


        # self.bas_gauchex = bas_gauchex
        # self.bas_gauchey = bas_gauchey
        # self.haut_gauchex = haut_gauchex
        # self.haut_gauchey = haut_gauchey
        # self.bas_droitex = bas_droitex
        # self.bas_droitey = bas_droitey
        # self.haut_droitex = haut_droitex
        # self.haut_droitey = haut_droitey

    """def longueur(self):
        self.long = self.haut_gauchey - self.bas_droitey
        return self.long

    def largeur(self):
        self.larg = self.bas_droitex - self.haut_gauchex
        return self.larg"""

    """"
    def point_bas_droite(self):
        self.bas_droitex = self.haut_gauchex + (self.bas_droitex - self.haut_gauchex)
        self.bas_droitey = self.haut_gauchey - (self.bas_droitey - self.haut_gauchey)
        return self.bas_droitex and self.bas_droitey

    def point_haut_gauche(self):
        self.haut_gauchex = self.haut_gauchex + (self.bas_droitex - self.haut_gauchex)
        self.haut_gauchey = self.haut_gauchey + (self.bas_droitey - self.haut_gauchey)
        return self.haut_gauchex and self.haut_gauchey"""


class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.Up = True
        self.Down = True
        self.Left = True
        self.Right = True


class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grille = [[Node(j, i) for j in range(height)] for i in range(width)]
        # self.grille = [[[True, (i, j)] for j in range(height)] for i in range(width)]
        for v in range(height - 1):
            self.grille[0][v].Left = False
            self.grille[width - 1][v].Right = False

        for h in range(width - 1):
            self.grille[h][0].Down = False
            self.grille[h][height - 1].Up = False

    def add_wall(self, pos1, pos2):
        if pos1.x - pos2.x == 1:
            self.grille[pos1.x][pos2.y].Right = False
            self.grille[pos2.x][pos1.y].Left = False
        elif pos1.x - pos2.x == -1:
            self.grille[pos1.x][pos2.y].Left = False
            self.grille[pos2.x][pos1.y].Right = False
        elif pos1.y - pos2.y == 1:
            self.grille[pos1.x][pos1.y].Up = False
            self.grille[pos1.x][pos2.y].Down = False
        elif pos1.y - pos2.y == -1:
            self.grille[pos1.x][pos2.y].Up = False
            self.grille[pos1.x][pos1.y].Down = False

    def remove_wall(self, pos1, pos2):
        if pos1.x - pos2.x == 1:
            self.grille[pos1.x][pos2.y].Right = True
            self.grille[pos2.x][pos1.y].Left = True
        elif pos1.x - pos2.x == -1:
            self.grille[pos1.x][pos2.y].Left = True
            self.grille[pos2.x][pos1.y].Right = True
        elif pos1.y - pos2.y == 1:
            self.grille[pos1.x][pos1.y].Up = True
            self.grille[pos1.x][pos2.y].Down = True
        elif pos1.y - pos2.y == -1:
            self.grille[pos1.x][pos2.y].Up = True
            self.grille[pos1.x][pos1.y].Down = True

    def isolate_box(self, box):
        for i in range(box.bas_gauchex, box.haut_droitex):
            for j in range(box.bas_gauchey, box.haut_droitey):
                if (i, j) not in ((box.bas_gauchex, box.bas_gauchey),
                                  (box.haut_droitex, box.haut_droitey),
                                  (box.bas_droitex, box.bas_droitey),
                                  (box.haut_gauchex, box.haut_gauchey)):
                    self.grille[i][j].Up = False
                    self.grille[i][j].Down = False
                    self.grille[i][j].Left = False
                    self.grille[i][j].Right = False

    def accessible_neighbours(self, pos):
        voisins = []
        if pos.x - 1 <= self.width:
            pos_gauche = Pos2D(pos.x - 1, pos.y)
            voisins.append(pos_gauche)
        if pos.x + 1 <= self.width:
            pos_droite = Pos2D(pos.x + 1, pos.y)
            voisins.append(pos_droite)
        if pos.y + 1 <= self.height:
            pos_haut = Pos2D(pos.x, pos.y - 1)
            voisins.append(pos_haut)
        if pos.y - 1 <= self.height:
            pos_bas = Pos2D(pos.x, pos.y + 1)
            voisins.append(pos_bas)

        return voisins


class GridRenderer:
    def __init__(self, grid):
        self.grid = grid

    def show(self):
        self.grid.haut_gauche = "???"
        self.grid.bas_gauche = "???"
        self.grid.bas_droite = "???"
        self.grid.haut_gauche_droite = "???"
        self.grid.Left = "???"
        self.grid.Right = "???"
        self.grid.Down = "???"
        self.grid.Up = "???"

    # ???, ???, ???, ???, ???, ???, ???, ???, ???, ???, ???


B = Grid(4, 4)
C = GridRenderer(B)
C.show()
