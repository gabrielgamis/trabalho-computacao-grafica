import glfw
from OpenGL.GL import *
import math

def main():
    if not glfw.init():
        return

    window = glfw.create_window(800, 600, "Transformações", None, None)

    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)

    angle = 0.0

    while not glfw.window_should_close(window):
        glClearColor(0.1, 0.1, 0.1, 1.0)
        glClear(GL_COLOR_BUFFER_BIT)

        glLoadIdentity()

        # 🔁 TRANSFORMAÇÕES
        glTranslatef(0.3, 0.0, 0.0)   # move para direita
        glRotatef(angle, 0, 0, 1)     # gira no eixo Z
        glScalef(0.5, 0.5, 1.0)       # diminui tamanho

        # 🔺 TRIÂNGULO
        glBegin(GL_TRIANGLES)

        glColor3f(1.0, 0.0, 0.0)
        glVertex2f(-0.5, -0.5)

        glColor3f(0.0, 1.0, 0.0)
        glVertex2f(0.5, -0.5)

        glColor3f(0.0, 0.0, 1.0)
        glVertex2f(0.0, 0.5)

        glEnd()

        angle += 0.5  # animação (rotação contínua)

        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()