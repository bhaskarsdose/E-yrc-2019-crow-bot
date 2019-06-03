'''
Team Id : <974>
*Author List : <Akshay Sharma, Bhaskar dutt, Varun pandey>
*Filename: <echo.py>
*Theme: <Thristy Crow -- Specific to eYRC /eYRCPlus >
*Functions: <sendcommand(), waitforresponse()>
*Global Variables: <global variable ser>
'''

import serial
import time
ser = serial.Serial("COM8", 9600, timeout=0.005)
'''
*Function Name: <sendcommand()>
*Input: <command >
*Output: <None>
*Logic: <it send command to the xbee module>

'''

def sendcommand(command):
    if ser.isOpen():
        print ("sending command ", command)
        ser.write(command.encode('utf-8'))
        ser.reset_output_buffer()
        # for character in command:
        #    ser.write(character)
    else:
        print ("Send-Serial not open!")
'''
*Function Name: <waitforresponse()>
*Input: <none >
*Output: <None>
*Logic: <it wait for  command from the xbee module>
'''

def waitforresponse():
    print (' awaiting response')
    if ser.isOpen():
        #start_time = time.now()
        while ser.inWaiting() == 0:
            #end_time = time.now()
            #elasped_time = start_time - end_time
            #if elasped_time > 6 :
            #    sendcommand(command[direc[0]])
            #    waitforresponse()
            #else:
            continue
        size = ser.inWaiting()
        received = ser.read(1)
        print ('size :', size)
        if size:
            print ("Received: ")
            print(received)
        else:
            print ('invalid character received')
        time.sleep(0.5)
    else:
        print ("Read-Serial not open!")

    ser.reset_input_buffer()
    print ('')
