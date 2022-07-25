#Python 
#Practice simple car game :)
import sys
from colorama import Fore
import time

class main:
    def car(commd, startedAlready):
        commd = ''
        while True:
            commd = input(Fore.LIGHTCYAN_EX + """┌──(root㉿Cargame)-[~]
└─# """).lower()
            if commd == 'start':
                if startedAlready:
                    print("The car is started already!")
                else:
                    startedAlready = True
                    print("The car is running.")
            elif commd == 'stop':
                if not startedAlready:
                    print("The car is stopped already!")
                else:
                    startedAlready = False
                    print("The car has stopped")
            if commd == 'quit':
                print("Thanks for playing! \n quiting...")
                time.sleep(2)
                sys.exit()
            elif commd == 'help':
                print("""
help = to see the following commands
start = to start the car
stop = stop the car
quit = to exit
                      """)
                
if __name__ == '__main__':
    main().car(startedAlready=False)
                    
                
                    
                
                
            
        

