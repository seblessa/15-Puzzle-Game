from main import *
from sys import argv

#run it all
if __name__ == '__main__':
    try:
        len(argv[1])
    except:
        intro()
    else:
        try:
            argv[2]=="-p" or argv[2]=="--print"
        except:
            text(argv[1],False)
        else:
            if argv[2]=="-p" or argv[2]=="--print":
                text(argv[1],True)
            else:
                print("Error")
                print("Only flags available: -p/--print")