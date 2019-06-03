'''
Team Id : <974>
*Author List : <Akshay Sharma, Bhaskar dutt, Varun pandey,deepanshu singh>
*Filename: <Main.py>
*Theme: <Thristy Crow -- Specific to eYRC /eYRCPlus >
*Functions: <drawGLScene(), axis direction(), startcondition(), dict_axis(), points(), main1()>
*Global Variables: <global variable used are Robot_start>
'''
from  Graph import *
from echo import *
import time
import vari
import threading

#this dictionary is used to store the coordinates of the pebble and water picther
arena_config ={0:("Water pitcher",15,"1-1") ,1:("Pebble",18,"3-3") ,4:("Pebble",9,"2-2"),5:("Pebble",6,"1-1")}

Robot_start = "Start-2"


#this dictionary stores the coordinates of the 1-1 axis of the graph
dict_1={1:[(4,1),(7,1)],2:[(2,2),(5,2)],3:[(4,3),(7,3)],4:[(6,2),(9,2)],5:[(0,3),(3,3)],
6:[(2,4),(5,4)],7:[(4,5),(7,5)],8:[(6,4),(9,4)],9:[(8,3),(11,3)],10:[(0,5),(3,5)],11:[(2,6),(5,6)],
12:[(4,7),(7,7)],13:[(6,6),(9,6)],14:[(8,5),(11,5)],15:[(0,7),(3,7)],16:[(2,8),(5,8)],17:[(4,9),(7,9)],
18:[(6,8),(9,8)],19:[(8,7),(11,7)]}

#this dictionary stores the coordinates of the 2-2 axis of the graph
dict_2={1:[(5,0),(6,2)],2:[(3,1),(4,3)],3:[(5,2),(6,4)],4:[(7,1),(8,3)],5:[(1,2),(2,4)],
6:[(3,3),(4,5)],7:[(5,4),(6,6)],8:[(7,3),(8,5)],9:[(9,2),(10,4)],10:[(1,4),(2,6)],11:[(3,5),(4,7)],
12:[(5,6),(6,8)],13:[(7,5),(8,7)],14:[(9,4),(10,6)],15:[(1,6),(2,8)],16:[(3,7),(4,9)],17:[(5,8),(6,10)],
18:[(7,7),(8,9)],19:[(9,6),(10,8)]}

#this dictionary stores the coordinates of the 3-3 axis of the graph
dict_3={1:[(6,0),(5,2)],2:[(4,1),(3,3)],3:[(6,2),(5,4)],4:[(8,1),(7,3)],5:[(2,2),(1,4)],
6:[(4,3),(3,2)],7:[(6,4),(5,6)],8:[(8,3),(7,5)],9:[(10,2),(9,4)],10:[(2,4),(1,6)],11:[(4,5),(3,7)],
12:[(6,6),(5,8)],13:[(8,5),(7,7)],14:[(10,4),(9,6)],15:[(2,6),(1,8)],16:[(4,7),(3,9)],17:[(6,8),(5,10)],
18:[(8,7),(7,9)],19:[(10,6),(9,8)]}

#this dictionary stores no of pebbles in each cell
#no_of_pebble ={0:1,1:1,2:1}
length_arena = len(arena_config)
print (length_arena)
if length_arena ==3 :
    from python_AR2 import *
elif length_arena ==4:
    from python_AR import *

no_of_pebble ={}
for key in range (0,len(arena_config)-1):
    no_of_pebble[key] = 1
# this dictionary contains the command as key and value as character that xbee module pass to the robot
command ={
'Left_Forward' : 'a',
'Right_Forward' :'d',
'Forward' :'w',
'Turn_180' :'y',
'Turn_Left_120':'x' ,
'Turn_Right_120':'c',
'Turn_Left_60':'g',
'Turn_Right_60':"f",
'Straight':'p'
}

left_turn = ["SENE","NWSW","NEW","SWE","WSE","ENW"]
right_turn = ["SEW","NWE","NESE","SWNW","WNE","ESW"]

finalRightdir ={
"NE":"SE",
"NW":"E",
"E":"SW",
"W":"NE",
"SW":"NW",
"SE":"W"
}
finalLeftdir ={
"NE":"W",
"NW":"SW",
"E":"NW",
"W":"SE",
"SW":"E",
"SE":"NE"
}
'''
*Function Name: <turncalculator()>
*Input: <facing_dir, dir_to_face>
*Output: <returns the axis_align_dir variable >
*Logic: < It calculates the pickup and drop turns needed for the bot to allign with desired marker axis.>
'''

def turncalculator(facing_dir , dir_to_face):
    dir =facing_dir + dir_to_face
    if dir in left_turn :
        axis_align_dir = [["Turn_Left_120"]]
    elif dir in right_turn:
        axis_align_dir = [["Turn_Right_120"]]
    else :
        axis_align_dir = [["Straight"]]
    return axis_align_dir

