
import sys

a=[1,2,3,4]
print("Press Enter to continue or press Esc to exit: ")
while True:
    try:
        if KeyboardInterrupt.is_pressed('ENTER'):
            print("you pressed Enter, so printing the list..")
            print(a)
            break
        if KeyboardInterrupt.is_pressed('Esc'):
            print("\nyou pressed Esc, so exiting...")
            
    except:
        break