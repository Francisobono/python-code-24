import sys
import os
import time


#stop, start, restart

time.sleep(4)
def validity_check():   
    if len(sys.argv) < 2 or sys.argv[1] not in ('stop', 'start', 'restart'):
        print("Please provide a valid choice (stop, start, resart)")

def start_d():
    os.system('systemctl start httpd')
    
def stop_d():
    os.system('systemctl stop httpd')
    
def restart_d():
    os.system('systemctl restart httpd')

    validity_check()
    if sys.argv[1] =='stop':
        stop_d()
    elif sys.argv[1] =='start':
        start_d()
    else:
        restart_d()
        
if __name__== '__main__':
    
    main()

        