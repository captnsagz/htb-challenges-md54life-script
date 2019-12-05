from bs4 import BeautifulSoup
import requests
import hashlib

port = input("Enter port:")
while(True):
        url = "http://docker.hackthebox.eu:" + port + "/"
        r = requests.session()
        out = r.get(url)
        soup = BeautifulSoup(out.content,"html.parser")
        md = hashlib.md5(soup.h3.text.encode('utf-8')).hexdigest()
        out = r.post(url=url, data = {'hash':md})
        print("sending md5 :-{}".format(md))
        if "Too slow!" in out.text:
                print("Too slow!")
        else:
                print(out.text)
                break;
