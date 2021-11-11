a={1:2,3:4,4:3,2:1,0:0}
b={}
max=0
for i in a:
    if a[i]>max:
        max=a[i]
        s=i
b.update({s:max})
a.pop(s,max)
max=0
for i in a:
    if a[i]>max:
        max=a[i]
        t=i
b.update({t:max})
a.pop(t,max)
max=0
for i in a:
    if a[i]>max:
        max=a[i]
        u=i
b.update({u:max})
a.pop(u,max)
max=0
for i in a:
    if a[i]>max:
        max=a[i]
        v=i
b.update({v:max})
a.pop(v,max)
# print(b)
max=0
for i in a:
    if a[i]>max:
        max=a[i]
    w=i
b.update({w:max})
a.pop(w,max)
print(b)



