import schedule
import time
import os
import sys, getopt
import socket


PING_RESULT = 0
NETWORK_RESULT = 0
flag = 0


def cys(argv):
    """
    默认的host为114.114.114.114，默认的时间为03:15。
    """
    inputweb = '114.114.114.114'
    inputtime = "03:15"
    try:
        opts, args = getopt.getopt(argv, "hw:t:", ["wfile=", "tfile="])
    except getopt.GetoptError:
        print("webtest.py -w <inputweb> -t <inputtime> 默认的host为114.114.114.114，默认的时间为03:15。")
        sys.exit(2)
    for opt, arg in opts:
        if opt == "-h":
            print("webtest.py -w <inputweb> -t <inputtime>")
            sys.exit()
        elif opt in ("-w", "--wfile"):
            inputweb = arg
        elif opt in ("-t", "--tfile"):
            inputtime = arg
    return inputweb, inputtime

web, rebootTime = cys(sys.argv[1:])
print('setHost:   ' + web)
print('setRootTime:   ' + rebootTime)


def Testroot():
    global flag
    if flag == 2:
        os.system(u"shutdown -r now")
        print("I will reboot")
    else:
        print("net is good")
        flag = 0


def internet(host = web, port=53, timeout=3):
  """
  Host: 114.114.114.114
  OpenPort: 53/tcp
  Service: domain (DNS/TCP)
  """
  connect = 1
  for i in range(50):
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        connect = 0
        print('connect successful')
    except:
        print('no connect')
  return connect

# def ping():
#     result = os.system(u"ping " + web + " -n 10")
#     if result == 0:
#         print("net good")
#     else:
#         print("net has wrong")
#     return result


def test():
    global flag
    print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    PING_RESULT = internet()
    print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    if PING_RESULT == 0:
        flag = 1
    else:
        if flag == 1:
            flag = 1
        else:
            flag =2

# schedule.every().minutes.do(test)
schedule.every(60).minutes.do(test)
# 每60分钟检测一次网络情况
schedule.every().day.at(rebootTime).do(Testroot)

while True:
    schedule.run_pending()
    time.sleep(1)
