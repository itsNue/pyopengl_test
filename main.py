from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def display1():
    glClear(GL_COLOR_BUFFER_BIT)
    #background1
    glBegin(GL_QUADS);
    glColor3f (0.0, 0.0, 0.1)
    glVertex2f(-10,500) 
    glVertex2f(1000, 500)
    glVertex2f (1000,340)
    glVertex2f (-10,340)
    glEnd()
    
    #background2
    glBegin(GL_QUADS);
    glColor3f (0.0, 0.4,0.1)
    glVertex2f (1000,340)
    glVertex2f(-10,340) 
    glVertex2f(1000, -10)
    glVertex2f (-10,-10)
    glEnd()
    
    #House
    #roof_back
    glBegin(GL_TRIANGLE_STRIP )
    glColor3f (0.6, 0.3, 0.21)
    glVertex2f(320, 200)
    glVertex2f(480, 200) 
    glVertex2f(400, 250)
    glEnd()
    
    
    #roof_2
    glBegin(GL_QUADS);
    glColor3f (0.6, 0.3, 0.21)
    glVertex2f(240, 250) 
    glVertex2f(400,  250)
    glVertex2f (400, 200)
    glVertex2f (240, 200)
    glEnd();
    #roof_front
    glBegin(GL_TRIANGLE_STRIP )
    glColor3f (0.6, 0.3, 0.25)
    glVertex2f(160, 200)
    glVertex2f(320, 200) 
    glVertex2f(240, 250)
    glEnd()
    #walls_1
    glBegin(GL_QUADS);
    glColor3f (0.9, 0.7, 0.3)
    glVertex2f(160, 200) 
    glVertex2f(320,  200)
    glVertex2f (320, 100)
    glVertex2f (160, 100)
    glEnd();
    #walls_2
    glBegin(GL_QUADS);
    glColor3f (0.9, 0.7, 0.21)
    glVertex2f(320, 200) 
    glVertex2f(480,  200)
    glVertex2f (480, 100)
    glVertex2f (320, 100)
    glEnd();
    #Door
    glBegin(GL_QUADS);
    glColor3f (0.7, 0.6, 0.15)
    glVertex2f(180,150) 
    glVertex2f(280, 150)
    glVertex2f (280,100)
    glVertex2f (180, 100)
    glEnd();
    
    glBegin(GL_LINES )
    glColor3f (0.9, 0.7, 0.3)
    glVertex2f(230, 100)
    glVertex2f(230, 150) 
    
    glEnd()

    #stars
    glBegin(GL_POINTS)
    glColor3f(1.0,1.0,0)
    glVertex2f(100,480)
    glVertex2f(10,375)
    glVertex2f(150,350)
    glVertex2f(70,385)
    glVertex2f(89,445)
    glVertex2f(220,420)
    glVertex2f(300,360)
    glVertex2f(350,460)
    glVertex2f(480,440)
    glVertex2f(500,410)
    glVertex2f(462,381)
    glVertex2f(350,369)
    glVertex2f(370,342)
    glVertex2f(389,489)
    glVertex2f(460,444)
    glVertex2f(442,404)
    glVertex2f(135,395)
    glVertex2f(325,400)
    glEnd()
    
    glutSolidSphere(1.15,250,250);  
    glFlush()
glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)   
glutInitWindowSize(500, 500)  
glutInitWindowPosition(100, 100)  
glutCreateWindow("My OpenGL Code")

glClearColor(0.0, 0.0, 0.0, 0.0) 
glColor3f(1.0, 1.0, 1.0)
glPointSize(5.0)
gluOrtho2D(0, 500, 0, 500)


glutDisplayFunc(display1) 
glutMainLoop()




