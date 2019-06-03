'''
Team Id : <974>
*Author List : <Akshay Sharma, Bhaskar dutt, Varun pandey>
*Filename: <Graph.py>
*Theme: <Thristy Crow -- Specific to eYRC /eYRCPlus >
*Functions: <neighbour_gen(), node_distance(), direction(), Astarsearch()>
*Global Variables: <None>
'''
import math
#this graph dictonary stores the arena in the graph form
graph = {(-1,5):[(0,5)],
 (12,5):[(11,5)],
 (0,5):[(1,6),(1,4)],
 (1,6):[(0,5),(0,7),(2,6)],
 (0,7):[(1,6),(1,8)],
 (1,8):[(0,7),(2,8)],
 (1,4):[(0,5),(0,3),(2,4)],
 (0,3):[(1,4),(1,2)],
 (1,2):[(0,3),(2,2)],
 (2,8):[(1,8),(3,7),(3,9)],
 (3,7):[(2,8),(2,6),(4,7)],
 (2,6):[(1,6),(3,7),(3,5)],
 (3,5):[(2,6),(2,4),(4,5)],
 (2,4):[(1,4),(3,5),(3,3)],
 (3,3):[(2,4),(2,2),(4,3)],
 (2,2):[(1,2),(3,3),(3,1)],
 (3,9):[(2,8),(4,9)],
 (4,9):[(3,9),(5,8),(5,10)],
 (5,8):[(4,9),(4,7),(6,8)],
 (4,7):[(3,7),(5,8),(5,6)],
 (5,6):[(4,7),(4,5),(6,6)],
 (4,5):[(3,5),(5,6),(5,4)],
 (5,4):[(4,5),(4,3),(6,4)],
 (4,3):[(3,3),(5,4),(5,2)],
 (5,2):[(4,3),(4,1),(6,2)],
 (4,1):[(5,2),(3,1),(5,0)],
 (3,1):[(2,2),(4,1)],
 (5,10):[(4,9),(6,10)],
 (6,10):[(5,10),(7,9)],
 (7,9):[(6,10),(6,8),(8,9)],
 (6,8):[(5,8),(7,9),(7,7)],
 (7,7):[(6,8),(6,6),(8,7)],
 (6,6):[(5,6),(7,7),(7,5)],
 (7,5):[(6,6),(6,4),(8,5)],
 (6,4):[(5,4),(7,5),(7,3)],
 (7,3):[(6,4),(6,2),(8,3)],
 (6,2):[(5,2),(7,3),(7,1)],
 (7,1):[(6,2),(6,0),(8,1)],
 (6,0):[(7,1),(5,0)],
 (5,0):[(4,1),(6,0)],
 (8,9):[(7,9),(9,8)],
 (9,8):[(8,9),(8,7),(10,8)],
 (8,7):[(7,7),(9,8),(9,6)],
 (9,6):[(8,7),(8,5),(10,6)],
 (8,5):[(7,5),(9,6),(9,4)],
 (9,4):[(8,5),(8,3),(10,4)],
 (8,3):[(7,3),(9,4),(9,2)],
 (9,2):[(8,3),(8,1),(10,2)],
 (8,1):[(7,1),(9,2)],
 (10,8):[(9,8),(11,7)],
 (11,7):[(10,8),(10,6)],
 (10,6):[(9,6),(11,7),(11,5)],
 (11,5):[(10,6),(10,4)],
 (10,4):[(9,4),(11,5),(11,3)],
 (11,3):[(10,4),(10,2)],
 (10,2):[(9,2),(11,3)] }

"""
Function Name : neighbour_gen()
Input: graph, point
Output: Returns neighbour coordinates for the specific node(point) using
point as the key in dictionary graph
"""
def neighbour_gen(graph, point):
    neighbours = graph[point]
    return neighbours

"""
Function Name : node_distance()
Input: curr_point1, goal_point2
Output: returns h variable which contains the manhattan distance
between the two coordinates by subtracting a x and y coordinates
of curr_point1 from x and y coordinate of goal_point2 respectively.
"""
def node_distance(curr_point1,goal_point2):
    x1,y1 = curr_point1
    x2,y2 = goal_point2

    h= math.sqrt(((x1-x2)**2)+((y1-y2)**2))
    return h

"""def node_distance2(curr_point1,curr_point1_dir,list_point2,list_point3):
    init__point = curr_point1
    init__dir = current_point1_dir
    point_1 = list_point2[0]
    point_1_dir = list_point2[1]
    point_2 = list_point3[0]
    point_2_dir = list_point3[1]
    short_path = None ,low_fcost = None ,pick,short_botdirection = None , final_bot_direc = None


    path_1,fcost_1,pick_1,botdirection_1,final_bot_dir_1 = Astarsearch(init__point,init__dir,point_1)

    path_2,fcost_2,pick_2,botdirection_2,final_bot_dir_2 = Astarsearch(init__point,init__dir,point_2)
    turn_dir = turncalculator(final_bot_dir ,axis_direction)


    if fcost_1 < fcost_2 :
        short_path,low_fcost,pick,short_botdirection,final_bot_direc = path_1,fcost_1,pick_1,botdirection_1,final_bot_dir_1

    elif fcost_1 > =fcost_2 :
        short_path,low_fcost,pick,short_botdirection,final_bot_direc = path_2,fcost_2,pick_2,botdirection_2,final_bot_dir_2

    turn_dir = turncalculator(final_bot_direc,axis_direction)

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



    else:
        #h1= abs(x1-x2)+abs(y1-y2)
        #h2= abs(x1-x3)+abs(y1-y3)
        h1= (x1-x2)+(y1-y2)
        h2= (x1-x3)+(y1-y3)
    h1 = abs(h1)
    h2 = abs(h2)
    if h1 < h2:
        h = h1
        point = list_point2[0]
        dir = list_point2[1]
    else:
        h = h2
        point = list_point3[0]
        dir = list_point3[1]

    return h , point, dir"""


