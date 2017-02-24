# Program that recommends movies to users using SVD with the help of Movielens dataset

import numpy as np
import math
from scipy import linalg as LA
from matGen1 import m_l,r_l


def svd(m,dim=2):
	# Convert the list m to array form
	t=np.array(m)
	# t is the transpose of array (or matrix) m
	t=t.transpose()
	m=np.array(m)
	# Product of matrices m and m-transpose
	mmt=np.dot(m,t)

	# Find eigen values and eigen vectors of the product
	eval,evec=LA.eig(mmt)

	u=list()

	# Reduce the matrix to the dimension n x dim
	for i in range(len(evec)):
		u.append([0]*dim)
		for j in range(dim):
			u[i][j]=round(evec[i][j].real,2)

	# Product of matrices m-transpose and m
	m1=np.dot(t,m)

	# Find eigen values and eigen vectors of the product
	eval,evec=LA.eig(m1)

	v=list()
	# Retain only real part of the values
	for i in range(len(evec)):
		v.append([0]*len(evec[0]))
		for j in range(len(evec[0])):
			v[i][j]=round(evec[i][j].real,2)

	v=np.array(v)
	# V-transpose
	Vt=v.transpose()

	# Reatain only the required dimensions
	Vt=Vt[:dim]
	V=Vt.transpose()

	return u,V


print 'Enter the number of concepts:'
dim=input()

u,v=svd(r_l,dim)

# Take the input - user id
print 'Enter user id:'
u_id=input()

# q - the row corresponding to user with user id u_id i.e, his ratings for the movies
q=[r_l[u_id-1]]

v=np.array(v)

# Get the v-transpose matrix
vt=v.transpose()

# Product of matrices q and v
pres=np.dot(q,v)

# Product of the resultant matrix with v-transpose
res=np.dot(pres,vt)
res=list(res[0])
res1=res

# Sort the ratings in descending order
res1=sorted(res1,reverse=True)

'''print 'Movies he watched'
for i in range(len(q[0])):
	if q[0][i] != 0:
		print m_l[i]
'''

print 'Enter number of movies to be shown:'
sl=input()

i=0
j=0
print 'Movies Recommended'
# To check the movies the person has already watched is not recommended
while i<sl:
	if q[0][res.index(res1[j])] == 0:
		print m_l[res.index(res1[j])]
		i+=1
	j+=1
