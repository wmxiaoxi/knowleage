import requests
url1 = "/zentao/bug-create-1-0-moduleID=0.html"
s=requests.session()
d={
"product": "1",
    "module": "0",
    "project": "",
    "openedBuild[]": "trunk",
    "assignedTo": "admin",
    "type": "codeerror",
}


f={
    'files[]':("1.png",open("d:\\1.png,rb",'image/png')),
    "lables[]":"tu1",
    "files[]":("2.png",open("d:\\2.png,rb",'image/png')),
    "lables[]":"tu2",
}
r=s.post(url1,data=d,files=f)
print(r.content)