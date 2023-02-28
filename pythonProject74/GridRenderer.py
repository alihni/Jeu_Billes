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