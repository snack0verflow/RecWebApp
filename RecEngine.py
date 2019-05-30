import numpy as np
import pickle
import math

u = 50
m = 38
ratings = np.zeros((u,m))

with open('ratings.pkl','rb') as f:
	ratings = pickle.load(f)

# print(ratings)

user = 5

def avgRating(user):
	s = 0.0
	c = 0 
	for rating in ratings[user]:
		if (rating != 0):
			s += rating
			c += 1
	return(s/c)

def pearsonSimilarity(user1,user2):
	a,b,c = (0.0,0.0,0.0)
	a1 = avgRating(user1)
	a2 = avgRating(user2)

	for movie in range(m):
		if(ratings[user1][movie] != 0 and ratings[user2][movie] != 0):
			a += (ratings[user1][movie] - a1) * (ratings[user2][movie] - a2)
			b += (ratings[user1][movie] - a1) ** 2
			c += (ratings[user2][movie] - a2) ** 2

	sim = a/(math.sqrt(b) * math.sqrt(c))
	return sim

def recommend(user):
	recom_movies = []

	for movie in range(m):
		if(ratings[user][movie] == 0):
			s = 0.0
			c = 0.0
			for user1 in range(u):
				if (ratings[user1][movie] != 0):
					pp = pearsonSimilarity(user,user1)
					s += pp * ratings[user1][movie]
					c += pp
			predicted = s/c
			recom_movies.append((movie,round(predicted,2)))

	recom_movies.sort(key=lambda tup: tup[1],reverse=True)
	return recom_movies[:5]

print(recommend(user))

