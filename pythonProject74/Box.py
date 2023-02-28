class Box:
    def __init__(self, bas_gauche_x, bas_gauche_y, haut_droite_x, haut_droite_y,
                 bas_droite_x, bas_droite_y, haut_gauche_x, haut_gauche_y, long, larg):
        self.long = long
        self.larg = larg
        self.bas_gauche = Pos2D(bas_gauche_x, bas_gauche_y)
        self.bas_droite = Pos2D(bas_droite_x, bas_droite_y)
        self.haut_gauche = Pos2D(haut_gauche_x, haut_gauche_y)
        self.haut_droite = Pos2D(haut_droite_x, haut_droite_y)