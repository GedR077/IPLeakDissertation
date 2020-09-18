import socket
import sys ### Line 1-3 of code import modules that allow for extra functionality to be used in code later
import time



host_name = ""
host_ip = "" ### This block of code assigns empty values to both host_name and host_ip to be used later
             ### Assigning them outside of a function allows for them to be set as global variables, thus able
             ### to be called and written too in other functions

def mainMenu():
    
    print("************MAIN MENU**************")
    print()

    choice = input("""
            A: Set Initial IP Address
            B: Test Current Traffic
            Q: Quit/Log Out

            Please enter your choice: """)

    if choice == "A" or choice =="a":
        get_Host_Name_IP()
    elif choice == "B" or choice =="b":
            leak_Detect()
            mainMenu()
    elif choice == "C" or choice =="b":
            change_IP()
            mainMenu()
    elif choice=="Q" or choice=="q":
            sys.exit
    else:
            print("You must only select either A or B")
            print("Please try again")
            mainMenu()



def get_Host_Name_IP():
    try:
        global host_name # This defines access to the global host_name variable so it can be set
        host_name = socket.gethostname() # Using Python's socket module to get the hostname of computer
        global host_ip
        host_ip = socket.gethostbyname(host_name) # Using hostname and socket module to find IP address of computer
        print("Hostname : ", host_name)
        print("IP : ", host_ip)
        time.sleep(5)
        mainMenu() # Previous line silences/delays the program for 5 seconds before returning to main menu in current line
    except:
        print("Unable to get Hostname and IP")
        
        time.sleep(5)
        mainMenu() ## This except loop simply throws an error and returns to the main menu if host name and IP can't be found
        

def leak_Detect():
    leak = 0

    while leak < 1 : # Sets a while loop while variable 'leak' is set a 0
        vpn_name = socket.gethostname()
        vpn_ip = socket.gethostbyname(vpn_name) ## Current and previous line grabs the current hostname and IP of computer respectively

        if host_ip != "": # If the global host_ip variable is not empty, continue the program
            

            if vpn_ip == host_ip : # If the new vpn_ip variable is the same as the global host_ip variable continue loop
                print ("Your IP is leaking")
                print (vpn_ip)
                print (host_ip)
                leak += 1 # Add 1 into leak to break the loop
                time.sleep(5)
            elif vpn_ip != host_ip : # If vpn_ip and host_ip are not the same, continue program
                print ("No leak detected, running again...")
                vpn_ip = socket.gethostbyname(vpn_name)
                time.sleep(5)

        else : # Else if global host_ip variable is empty, only continue this line of programming
            print ("No IP found, please use option A first")
            break
            
    mainMenu()

def change_IP ():
    global host_ip
    host_ip = "192.000.0.00" ######### TEST FUNCTION #########
    print (host_ip)
    mainMenu()


mainMenu() 

