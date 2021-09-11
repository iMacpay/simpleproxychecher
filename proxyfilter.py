import time
import requests



def getproxy(Proxyurl):
    r = requests.session()
    r = requests.get(Proxyurl)
    proxies = r.text
    proxylist = proxies.splitlines()
    return proxylist


def simplecheck(Testurl, Proxy):
    r = requests.session()
    proxies = {'http': 'http://' + Proxy,
               'https': 'http://' + Proxy}
    r = requests.get(Testurl, proxies=proxies)
    result = r.status_code
    return result


if __name__ == "__main__":
    testurl = ""
    proxyurl = ""
    proxylist = getproxy(proxyurl)
    for proxy in proxylist:
        res = simplecheck(testurl, proxy)
        print(proxy, "response code is:", res)
