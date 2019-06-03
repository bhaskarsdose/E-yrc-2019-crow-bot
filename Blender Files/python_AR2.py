'''
Team Id : <974>
*Author List : <Akshay Sharma, Bhaskar dutt, Varun pandey>
*Filename: <python_AR.py>
*Theme: <Thristy Crow -- Specific to eYRC /eYRCPlus >
*Functions: <getCameraMatrix(), main(), (), init_gl(),
  resize(), drawGLScene(), detect_markers(), draw_background(),overlay()>
*Global Variables: <global variable are used in  our code named texture_object, texture_background, camera_matrix,
dist_coeff, matka_1, matka_2, matka_3, matka_4, Crow1, Crow2, Crow3, Crow4, pather_NO_6_TEX_1,pather_NO_5_TEX_1,
pather_NO_6_TEX_2, pather_NO_5_TEX_2,pather_NO_6_TEX_3,pather_NO_5_TEX_3, list_pebble
'''
import numpy as np
import cv2
import cv2.aruco as aruco
import math
import time
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from PIL import Image
import pygame
from objloader import *
import vari
texture_object = None
texture_background = None
camera_matrix = None
dist_coeff = None
videoSourceIndex = 0
cap = cv2.VideoCapture(cv2.CAP_DSHOW + videoSourceIndex)
matka_1 = None
matka_2 = None
matka_3=None
matka_4 = None
Crow1 = None
Crow2 = None
Crow3 = None
Crow4 = None
Crow_diffrent = None
pather_NO_6_TEX_1 = None
pather_NO_5_TEX_1 = None
pather_NO_6_TEX_2 = None
pather_NO_5_TEX_2 = None
pather_NO_6_TEX_3 = None
pather_NO_5_TEX_3 = None

INVERSE_MATRIX = np.array([[ 1.0, 1.0, 1.0, 1.0],
                           [-1.0,-1.0,-1.0,-1.0],
                           [-1.0,-1.0,-1.0,-1.0],
                           [ 1.0, 1.0, 1.0, 1.0]])
list_pebble =[]

################## Define Utility Functions Here #######################
"""
Function Name : getCameraMatrix()
Input: None
Output: camera_matrix, dist_coeff
Purpose: Loads the camera calibration file provided and returns the camera and
         distortion matrix saved in the calibration file.
"""
def getCameraMatrix():
        global camera_matrix, dist_coeff
        with np.load('Camera.npz') as X:
                camera_matrix, dist_coeff, _, _ = [X[i] for i in ('mtx','dist','rvecs','tvecs')]
########################################################################
############# Main Function and Initialisations ########################
"""
Function Name : main()
Input: None
Output: None
Purpose: Initialises OpenGL window and callback functions. Then starts the event
         processing loop.
"""
def main():
        glutInit()
        getCameraMatrix()
        glutInitWindowSize(640, 480)
        glutInitWindowPosition(625, 100)
        glutInitDisplayMode(GLUT_RGB | GLUT_DEPTH | GLUT_DOUBLE)
        window_id = glutCreateWindow("OpenGL")
        init_gl()
        glutDisplayFunc(drawGLScene)
        glutIdleFunc(drawGLScene)
        glutReshapeFunc(resize)
        glutMainLoop()
