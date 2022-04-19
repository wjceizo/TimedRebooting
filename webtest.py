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
    port = 53
    delay = 60
    Det = 23
    try:
        opts, args = getopt.getopt(argv, "hw:t:p:d:c:", ["wfile=", "tfile=","pfile=","dfile=","cfile="])
    except getopt.GetoptError:
        print("webtest.py -w <inputweb> -t <inputtime> -p <port> -d <delay> -c <Det>默认的host为114.114.114.114，默认的时间为03:15,默认的端口为53，默认的等待时间是60分钟，默认连续检测次数是22")
        sys.exit(2)
    for opt, arg in opts:
        if opt == "-h":
            print("webtest.py -w <inputweb> -t <inputtime> -p <port> -d <delay> -c <Det>")
            sys.exit()
        elif opt in ("-w", "--wfile"):
            inputweb = arg
        elif opt in ("-t", "--tfile"):
            inputtime = arg
        elif opt in ("-p", "--pfile"):
            port = arg
        elif opt in ("-d", "--dfile"):
            delay = arg
        elif opt in ("-c", "--cfile"):
            Det = arg
    return inputweb, inputtime, port, delay, Det

web0, rebootTime0, port0, delay0, det0 = cys(sys.argv[1:])

web = os.getenv('Timed_inputweb')
rebootTime = os.getenv('Timed_inputtime')
port = os.getenv('Timed_port')
delay = os.getenv('Timed_delay')
det = os.getenv('Timed_det')

if web is None:
    web = web0
if rebootTime is None:
    rebootTime = rebootTime0
if port is None:
    port = port0
if delay is None:
    delay = delay0
if det is None:
    det = det0

port = int(port)
delay = int(delay)
det = int(det)

print('setHost:   ' + str(web))
print('setRootTime:   ' + str(rebootTime))
print('setPort:   ' + str(port))
print('setDelay:   ' + str(delay))
print('setConsecutiveDetections:   ' + str(det))



def Testroot():
    global flag
    if flag >= det:
        os.system(u"shutdown -r now")
        print("I will reboot")
    else:
        print("net is good")
        flag = 0


def internet(host = web, portd=port, timeout=5):
  """
  Host: 114.114.114.114
  OpenPort: 53/tcp
  Service: domain (DNS/TCP)
  """
  connect = 1
  for i in range(15):
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, portd))
        connect = 0
        print('connect successful')
    except:
        print('no connect')
  return connect


def test():
    global flag
    print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    PING_RESULT = internet()
    print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    if PING_RESULT == 0:
        flag = flag
    else:
        flag = flag + 1


# schedule.every().minutes.do(test)
schedule.every(delay).minutes.do(test)
# 每delay分钟检测一次网络情况
schedule.every().day.at(rebootTime).do(Testroot)

while True:
    schedule.run_pending()
    time.sleep(1)
