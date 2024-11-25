class Gun:
    def __init__(self,name,ammo,lp):
        self.name = name
        self.ammo = ammo
        self.ammo = lp
    def add_ammo(self,ammo):
        self.ammo += ammo
    def fire_ammo(self,ammo):
        if self.ammo > 0:
            self.ammo -=1
        else:
            print("out of ammo")