'''
*Function Name: <axis_direction()>
*Input: <none>
*Output: <the dictionary  dict_1,dict-2,dict_3 are returns the values of directions with coordinates of shortest path that is stored
        in list  in the dictionary>
*Logic: <It calcutlates the facing direction of every node by the use of both the nodes of that particular axis.>
'''

def axis_direction():
    for key in dict_1:
        pointlist =dict_1[key]
        x1 ,y1 = pointlist[0]
        x2,y2 = pointlist[1]
        axis_direction_1 =None
        axis_direction_2 = None

        if x1 < x2:
            axis_direction_1 ="E"
            axis_direction_2 = "W"
        else :
            axis_direction_1="W"
            axis_direction_2 = "E"
        pointlist[0] = [pointlist[0] , axis_direction_1]
        pointlist[1] = [pointlist[1] , axis_direction_2]

    for key in dict_2 :
        pointlist =dict_2[key]
        x1 ,y1 = pointlist[0]
        x2,y2 = pointlist[1]
        axis_direction_1 =None
        axis_direction_2 = None
        if x1 < x2 and y1 < y2 :
            axis_direction_1 ="SE"
            axis_direction_2 = "NW"
        else :
            axis_direction_1="NW"
            axis_direction_2 = "SE"
        pointlist[0] = [pointlist[0] , axis_direction_1]
        pointlist[1] = [pointlist[1] , axis_direction_2]

    for key in dict_3:
        axis_direction_1 =None
        axis_direction_2 = None
        pointlist =dict_3[key]
        x1 ,y1 = pointlist[0]
        x2,y2 = pointlist[1]
        if x1 > x2 and y1 < y2 :
            axis_direction_1 ="SW"
            axis_direction_2 = "NE"
        else :
            axis_direction_1="NE"
            axis_direction_2 = "SW"
        pointlist[0] = [pointlist[0] , axis_direction_1]
        pointlist[1] = [pointlist[1] , axis_direction_2]

    return dict_1,dict_2,dict_3

'''
*Function Name: <startcondition>
*Input:<takes coordinate of the starting position of the robot as the input>
*Output:<Return [init_point,init_direction] i.e starting point and starting direction>
*Logic: <It initialize the starting coordinates and particular direction required for the bot.>
'''

def startcondition(Robot_start):
    if Robot_start =="Start-1":
        init_point =(-1,5)
        init_direction = "E"
    else :
        init_point =(12,5)
        init_direction ="W"
    return [init_point,init_direction]

'''
*Function Name: <dict_axis()>
*Input: <takes the axis of the cell >
*Output: <Return dictionary for particular axis>
*Logic: <comparing the axis from the given arena configuration.>

'''
def dict_axis(axis):

    if axis == "1-1":
        dict =dict_1
    elif axis =="2-2":
        dict =dict_2
    else :
        dict=dict_3
    return dict
'''
Function Name: <point()>
*Input:<taking dictionary named 'arena config' as input>
*Output:<pebble_point,pitcher_point,aruco_pebble ,aruco_pitcher,id_dict>
*Logic:<It initializes the pitcher point, pebble point, pitcher_id, pebble_id and axis directon(all are in the form of dict.)
        from the given arena_configuration.>
'''
def points(arena_config):
    axis_direction()
    pebble_point ={}
    pitcher_point ={}
    aruco_pebble ={}
    aruco_pitcher={}
    id_dict ={}
    i=0
    j=0
    for key in arena_config  :
        cell_name = arena_config[key][0]
        cell_no = arena_config[key][1]
        cell_axis = arena_config[key][2]
        points = dict_axis(cell_axis)
        if cell_name == "Water pitcher" :
            pitcher_point[j] = points[cell_no]
            aruco_pitcher[j] = key
            id_dict[key]= 0
        else :
            pebble_point[i] =points[cell_no]
            aruco_pebble[i]= key
            id_dict[key] =0
            i=i+1
    return pebble_point,pitcher_point,aruco_pebble ,aruco_pitcher,id_dict

pebble_dict , pitcher_dict,vari.pebble_id ,vari.pitcher_id ,vari.id_list  = points(arena_config)

