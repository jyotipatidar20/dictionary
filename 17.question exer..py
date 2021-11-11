dic1={1:10, 2:20}
dic2={3:30,2:40}
dic3={5:50,6:60}
c={}
for i in (dic1,dic2,dic3):
    c.update(i)
print(c)