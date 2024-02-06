def main():
    a=input("what time is it?")
    a=convert(a)
    if(a>=7 and a<=8):
        print("breakfast time")
    elif(a>=12 and a<=13):
        print("lunch time")
    elif(a>=18 and a<=19):
        print("dinner time")



def convert(time):
    x,y=time.split(":")
    x=int(x)
    y=int(y)/60
    time=str(x+y)
    return float(time)



if __name__ == "__main__":
    main()
