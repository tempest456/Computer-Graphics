from OpenGL.GL import * 
from OpenGL.GLU import * 
from OpenGL.GLUT import * 
from random import * 
from numpy import * 
import sys 
# Globals for window width and height 
global width 
global height 
# Initial values of width and height 
width = 500 
height = 500 
 
def init(): 
 
    # White background 
    glClearColor(1.0, 1.0, 1.0, 0.0) 
    
    # Set the projection matrix... our "view" 
    glMatrixMode(GL_PROJECTION) 
    glLoadIdentity() 
    
    # Set the plot window range 
    # This will coincide with the for... arange loops 
    gluOrtho2D(-30.0, 30.0, -30.0, 30.0) 
    
    # Set the matrix for the object we are drawing 
    glMatrixMode(GL_MODELVIEW) 
    glLoadIdentity() 
    
def plotlorenz(): 
    glClear(GL_COLOR_BUFFER_BIT) 
 
    # Initial values for x, y, and z 
    x = 0.50000 
    y = 0.50000 
    z = 0.50000 
    dt = 0.0005
    
    glColor3f(1.0,0.0,0.0) 
 
    for n in arange(-30,30, 0.0005): 
        x = x + (-10*x + 10*y)*dt 
        y = y + (28*x - y - x*z)*dt 
        z = z + (-2.66667*z + x*y)*dt 
    
        # Plot x versus y 
        glBegin(GL_POINTS) 
        glVertex2f(x, z)
        glEnd() 
        glFlush() 
        
def keyboard(key, x, y): 
    # Allows us to quit by pressing 'Esc' or 'q' 
    if key == chr(27): 
        sys.exit() 
    if key == "q": 
        sys.exit() 

def main(): 
    global width 
    global height 
    
    glutInit(sys.argv) 
    glutInitDisplayMode(GLUT_RGB|GLUT_SINGLE) 
    glutInitWindowPosition(100,100) 
    glutInitWindowSize(width,height) 
    glutCreateWindow("Lorenz2") 
    glutDisplayFunc(plotlorenz) 
    glutKeyboardFunc(keyboard) 
    
    init() 
    glutMainLoop()
    
main() 

