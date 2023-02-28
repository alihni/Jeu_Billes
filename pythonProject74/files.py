class Pos2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return other.x == self.x and other.y == self.y


class Box:
    def __init__(self, bas_gauche_x, bas_gauche_y, haut_droite_x, haut_droite_y,
                 bas_droite_x, bas_droite_y, haut_gauche_x, haut_gauche_y, long, larg):
        self.long = long
        self.larg = larg
        self.bas_gauche = Pos2D(bas_gauche_x, bas_gauche_y)
        self.bas_droite = Pos2D(bas_droite_x, bas_droite_y)
        self.haut_gauche = Pos2D(haut_gauche_x, haut_gauche_y)
        self.haut_droite = Pos2D(haut_droite_x, haut_droite_y)


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
        self.grille = [[Node(j, i) for j in range(width)] for i in range(height)]
        # self.grille = [[[True, (i, j)] for j in range(height)] for i in range(width)]
        for v in range(height - 1):
            self.grille[0][v].Left = False
            self.grille[width - 1][v].Right = False

        for h in range(width - 1):
            self.grille[h][0].Down = False
            self.grille[h][height - 1].Up = False

    def add_wall(self, pos1, pos2):
        if pos1.x - pos2.x == 1:
            self.grille[pos1.x][pos1.y].Right = False
            self.grille[pos2.x][pos2.y].Left = False
        elif pos1.x - pos2.x == -1:
            self.grille[pos1.x][pos1.y].Left = False
            self.grille[pos2.x][pos2.y].Right = False
        elif pos1.y - pos2.y == 1:
            self.grille[pos1.x][pos2.y].Up = False
            self.grille[pos1.x][pos1.y].Down = False
        elif pos1.y - pos2.y == -1:
            self.grille[pos1.x][pos1.y].Up = False
            self.grille[pos1.x][pos2.y].Down = False

    def remove_wall(self, pos1, pos2):
        if pos1.x - pos2.x == 1:
            self.grille[pos1.x][pos1.y].Right = True
            self.grille[pos2.x][pos2.y].Left = True
        elif pos1.x - pos2.x == -1:
            self.grille[pos1.x][pos1.y].Left = True
            self.grille[pos2.x][pos2.y].Right = True
        elif pos1.y - pos2.y == 1:
            self.grille[pos1.x][pos2.y].Up = True
            self.grille[pos1.x][pos1.y].Down = True
        elif pos1.y - pos2.y == -1:
            self.grille[pos1.x][pos1.y].Up = True
            self.grille[pos1.x][pos2.y].Down = True

    def isolate_box(self, box):
        for i in range(box.bas_gauchex, box.haut_droitex + 1):
            for j in range(box.bas_gauchey, box.haut_droitey + 1):
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
        if pos.x - 1 >= 0:
            pos_gauche = Pos2D(pos.x - 1, pos.y)
            voisins.append(pos_gauche)
        if pos.x + 1 < self.width:
            pos_droite = Pos2D(pos.x + 1, pos.y)
            voisins.append(pos_droite)
        if pos.y - 1 >= 0:
            pos_haut = Pos2D(pos.x, pos.y - 1)
            voisins.append(pos_haut)
        if pos.y + 1 < self.height:
            pos_bas = Pos2D(pos.x, pos.y + 1)
            voisins.append(pos_bas)

        return voisins


class GridRenderer:
    def __init__(self, grid):
        self.grid = grid
        self.grid.haut_gauche = "┌"
        self.grid.bas_gauche = "└"
        self.grid.bas_droite = "┘"
        self.grid.haut_droite = "┐"

        self.grid.vertical_droite = "│"
        self.grid.vertical_gauche = "│"
        self.grid.horizontal = "─"

    def show(self):
        print(self.grid.haut_gauche + self.grid.horizontal * self.grid.width + self.grid.haut_droite)
        for y in range(self.grid.height):
            gauche = self.grid.vertical_gauche
            print(gauche + " " * self.grid.width + self.grid.vertical_droite)

        print(self.grid.bas_gauche + self.grid.horizontal * self.grid.width + self.grid.bas_droite)


B = Grid(8, 8)
C = GridRenderer(B)
C.show()
