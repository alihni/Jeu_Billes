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

    def isolate_box(self, Box):
        Box.bas_gauche = False
        Box.bas_droite = False
        Box.haut_droite = False
        Box.haut_gauche = False
        Box.bas_gauchex = False
        Box.bas_gauchey = False
        Box.haut_droitex = False
        Box.haut_droitey = False
        for i in range(Box.larg):
            Box.larg[i] = False
        for j in range(Box.long):
            Box.long[j] = False

    def accessible_neighbours(self, pos):
        glob = []
        if pos.x - 1 <= self.width-1:
            pos_gauche = pos.x - 1
            glob.append(pos_gauche)
        if pos.x + 1 <= self.width-1:
            pos_droite = pos.x + 1
            glob.append(pos_droite)
        if pos.y + 1 <= self.height-1:
            pos_haut = pos.y + 1
            glob.append(pos_haut)
        if pos.y - 1 <= self.height-1:
            pos_bas = pos.y - 1
            glob.append(pos_bas)
        if pos.x - 1 <= self.width-1 and pos.y + 1 <= self.height-1:
            pos_haut_gauche = pos.x - 1, pos.y + 1
            glob.append(pos_haut_gauche)
        if pos.x + 1 <= self.width-1 and pos.y - 1 <= self.height-1:
            pos_haut_droite = pos.x + 1, pos.y - 1
            glob.append(pos_haut_droite)
        if pos.x - 1 <= self.width-1 and pos.y - 1 <= self.height-1:
            pos_bas_gauche = pos.x - 1, pos.y - 1
            glob.append(pos_bas_gauche)
        if pos.x + 1 <= self.width-1 and pos.y - 1 <= self.height-1:
            pos_bas_droite = pos.x + 1, pos.y - 1
            glob.append(pos_bas_droite)
        return glob
