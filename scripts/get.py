import requests
origin = requests.get(
    "https://zhs.company/link/cNFFLggjAAvwtHFc?mu=6&ox=1&tj=1").text
lines = origin.split("\n")
w = ""
for singleLine in lines:
    l = singleLine.split(",")
    if "HK"  in l[len(l)-1]:
        if "NF" not in l[len(l)-1]:
            pass
        elif "游戏" in l[len(l)-1]:
            pass
        elif "耗尽" in l[len(l)-1]:
            pass
        else:
            w += ",".join(l)
            w +="\n"
f = open("zhs.txt",mode="w")
f.write(w)
f.close()
