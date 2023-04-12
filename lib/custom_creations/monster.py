class Monster:
    def __init__(self, name, picture_path=None, center=None, hp=None, level=None, inventory=None):
        self.name = name
        self.picture_path=picture_path
        self.center = center
        self.hp = hp
        self.level = level
        self.inventory = inventory
    