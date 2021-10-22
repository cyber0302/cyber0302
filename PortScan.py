from socket import *
from threading import *
import optparse


def PortScan(targethost,targetport):
    try:
        sock = socket(AF_INET,SOCK_STREAM)
        sock.connect((targethost,targetport))
        print(f"[+] {targetport} => Port Open")
    except:
        print(f"[-] {targetport} => Port Close")
    finally:
        sock.close()



def hostScan(targethost,targetports):
    try:
        targetIp = gethostbyname(targethost)
        print("*" * 15, "*" * len(targetIp), sep="")
        print(f"[+] Ip adresi: {targetIp}")
        try:
            targetName = gethostbyaddr(targetIp)
            print(f"[+]makine adı: {targetName[0]}")
            print("*" * 13, "*" * len(targetName[0]), sep="")
        except:
            print("makina adı bulunamadı")
            print("*" * 17, "*" * len(targetIp), sep="")
    except:
        print(f"host bulunamadı: {targethost}")
    setdefaulttimeout(1)
    for targetport in targetports:
        try:
            t = Thread(target=PortScan,args=(targethost,int(targetport)))
            t.start()
        except:
            print("hatalı işlem")


def main():
    parser = optparse.OptionParser("Program Use: -H <Host Address> -p <Port address")
    parser.add_option("-H", dest="targetHost", type="string", help="Hedef Ana makine")
    parser.add_option("-p", dest="targetPort", type="string", help="(,) veya (,)'süz port belirtin")

    (options, args) = parser.parse_args()
    targetHost = options.targetHost
    targetPorts = str(options.targetPort).split(",")
    if (targetHost == None) or (targetPorts[0] == None):
        print(parser.usage)
        exit(0)
    hostScan(targetHost, targetPorts)


if __name__ == "__main__":
    main()



























