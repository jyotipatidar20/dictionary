a={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
b={}
min=0
for i in a:
    if a[i]<min:
        min=i
    s=i
b.update({s:min})
a.pop(s,min)
print(min)
min=0
for i in a:
    if a[i]<=min:
        min=i
    t=i
b.update({t:min})
a.pop(t,min)
print(a)
min=0
for i in a:
    if a[i]<min:
        min=a[i]
    u=i
b.update({u:min})
a.pop(u,min)
min=0
for i in a:
    if a[i]<min:
        min=a[i]
    v=i
b.update({v:min})
a.pop(v.min)
min=0
for i in a:
    if a[i]<min:
        min=a[i]
    w=i
b.update({v:min})
a.pop(w,min)
print(b)

