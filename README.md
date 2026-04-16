# Trabalho Avaliativo Computação Gráfica

🖥️ Explorando o Universo Gráfico com OpenGL: Uma Introdução Prática
📌 Atividade Avaliativa P1
👨‍🎓 Autor(es)

Gabriel Gamis
(adicione outros integrantes se tiver grupo)

🎯 Objetivo Geral

Introduzir os conceitos básicos da computação gráfica e a utilização da biblioteca OpenGL para a criação de aplicações visuais interativas.

🎯 Objetivos Específicos
Compreender a arquitetura básica de um pipeline gráfico
Apresentar funções do OpenGL para desenho de primitivas geométricas
Demonstrar o uso de cores
Aplicar transformações geométricas (translação, rotação e escala)
Implementar exemplos práticos
📚 1. Introdução ao OpenGL e Configuração do Ambiente
🧠 O que é OpenGL

O OpenGL (Open Graphics Library) é uma API gráfica utilizada para desenvolvimento de aplicações que envolvem computação gráfica 2D e 3D. Ele permite a comunicação entre o software e a GPU (placa de vídeo).

🕰️ Breve história

Criado pela Silicon Graphics nos anos 90, o OpenGL se tornou um dos padrões da indústria para gráficos, sendo utilizado em jogos, simulações e aplicações científicas.

⚙️ O que é uma API gráfica

Uma API gráfica é um conjunto de funções que permite ao programador interagir com o hardware gráfico sem precisar lidar diretamente com o baixo nível da GPU.

🛠️ Configuração do ambiente
Requisitos:
Python instalado
Bibliotecas:
glfw
PyOpenGL
PyOpenGL-accelerate
Instalação:
pip install -r requirements.txt
💻 Exemplo prático: criação de janela

Arquivo: codigo1.py

✔️ Funcionalidade:
Inicializa o GLFW
Cria uma janela
Executa o loop principal
Limpa a tela
🔺 2. Desenhando as Primeiras Formas Geométricas
🧩 Conceitos
Vértices: pontos no espaço
Primitivas:
GL_POINTS → ponto
GL_LINES → linha
GL_TRIANGLES → triângulo
🔧 Funções principais
glBegin() e glEnd() → delimitam o desenho
glVertex*() → define os vértices
💻 Exemplo prático

Arquivo: codigo2.py

✔️ Funcionalidade:
Desenha:
Um ponto
Uma linha
Um triângulo
🎨 3. Cores no OpenGL
🌈 Sistema de cores

O OpenGL utiliza o sistema RGBA:

R (Red) → vermelho
G (Green) → verde
B (Blue) → azul
A (Alpha) → transparência

Valores variam de 0.0 a 1.0

🔧 Função utilizada
glColor3f(r, g, b)
💻 Exemplo prático

Arquivo: codigo3.py

✔️ Funcionalidade:
Aplica cores diferentes nas primitivas
Adiciona um quadrado
Trabalha com cores por objeto
🔄 4. Transformações Geométricas
🧠 Conceito Model-View

As transformações permitem manipular objetos na cena, alterando posição, rotação e escala.

🔧 Funções utilizadas
glTranslatef() → translação
glRotatef() → rotação
glScalef() → escala
⚠️ Ordem das transformações

A ordem influencia diretamente no resultado final da renderização.

💻 Exemplo prático

Arquivo: codigo4.py

✔️ Funcionalidade:
Aplica translação
Aplica rotação contínua (animação)
Aplica escala
Renderiza um triângulo animado
🧪 Metodologia
Desenvolvimento em Python
Utilização da biblioteca OpenGL
Implementação de exemplos progressivos
Testes realizados localmente
📂 Estrutura do Projeto
projeto-opengl/
│
├── codigo1.py
├── codigo2.py
├── codigo3.py
├── codigo4.py
├── requirements.txt
├── README.md
🎥 Vídeo de Demonstração

🔗 Link: https://drive.google.com/file/d/1z9YWw5tNtNma5KP3I6IEKilOIwSnd5-v/view?usp=sharing

☁️ Código na Nuvem

🔗 Link: https://github.com/gabrielgamis/trabalho-computacao-grafica
