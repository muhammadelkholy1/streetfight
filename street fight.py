from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
width, height = 600, 400

x_pos = 0
y_pos = -30  # Set y_pos to -30 to move the character below the health bar
punching_arms = False
punching_legs = False
# Health bars
health1 = 150
health2 = 150

def draw_health_bars():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, width, 0, height)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    # Draw health bar 1 on top left
    glColor3f(1.0, 0.0, 0.0)  # Red color
    glBegin(GL_QUADS)
    glVertex2f(10, height - 30)
    glVertex2f(health1 + 10, height - 30)
    glVertex2f(health1 + 10, height - 10)
    glVertex2f(10, height - 10)
    glEnd()

    # Draw health bar 2 on top right
   
    glColor3f(0.0, 1.0, 0.0)  # Green color
    glBegin(GL_QUADS)
    glVertex2f(width - health2 - 10, height - 30)
    glVertex2f(width - 10, height - 30)
    glVertex2f(width - 10, height - 10)
    glVertex2f(width - health2 - 10, height - 10)
    glEnd()
    """"
    if health2 <= 0:
        glColor3f(0.0, 1.0, 0.0)  # Green color
        glRasterPos2f(width/2 - 40, height/2)
        glutBitmapString(//GLUT_BITMAP_TIMES_ROMAN_24//, "I win")
    """
      
def draw_character_1():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, width, 0, height)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    global x_pos, y_pos, punching_arms, punching_legs

    # Draw head
    glColor3f(1.0, 0.8, 0.6)  # Skin color
    glBegin(GL_POLYGON)
    glVertex2f(200 + x_pos, 350 + y_pos)
    glVertex2f(250 + x_pos, 400 + y_pos)
    glVertex2f(300 + x_pos, 380 + y_pos)
    glVertex2f(350 + x_pos, 350 + y_pos)
    glVertex2f(300 + x_pos, 320 + y_pos)
    glVertex2f(250 + x_pos, 300 + y_pos)
    glEnd()

    # Draw body
    glColor3f(0.0, 0.0, 1.0)  # Blue color
    glBegin(GL_POLYGON)
    glVertex2f(250 + x_pos, 300 + y_pos)
    glVertex2f(300 + x_pos, 320 + y_pos)
    glVertex2f(300 + x_pos, 200 + y_pos)
    glVertex2f(250 + x_pos, 180 + y_pos)
    glEnd()

    # Draw arms
    if punching_arms:
        glColor3f(1.0, 0.0, 0.0)  # Red color when punching
    else:
        glColor3f(1.0, 1.0, 0.0)  # Yellow color
    glBegin(GL_POLYGON)
    glVertex2f(250 + x_pos, 300 + y_pos)
    glVertex2f(200 + x_pos, 280 + y_pos)
    glVertex2f(180 + x_pos, 250 + y_pos)
    glVertex2f(200 + x_pos, 220 + y_pos)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(300 + x_pos, 320 + y_pos)
    glVertex2f(350 + x_pos, 340 + y_pos)
    glVertex2f(370 + x_pos, 310 + y_pos)
    glVertex2f(350 + x_pos, 280 + y_pos)
    glEnd()

    # Draw legs
    if punching_legs:
        glColor3f(1.0, 0.5, 0.0)  # Orange color when punching
    else:
        glColor3f(0.0, 1.0, 0.0)  # Green color
    glBegin(GL_POLYGON)
    glVertex2f(250 + x_pos, 180 + y_pos)
    glVertex2f(300 + x_pos, 200 + y_pos)
    glVertex2f(320 + x_pos, 150 + y_pos)
    glVertex2f(280 + x_pos, 130 + y_pos)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(300 + x_pos, 200 + y_pos)
    glVertex2f(250 + x_pos, 180 + y_pos)
    glVertex2f(220 + x_pos, 120 + y_pos)
    glVertex2f(240 + x_pos, 100 + y_pos)
    glEnd()
    
    
    
    
