from ping3 import ping
import requests


def result(x):
    if x==None:
        return False

    else:
        return True


"""
InputProxyList = open( "InputProxyList.txt","w")
InputProxyList.write("Please remove this text and paste your proxy list for example\n0.0.0.0:0000\n1.1.1.1:1111")
"""

InputProxyList = open( "InputProxyList.txt","r")
OutputProxyList = open("OutputProxyList.txt", "w")
rp=InputProxyList.read().split()
InputProxyList.close()

spbefor=10000000
SmallestPing=-1
SmallestPingServer="All Of Servers Are Time out..."


T=0

for n in range(0,(len(rp))):

        s=rp[n].split(":")[0]
        proxyIPPort=rp[n]
        httpProxy="http://"+proxyIPPort
        httpsProxy="http://"+proxyIPPort
        spnow=ping(s)
        ToF=result(spnow)
        if ToF:
            proxy = { "http": httpProxy,
                      "https": httpsProxy
                      }

            try:
                r = requests.get("https://telegram.org/", proxies=proxy)
                LiveOrDie = "It is Telegram proxy"
                T=T+1

            except:
                LiveOrDie = "Not Telegram proxy"

        print(LiveOrDie)
        print((n+1),"of",(len(rp)))
        print(rp[n])
        print("Live" if ToF else "Die")
        print("----------------------------------")


        print("T=",T)

        if ToF:
            if spnow<spbefor:
                SmallestPing=spnow
                SmallestPingServer=rp[n]
                spbefor=spnow


            OutputProxyList.write(rp[n])
            OutputProxyList.write("\n")
            OutputProxyList.write("--------------------------------")
            OutputProxyList.write("\n")

if SmallestPing!=(-1):
    print(SmallestPing)
print(SmallestPingServer)


OutputProxyList.close()



