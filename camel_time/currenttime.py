import time

def getTime():
    return time.gmtime()

def main():
    while(True):
        file = open('times.txt', 'a+')

        currentTime = getTime()

        strTime = time.strftime("%Y-%m-%d %H:%M:%S", currentTime)
        file.write(strTime)

        file.write('\n')
        file.close()
        time.sleep(30)

if __name__ == '__main__':
    main()
