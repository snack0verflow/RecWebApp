import math
import random
import numpy as np
import pickle

u = 50
m = 38
ratings_matrix = np.zeros((u,m))

for j in range(m):
	mean = random.uniform(2.6,3.9)

	for i in range(u):
		a = random.uniform(0,1)
		if(a<0.6):
			ratings_matrix[i][j] = mean + random.uniform(-0.9,0.9)
			ratings_matrix[i][j] = round(ratings_matrix[i][j],2)

# for i in range(u):
# 	for j in range(m):
# 		print(ratings_matrix[i][j],end='\t')
# 	print()
with open('ratings.pkl','wb') as f:
	pickle.dump(ratings_matrix,f)
# print(ratings_matrix)
