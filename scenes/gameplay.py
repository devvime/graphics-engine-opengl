from core.model import *
import glm

from entities.player.player import Player

class GamePlay:
    def __init__(self, app):
        self.app = app
        self.objects = []
        self.load()
        self.skybox = AdvancedSkyBox(app)

    def add_object(self, obj):
        self.objects.append(obj)

    def load(self):
        app = self.app
        add = self.add_object

        # floor
        add(Cube(app, pos=(0, -2, 0), scale=(20, 1, 20)))

        # cat
        add(Cat(app, pos=(0, -1, -10)))
        
        #player
        add(Player(app, pos=(0, 0, 0)))

        # moving cube
        self.moving_cube = MovingCube(app, pos=(0, 6, 8), scale=(3, 3, 3), tex_id=1)
        add(self.moving_cube)

    def update(self):
        self.moving_cube.rot.xyz = self.app.time
