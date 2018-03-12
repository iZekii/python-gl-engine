from pyglet.gl import *


class Window(pyglet.window.Window):

    def __init__(self, width, height, title='', resizable=False):
        super(Window, self).__init__(width, height, title, resizable)

    @staticmethod
    def set_projection():
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()

    @staticmethod
    def set_model():
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

    def set3d(self):
        self.set_projection()
        fov, min_render_dist, max_render_dist = 70, 0.5, 10000
        aspect_ratio = self.width / self.height
        gluPerspective(fov, aspect_ratio, min_render_dist, max_render_dist)
        self.set_model()

    def set2d(self):
        pass  # Not needed quite yet

    def on_draw(self):
        self.clear()
        self.set3d()


if __name__ == '__main__':
    window = Window(400, 400, 'Hello World!', True)
    glClearColor(0.2, 0.5, 0.8, 1)

    pyglet.app.run()