"""
Function Name : init_gl()
Input: None
Output: None
Purpose: Initialises various parameters related to OpenGL scene.
"""
def init_gl():
        global texture_object, texture_background
        global matka_1,matka_2,matka_3,matka_4,pather_NO_5_TEX_1,pather_NO_6_TEX_1,pather_NO_5_TEX_2,pather_NO_6_TEX_2,pather_NO_5_TEX_3,pather_NO_6_TEX_3,Crow1,Crow2,Crow3,Crow4,Crow_diffrent
        glClearColor(0.0, 0.0, 0.0, 0.0)
        glClearDepth(100.0)
        glDepthFunc(GL_LESS)
        glEnable(GL_DEPTH_TEST)
        glShadeModel(GL_SMOOTH)
        glMatrixMode(GL_MODELVIEW)
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        glEnable(GL_TEXTURE_2D)
        texture_background = glGenTextures(1)
        texture_object = glGenTextures(1)
        matka_1 = OBJ('matka_1.obj', swapyz=True)
        matka_2 = OBJ('matka_2.obj', swapyz=True)
        matka_3 = OBJ('matka_3.obj', swapyz=True)
        matka_4 = OBJ('matka_4.obj', swapyz=True)
        Crow_diffrent = OBJ('Crow_diffrent.obj', swapyz=True)
        Crow1 = OBJ('Crow1.obj', swapyz=True)
        Crow2 = OBJ('Crow2.obj', swapyz=True)
        Crow3 = OBJ('Crow3.obj', swapyz=True)
        Crow4 = OBJ('Crow4.obj', swapyz=True)
        pather_NO_5_TEX_1 = OBJ('pather_NO_5_TEX_1.obj', swapyz=True)
        pather_NO_6_TEX_1 = OBJ('pather_NO_6_TEX_1.obj', swapyz=True)
        pather_NO_5_TEX_2 = OBJ('pather_NO_5_TEX_2.obj', swapyz=True)
        pather_NO_6_TEX_2 = OBJ('pather_NO_6_TEX_2.obj', swapyz=True)
        pather_NO_5_TEX_3 = OBJ('pather_NO_5_TEX_3.obj', swapyz=True)
        pather_NO_6_TEX_3 = OBJ('pather_NO_6_TEX_3.obj', swapyz=True)

"""
Function Name : resize()
Input: None
Output: None
Purpose: Initialises the projection matrix of OpenGL scene
"""
def resize(w,h):
        ratio = 1.0* w / h
        glMatrixMode(GL_PROJECTION)
        glViewport(0,0,w,h)
        gluPerspective(45, ratio, 0.1, 100.0)
"""
Function Name : drawGLScene()
Input: None
Output: None
Purpose: It is the main callback function which is called again and
         again by the event processing loop. In this loop, the webcam frame
         is received and set as background for OpenGL scene. ArUco marker is
         detected in the webcam frame and 3D model is overlayed on the marker
         by calling the overlay() function.
"""

def drawGLScene():
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        ar_list = []
        flag_g = 0
        flag_b = 0
        flag_r = 0
        ret, frame = cap.read()
        thk0 = 0
        thk1 = 0
        thk2 = 0

        if ret == True:
                draw_background(frame)
                glMatrixMode(GL_MODELVIEW)
                glLoadIdentity()
                ar_list = detect_markers(frame)


                for i in ar_list:
                    for key in vari.pebble_id :
                        list_pebble.append (vari.pebble_id[key])


                    for key in vari.pitcher_id:
                        mtemp = vari.pitcher_id[key]

                    if i[0] ==list_pebble[0]:
                        if vari.id_list[list_pebble[0]] == 0 :
                            gl = pather_NO_6_TEX_1.gl_list #red
                        elif vari.id_list[list_pebble[0]]== 1:
                            gl = pather_NO_5_TEX_2.gl_list

                        overlay(frame, ar_list, i[0],gl)
                    if i[0] == list_pebble[1]:
                        if vari.id_list[list_pebble[1]] == 0 :
                            gl = pather_NO_6_TEX_2.gl_list #green
                        elif vari.id_list[list_pebble[1]]== 1:
                             gl = pather_NO_5_TEX_2.gl_list
                        overlay(frame, ar_list, i[0],gl)

                        overlay(frame, ar_list, i[0],gl)
                    if i[0] == mtemp:
                        if vari.id_list[mtemp] == 0:
                            magl =matka_1.gl_list
                        #elif vari.id_list[mtemp] == 1:
                        #    magl =matka_2.gl_list
                        elif vari.id_list[mtemp] ==1:
                            magl =matka_3.gl_list
                        else :
                            magl =matka_4.gl_list

                        overlay(frame, ar_list, i[0],magl)

                    if i[0] == 10:
                        local_list =[]
                        for akey in range(0,2):
                            local_list.append(vari.pebble_id[akey])
                        if vari.C_variable ==-2 :
                            cr =Crow_diffrent.gl_list
                        elif vari.C_variable == -3 :
                            cr =Crow1.gl_list
                        else  :
                            if vari.C_variable == local_list[1]:
                                 cr =Crow3.gl_list #red

                            elif  vari.C_variable == local_list[0]:
                                cr =Crow2.gl_list #green


                        overlay(frame, ar_list, i[0],cr)


                cv2.imshow('frame', frame)
                cv2.waitKey(1)
        glutSwapBuffers()

