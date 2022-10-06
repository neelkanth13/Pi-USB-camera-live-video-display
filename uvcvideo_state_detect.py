import os
import subprocess as sp
import time
 
string1 = "uvcvideo: Failed"
               

while True:
    # Kill if there any instance of guvcview running
    guvcview_pid = sp.getoutput('pidof guvcview')
    os.system("kill -9 " + guvcview_pid)
    os.system('sudo dmesg -c')

    time.sleep(3)
    # Toggle all the USB ports of Pi
    os.system('sudo uhubctl -l 1-1 -p all -a off')
    time.sleep(3)
    os.system('sudo uhubctl -l 1-1 -p all -a on')
    time.sleep(3)

    # Now start gucview
    os.system('guvcview &')
    guvcview_pid = sp.getoutput('pidof guvcview')

    time.sleep(6)
    os.system('sudo dmesg -c | grep "uvcvideo: Failed" > /home/pi/uvcvideo_err_op')
    
    # check if gucview has failed to initialize properly
    file1 = open("/home/pi/uvcvideo_err_op", "r")
    readfile = file1.read()

    if string1 in readfile: 
        print('String [', string1, '] Found In File')

        # kill gucvview process there
        os.system("kill -9 " + guvcview_pid)
    else:
        #guvcview has been initialized successfully
        break
 

# closing a file
file1.close() 
