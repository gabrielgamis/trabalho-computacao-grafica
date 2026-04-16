import glfw
from OpenGL.GL import *

def main():
    if not glfw.init():
        return

    window = glfw.create_window(800, 600, "Primitivas com Cores", None, None)

    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)

    while not glfw.window_should_close(window):
        glClearColor(0.1, 0.1, 0.1, 1.0)
        glClear(GL_COLOR_BUFFER_BIT)

        # 🔴 PONTO (vermelho)
        glPointSize(10)
        glColor3f(1.0, 0.0, 0.0)
        glBegin(GL_POINTS)
        glVertex2f(-0.7, 0.5)
        glEnd()

        # 🟢 LINHA (verde)
        glLineWidth(3)
        glColor3f(0.0, 1.0, 0.0)
        glBegin(GL_LINES)
        glVertex2f(-0.5, 0.0)
        glVertex2f(0.5, 0.0)
        glEnd()

        # 🔵 TRIÂNGULO (azul)
        glColor3f(0.0, 0.0, 1.0)
        glBegin(GL_TRIANGLES)
        glVertex2f(-0.2, -0.5)
        glVertex2f(0.2, -0.5)
        glVertex2f(0.0, 0.2)
        glEnd()

        # 🟡 QUADRADO (amarelo)
        glColor3f(1.0, 1.0, 0.0)
        glBegin(GL_QUADS)
        glVertex2f(0.5, 0.5)
        glVertex2f(0.8, 0.5)
        glVertex2f(0.8, 0.2)
        glVertex2f(0.5, 0.2)
        glEnd()

        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()