"""
Function Name : direction()
Input: current_direction , current_point, next_point
Output: returns dictionary(option{}) and next_direction, the next direction
is calculated using current_direction and next_point and the bot direction
is decided dictionary(option{})

"""

def direction(current_direction,current_point,next_point) :
    x1,y1 = current_point
    x2,y2 = next_point


    if y2-y1 == 1:
        if x2-x1 == 1:
            next_direction = 'SE'
        elif x2- x1 == -1:
            next_direction = 'SW'
    elif y2 - y1 == -1 :
        if x2-x1 == 1:
            next_direction = 'NE'
        elif x2- x1 == -1:
            next_direction = 'NW'
    elif y2 -y1 ==0 :
        if x2 - x1 ==1:
            next_direction = 'E'
        elif x2 - x1 == -1 :
            next_direction = 'W'
    decider = current_direction + next_direction
    option ={
    "EE" :['Forward'],
    "WW" :['Forward'],
    "NWNW":['Forward'],
    "NENE":['Forward'],
    "SESE":['Forward'],
    "SWSW":['Forward'],

    "EW" : ['Turn_180'],
    "WE" : ['Turn_180'],
    "NESW":['Turn_180'],
    "NWSE":['Turn_180'],
    "SENW":['Turn_180'],
    "SWNE":['Turn_180'],
    #"NWSW":['Turn_180'],
    #"SWNW":['Turn_180'],

    "ENE" :['Left_Forward'],
    "WSW" :['Left_Forward'],
    "NWW" :['Left_Forward'],
    "SWSE":['Left_Forward'],
    "NENW":['Left_Forward'],
    "SEE" :['Left_Forward'],
    #"SNW":['Left_Forward'],
    #"NNW":['Left_Forward'],
    #"ENW":['Left_Forward'],
    #"WSE":['Left_Forward'],
    #"SENE":['Left_Forward'],
    #"NEW":['Left_Forward'],
    #"SWE":['Left_Forward'],
    #"NWSW":['Left_Forward'],

    "ESE" :['Right_Forward'],
    "WNW" :['Right_Forward'],
    "NWNE":['Right_Forward'],
    "NEE" :['Right_Forward'],
    "SESW":['Right_Forward'],
    "SWW" :['Right_Forward'],
    #"NWE":['Right_Forward'],
    #"ESW":['Right_Forward'],
    #"WNE":['Right_Forward'],
    #"SEW":['Right_Forward'],
    #"NESE":['Right_Forward'],
    #"SWNW":['Right_Forward']

    }

    return option[decider],next_direction
"""
Function Name : Astarsearch()
Input: graph , startnode, startdirection, destnode
Output: this function returns the pathlist,fcost,
pickup_node_in_astar,
botdirections, final_facing_dir

"""

def Astarsearch(startnode,startdirection,destnode):
    open_list = []
    close_list = []
    pathlist=[]
    nodeparents = {}
    fcost = {}
    gcost = {}
    nodedirections = {}
    botdirections = []
    fcost[startnode] = 0 + node_distance(startnode, destnode)
    gcost[startnode] = 0
    nodedirections[startnode] = [startdirection]

    open_list.append(startnode)
    while True :
        fcostcomp  = 999
        current_node  = 0

        for node in open_list:
            if (fcost[node] < fcostcomp) :
                current_node = node
                fcostcomp = fcost[node]
        open_list.remove(current_node)
        close_list.append(current_node)

        if (current_node ==  destnode):
            break

        neighbouringnodes =neighbour_gen(graph, current_node)

        for neighbour in neighbouringnodes:
            if neighbour in close_list:
                continue
            turn ,next_direction = direction(nodedirections[current_node][0],current_node,neighbour)
            new_gcost = gcost[current_node] + node_distance(current_node,neighbour)

            if neighbour not in open_list:
                open_list.append(neighbour)
            elif new_gcost >= gcost[neighbour]:
                continue

            gcost[neighbour] = new_gcost
            fcost[neighbour] = gcost[neighbour] + node_distance(neighbour,destnode)
            nodedirections[neighbour] = [next_direction,turn]

            nodeparents[neighbour] = current_node

    pathnode= destnode
    pathlist.append(destnode)

    while pathnode != startnode :
        pathnode = nodeparents[pathnode]
        pathlist.append(pathnode)

    pathlist.reverse()
    length =  len(pathlist)
    for j in range(0,length-1):
        contents=nodedirections[pathlist[j+1]]
        botdirections.append(contents[1])


    pickup_node_in_astar = pathlist[-1]
    final_facing_dir = nodedirections[destnode][0]

    return pathlist,fcost[destnode], pickup_node_in_astar, botdirections, final_facing_dir