'''
*Function Name: <main1()>
*Input: <none>
*Output: <none>
*Logic: <this function implements the astar algorithm on the given arena config.
         using Graph.py , vari.py files and returns the shortest path then
         send the commands to bot for traversing.>
'''
def main1():

    init_node , init_direction =startcondition(Robot_start)
    while True:
        if  not no_of_pebble or not pebble_dict:
            sendcommand('b')
            print ("path complte")
            break
        else:
            print ("start ")
            print(init_node)
            print(init_direction)
            temp  = 999
            nearest_node = 0
            axis_direction = None
            delete_key =[]
            print (pebble_dict)
            print(pitcher_dict)
            for key in no_of_pebble:
                if no_of_pebble[key] <=0:
                    delete_key.append(key)
            if delete_key :
                for key in delete_key :
                    del(pebble_dict[key])
                    del(no_of_pebble[key])
            if no_of_pebble:
                for key  in pebble_dict :
                    for node in pebble_dict[key]:
                        shortestdistance = node_distance(init_node ,node[0])
                        if shortestdistance <= temp:
                            temp = shortestdistance
                            nearest_node = node[0]
                            axis_direction = node[1]
                            a=key
            print (a)
            atemp = vari.pebble_id[a]

            if a in no_of_pebble:
                no_of_pebble[a] = no_of_pebble[a] -1
                length = len(no_of_pebble)

            else :
                sendcommand('b')
                print("Path Complete")
                break


            """ shortest path from starting node to pickup node"""
            path,fcost,pick,botdirection,final_bot_dir = Astarsearch(init_node,init_direction,nearest_node)


            print ("path to pebble")
            print(path)
            turn_dir = turncalculator(final_bot_dir ,axis_direction)

            for i in turn_dir :
                botdirection.append(i)

            if botdirection[-1] == ["Turn_Left_120"] or ["Turn_Right_120"] :
                if botdirection[-1] == ["Turn_Left_120"] :
                    if final_bot_dir != axis_direction:
                        key = final_bot_dir
                        final_bot_dir = finalLeftdir[key]
                        print("fofoofofofofoof",botdirection[-1],final_bot_dir)
                elif botdirection[-1] == ["Turn_Right_120"] :
                    if final_bot_dir != axis_direction:
                        key = final_bot_dir
                        final_bot_dir = finalRightdir[key]
                        print("fofoofofofofoof",botdirection[-1],final_bot_dir)
            print (final_bot_dir)
            print(pick)
            print(botdirection)
            flag0 =0
            for direc in botdirection :
                if direc[0] in command.keys():
                    if direc[0] in ["Forward"]:
                        vari.C_variable = -3
                    if [direc[0]] in [["Turn_Left_120"],["Turn_Right_120"],["Straight"]]:
                        vari.id_list[atemp]=vari.id_list[atemp]+1
                        vari.C_variable = atemp
                    #time.sleep(5)
                    #print ("pebble")
                    sendcommand(command[direc[0]])
                    waitforresponse()


            init_node = pick
            init_direction = final_bot_dir
            print (init_node)
            print(init_direction)

            temp1 = 999
            destnode = 0
            des_axis_direction = None
            #print("pitcher_dict[0][0],pitcher_dict[1][0]",pitcher_dict[0][0][0],pitcher_dict[0][0][1])
            #print("pitcher_dict[0][1],pitcher_dict[1][1]",pitcher_dict[0][1][0],pitcher_dict[0][0][1])
            #for key in pitcher_dict[0]:
                #print("pitcher_dict[0][0],pitcher_dict[1][0]",pitcher_dict[0][0],pitcher_dict[1][0])
                #print("pitcher_dict[0][1],pitcher_dict[1][1]",pitcher_dict[0][1],pitcher_dict[1][1])

            for key in pitcher_dict[0]:
                shortestdistance = node_distance(init_node ,key[0])

                if (shortestdistance < temp1) :
                    destnode = key[0]
                    des_axis_direction = key[1]
                    temp1 =shortestdistance


            path,fcost,pick,botdirection,final_bot_dir = Astarsearch(init_node,init_direction,destnode)
            print (final_bot_dir)

            turn_dir = turncalculator(final_bot_dir ,des_axis_direction)
            for i in turn_dir :
                botdirection.append(i)

            if botdirection[-1] == ["Turn_Left_120"] or ["Turn_Right_120"] :
                if botdirection[-1] == ["Turn_Left_120"] :
                    if final_bot_dir != des_axis_direction:
                        key = final_bot_dir
                        final_bot_dir = finalLeftdir[key]
                        print("fofoofofofofoof",botdirection[-1],final_bot_dir)
                elif botdirection[-1] == ["Turn_Right_120"] :
                    if final_bot_dir != des_axis_direction:
                        key = final_bot_dir
                        final_bot_dir = finalRightdir[key]
                        print("fofoofofofofoof",botdirection[-1],final_bot_dir)
            a = vari.pitcher_id[0]

            print(path)
            print (botdirection)
            print (final_bot_dir)
            print(destnode)
            flag1 =0
            for direc in botdirection :
                if direc[0] in command.keys():
                    if [direc[0]] in [["Turn_Left_120"],["Turn_Right_120"],["Straight"]]:
                        vari.id_list[a]+=1
                        vari.C_variable = -3
                    #time.sleep(5)
                    print ("pitcher")
                    sendcommand(command[direc[0]])
                    waitforresponse()

            init_node = destnode
            init_direction = final_bot_dir


#It uses the threading library for merging the aruco projection part and algorithm part

if __name__ == '__main__':
    t1 = threading.Thread(target = main1)
    #t2 = threading.Thread(target = main)
    #t2.start()
    #time.sleep(20)
    t1.start()
