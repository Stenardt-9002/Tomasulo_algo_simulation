import os
# import finalparser


if __name__ == '__main__':
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

        pass