def draw_character_2():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, width, 0, height)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    global x_pos, y_pos, punching_arms, punching_legs

    # Draw head
    glColor3f(1.0, 0.8, 0.6)  # Skin color
    glBegin(GL_POLYGON)
    glVertex2f(width - (200 + x_pos), 350 + y_pos)
    glVertex2f(width - (250 + x_pos), 400 + y_pos)
    glVertex2f(width - (300 + x_pos), 380 + y_pos)
    glVertex2f(width - (350 + x_pos), 350 + y_pos)
    glVertex2f(width - (300 + x_pos), 320 + y_pos)
    glVertex2f(width - (250 + x_pos), 300 + y_pos)
    glEnd()

    # Draw body
    glColor3f(0.0, 0.0, 1.0)  # Blue color
    glBegin(GL_POLYGON)
    glVertex2f(width - (250 + x_pos), 300 + y_pos)
    glVertex2f(width - (300 + x_pos), 320 + y_pos)
    glVertex2f(width - (300 + x_pos), 200 + y_pos)
    glVertex2f(width - (250 + x_pos), 180 + y_pos)
    glEnd()

    # Draw arms
    if punching_arms:
        glColor3f(1.0, 0.0, 0.0)  # Red color when punching
    else:
        glColor3f(1.0, 1.0, 0.0)  # Yellow color
    glBegin(GL_POLYGON)
    glVertex2f(width - (250 + x_pos), 300 + y_pos)
    glVertex2f(width - (200 + x_pos), 280 + y_pos)
    glVertex2f(width - (180 + x_pos), 250 + y_pos)
    glVertex2f(width - (200 + x_pos), 220 + y_pos)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(width - (300 + x_pos), 320 + y_pos)
    glVertex2f(width - (350 + x_pos), 340 + y_pos)
    glVertex2f(width - (370 + x_pos), 310 + y_pos)
    glVertex2f(width - (350 + x_pos), 280 + y_pos)
    glEnd()

    # Draw legs
    if punching_legs:
        glColor3f(1.0, 0.5, 0.0)  # Orange color when punching
    else:
        glColor3f(0.0, 1.0, 0.0)  # Green color
    glBegin(GL_POLYGON)
    glVertex2f(width - (250 + x_pos), 180 + y_pos)
    glVertex2f(width - (300 + x_pos), 200 + y_pos)
    glVertex2f(width - (320 + x_pos), 150 + y_pos)
    glVertex2f(width - (280 + x_pos), 130 + y_pos)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(width - (300 + x_pos), 200 + y_pos)
    glVertex2f(width - (250 + x_pos), 180 + y_pos)
    glVertex2f(width - (220 + x_pos), 120 + y_pos)
    glVertex2f(width - (240 + x_pos), 100 + y_pos)
    glEnd()    

def keyboard(key, x, y):
    global x_pos, y_pos, punching_arms, punching_legs,health1,health2
    if key == b'w':
        y_pos += 5
    elif key == b's':
        y_pos -= 5
    elif key == b'd':
        x_pos += 5
    elif key == b'a':
        x_pos -= 5
    elif key == b'p':
        punching_arms = True
        if abs(x_pos - x_pos) < 50 and abs(y_pos - y_pos) < 50:
            health2 -= 7  
    elif key == b'o':
        punching_legs = True
        if abs(x_pos - x_pos) < 50 and abs(y_pos - y_pos) < 50:
            health2 -= 7  
            
def keyboard_up(key, x, y):
    global punching_arms, punching_legs ,health1 , health2
    if key == b'p':
        punching_arms = False
    elif key == b'o':
        punching_legs = False

def keyboard(key, x, y):
    global x_pos, y_pos, punching_arms, punching_legs,health1,health2
    if key == b'w':
        y_pos += 5
    elif key == b's':
        y_pos -= 5
    elif key == b'd':
        x_pos += 5
    elif key == b'a':
        x_pos -= 5
    elif key == b'p':
        punching_arms = True
        if abs(x_pos - x_pos) < 50 and abs(y_pos - y_pos) < 50:
            health2 -= 5  
    elif key == b'o':
        punching_legs = True
        if abs(x_pos - x_pos) < 50 and abs(y_pos - y_pos) < 50:
            health2 -= 5 
             
def keyboard_up(key, x, y):
    global punching_arms, punching_legs ,health1 , health2
    if key == b'p':
        punching_arms = False
    elif key == GLUT_KEY_LEFT:
        moving_left = False
    elif key == GLUT_KEY_RIGHT:
        moving_right = False 
    elif key == b'o':
        punching_legs = False
        
    elif key == GLUT_KEY_LEFT:
        moving_left = False
    elif key == GLUT_KEY_RIGHT:
        moving_right = False 
def display():
    glClearColor(1, 1, 1, 1)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    draw_health_bars()
    draw_character_1()
    draw_character_2()

    glutSwapBuffers()

def idle():
    global x_pos ,punching_arms,punching_legs
    if punching_arms:
        x_pos += 1
        
        if x_pos >= 5:
            punching_arms = 0.1
            x_pos = 1    
    if punching_legs:
        x_pos += 1
        
        if x_pos >= 5:
            punching_legs = 0.1
            x_pos = 1        
   
   
    glutPostRedisplay() 

glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
glutInitWindowSize(width, height)
glutCreateWindow("Fighting Character")
glutDisplayFunc(display)
glutIdleFunc(idle)
glutKeyboardFunc(keyboard)
glutKeyboardUpFunc(keyboard_up)
glutMainLoop()