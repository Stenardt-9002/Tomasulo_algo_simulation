import os
# import finalparser

DEBUG = False



if __name__ == '__main__':
    if DEBUG == False:
        if os.name == 'nt':
            try:
                os.system("python finalparser.py")
            except:
                print("An unexpected Error occured,Program Halted,Report Input to user OR check python installation in O.S.")


        pass
        #windows
        else:
            try:
                os.system("python3 finalparser.py")
            except:
                print("An unexpected Error occured,Program Halted,Report Input to user")

    else:
        os.system("python3 debuggerfile.py")
