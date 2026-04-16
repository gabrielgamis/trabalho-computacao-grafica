import glfw
from OpenGL.GL import *

def main():
    if not glfw.init():
        return

    window = glfw.create_window(800, 600, "Primitivas OpenGL", None, None)

    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)

    while not glfw.window_should_close(window):
        # Cor de fundo
        glClearColor(0.1, 0.1, 0.1, 1.0)
        glClear(GL_COLOR_BUFFER_BIT)

        # -------------------
        # 🔴 PONTO
        # -------------------
        glPointSize(8)
        glBegin(GL_POINTS)
        glColor3f(1.0, 0.0, 0.0)  # vermelho
        glVertex2f(-0.5, 0.5)
        glEnd()

        # -------------------
        # 🟢 LINHA
        # -------------------
        glLineWidth(3)
        glBegin(GL_LINES)
        glColor3f(0.0, 1.0, 0.0)  # verde
        glVertex2f(-0.5, 0.0)
        glVertex2f(0.5, 0.0)
        glEnd()

        # -------------------
        # 🔵 TRIÂNGULO
        # -------------------
        glBegin(GL_TRIANGLES)
        glColor3f(0.0, 0.0, 1.0)  # azul
        glVertex2f(-0.2, -0.5)

        glColor3f(1.0, 1.0, 0.0)  # amarelo
        glVertex2f(0.2, -0.5)

        glColor3f(1.0, 0.0, 1.0)  # roxo
        glVertex2f(0.0, 0.2)
        glEnd()

        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()