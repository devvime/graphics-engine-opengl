from core.vao import VAO
from core.texture import Texture

class Mesh:
    def __init__(self, app):
        self.app = app
        self.vao = VAO(app.ctx)
        self.texture = Texture(app)

    def destroy(self):
        self.vao.destroy()
        self.texture.destroy()