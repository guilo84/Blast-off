from time import sleep

def blastoff(t):
    while t > 0:
        print(t)
        t-=1
        sleep(1)
    print("blast off")

count = int(input("How many seconds until launch?  "))

blastoff(count)