########################################################################
######################## Aruco Detection Function ######################
"""
Function Name : detect_markers()
Input: img (numpy array)
Output: aruco list in the form [(aruco_id_1, centre_1, rvec_1, tvec_1),(aruco_id_2,
        centre_2, rvec_2, tvec_2), ()....]
Purpose: This function takes the image in form of a numpy array, camera_matrix and
         distortion matrix as input and detects ArUco markers in the image. For each
         ArUco marker detected in image, paramters such as ID, centre coord, rvec
         and tvec are calculated and stored in a list in a prescribed format. The list
         is returned as output for the function
"""
def detect_markers(img):
    aruco_list = []
    markerLength = 100
    corners_list=[]
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    aruco_dict = aruco.Dictionary_get(aruco.DICT_5X5_250)
    parameters = aruco.DetectorParameters_create()
    corners, ids, _, = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)
    for cor in corners :
    	x = int((cor[0][0][0] + cor[0][1][0] + cor[0][2][0] + cor[0][3][0])/4)
    	y = int((cor[0][0][1] + cor[0][1][1] + cor[0][2][1] + cor[0][3][1])/4)
    	tupl = (x,y)
    	corners_list.append(tupl)
    rvec, tvec, _ = aruco.estimatePoseSingleMarkers(corners, markerLength, camera_matrix, dist_coeff)
    if rvec is not None:
        for id,corn,rv,tv in zip(ids,corners_list,rvec,tvec):
            tup = (int(id),corn,rv.reshape((-1,1,3)), tv.reshape((-1,1,3)))
            aruco_list.append(tup)

            aruco.drawDetectedMarkers(img,corners,ids)

    return aruco_list

"""
Function Name : draw_background()
Input: img (numpy array)
Output: None
Purpose: Takes image as input and converts it into an OpenGL texture. That
         OpenGL texture is then set as background of the OpenGL scene
"""
def draw_background(img):
    bg_image = cv2.flip(img, 0)
    bg_image = Image.fromarray(bg_image)
    ix = bg_image.size[0]
    iy = bg_image.size[1]
    bg_image = bg_image.tobytes("raw", "BGRX", 0, -1)
    glBindTexture(GL_TEXTURE_2D, texture_background)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexImage2D(GL_TEXTURE_2D, 0, 3, ix, iy, 0,GL_RGBA, GL_UNSIGNED_BYTE, bg_image)
    glBindTexture(GL_TEXTURE_2D, texture_background)
    glPushMatrix()
    glTranslatef(0.0,0.0,-7.0)
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 1.0); glVertex3f(-4.0, -3.0, 0.0)
    glTexCoord2f(1.0, 1.0); glVertex3f( 4.0, -3.0, 0.0)
    glTexCoord2f(1.0, 0.0); glVertex3f( 4.0,  3.0, 0.0)
    glTexCoord2f(0.0, 0.0); glVertex3f(-4.0,  3.0, 0.0)
    glEnd()
    glPopMatrix()
    return None
"""
Function Name : overlay()
Input: img (numpy array), aruco_list, aruco_id, glfunc(Name of Object to be overlayed on marker)
Output: None
Purpose: Receives the ArUco information as input and overlays the 3D Model of a crow , pebble , pitcher
         on the ArUco marker. That ArUco information is used to
         calculate the rotation matrix and subsequently the view matrix. Then that view matrix
         is loaded as current matrix and the 3D model is rendered using glCallList.

"""
def overlay(img, ar_list, ar_id,glfunc):
    for x in ar_list:
        if ar_id == x[0]:
            centre, rvec, tvec = x[1], x[2], x[3]

            rmtx = cv2.Rodrigues(rvec)[0]
            view_matrix = np.array([[rmtx[0][0],rmtx[0][1],rmtx[0][2],tvec[0][0][0]/300],
                                    [rmtx[1][0],rmtx[1][1],rmtx[1][2],tvec[0][0][1]/300],
                                    [rmtx[2][0],rmtx[2][1],rmtx[2][2],tvec[0][0][2]/300],
                                    [0.0 , 0.0, 0.0  ,1.0    ]])
            view_matrix = view_matrix * INVERSE_MATRIX
            view_matrix = np.transpose(view_matrix)

            glPushMatrix()
            glLoadMatrixd(view_matrix)
            #time.sleep(1)
            glCallList(glfunc)
            glPopMatrix()
