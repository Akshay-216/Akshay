def main():
    msg=input("msg is:")
    convert(msg)
def convert(str):
    print(str.replace(':)','🙂').replace(':(', '🙁'))
if __name__=='__main__':
    main()

