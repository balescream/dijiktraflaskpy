#creates random database with paths for 50 nodes
import random
f=open("db.txt","a")
x=0
while x < 50:
	q=random.randint(0,50)
	f.write(str(q))
	f.write("	")
	p=random.randint(0,50)
	f.write(str(p))
	f.write("	")
	if p==q:
		f.write('0')
	else:
		f.write(str(random.randint(1,105)))
	f.write("\n")
	x+=1
f.close();		