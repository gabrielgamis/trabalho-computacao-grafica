import glfw
from OpenGL.GL import *

def main():
    # Inicializa o GLFW
    if not glfw.init():
        return

    # Cria a janela
    window = glfw.create_window(800, 600, "Janela OpenGL", None, None)

    if not window:
        glfw.terminate()
        return

    # Define contexto OpenGL
    glfw.make_context_current(window)

    # Loop principal
    while not glfw.window_should_close(window):
        # Limpa a tela (preto)
        glClear(GL_COLOR_BUFFER_BIT)

        # Troca buffers
        glfw.swap_buffers(window)

        # Processa eventos (teclado/mouse)
        glfw.poll_events()

    # Finaliza
    glfw.terminate()

if __name__ == "__main__":
    main()