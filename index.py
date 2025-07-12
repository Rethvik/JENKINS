import sys
if(len(sys.argv)>1):
    print("Now I will say based on your age")
    if(int(sys.argv[0])>20):
        print('You entered yours 20, carefull!!!')
    else:
        print("Enjoy the life")
else:
    print("Live on your life")