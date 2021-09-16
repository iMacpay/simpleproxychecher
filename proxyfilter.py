import time
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed



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
    try:
        r = requests.get(Testurl, proxies=proxies,timeout=10)
    except requests.exceptions.ProxyError:
        print(f'Proxy {Proxy} Can not connect')
    result = r.status_code
    return result,Proxy




if __name__ == "__main__":
    testurl = "http://proxytest.edatastore.io"
    proxyurl = "http://onezpay.com/iplist/txt"
    proxylist = getproxy(proxyurl)
    Threads=50
    with ThreadPoolExecutor(max_workers=Threads) as executor:
        obj_list = []
        begin = time.time()
        for proxy in proxylist:
            res = executor.submit(simplecheck,testurl,proxy)
            obj_list.append(res)
        for future in as_completed(obj_list):
            data = future.result()
            print(f'the response from proxy :{data[1]}  is  {data[0]}！')
        times = time.time() - begin
        print(times)



