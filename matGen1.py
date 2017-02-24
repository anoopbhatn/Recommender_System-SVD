import csv

fileh=open('movies1.csv','r')

reader = csv.reader(fileh, delimiter=',')
m_l=list()
l=list()

# The list of all the movies
for row in reader:
	l=row
	m_l.append(l[1])

i=943


fileh=open('ratings1.csv','r')

reader = csv.reader(fileh, delimiter=',')
r_l=list()
for j in range(i):
	r_l.append([0]*1682)

l=list()
# The dictionary - { user_id : { movie_id : rating } }
for row in reader:
	l=row
	try:
		r_l[int(l[0])-1][int(l[1])-1]=float(l[2])
	except:
		print l[1]