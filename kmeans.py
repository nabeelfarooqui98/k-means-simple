import numpy as np

#hardcoded values
centroids = np.array([[1, 1], [ 5, 7] , [3.5,4.5 ]])
#points = np.array([ [1, 1], [1.5, 2] ,[3, 4] , [5, 7] , [3.5, 5] , [4.5, 5] , [3.5, 4.5]])

points = []

#load from file
file_in = open('datapoints.txt', 'r')
a = file_in.readlines()

num_points = int(a[0])

for i in range(1,num_points+1):
	c= float( a[i].split()[0] )
	d= float ( a[i].split()[1] )
	points.append( list( (c,d ) ) )

points = np.array(points)
#print(points)
#print(num_points)
#print(list( (a,b) ))
#for y in file_in.readlines():
#	(a,b) = 

num_cen = int(a[num_points+1])

for i in range(num_points+2,num_cen+1):
	c= float( a[i].split()[0] )
	d= float ( a[i].split()[1] )
	centroids.append( list( (c,d ) ) )

centroids = np.array(centroids)


#######3 END READING FROM FILE

point_centroid = {} #blank dict
for index_p , p in enumerate(points):
	#assign all points to cluster -1 by defaul
	#convert to tuple first because dict cant use numpy array
	point_centroid[tuple(p)] = -1 

#print(point_centroid)

#print(centroids)
#print(points)

#blank 2d matrix for distances
dist = [[None for _ in range(len(centroids))] for _ in range(len(points))]

for index_c , c in enumerate(centroids):
	for index_p , p in enumerate(points):
		#calculate euclidean dist between every centroid and point
		dist[index_p][index_c] = np.linalg.norm(c - p) 
		

#convert dist to ndarray
dist = np.array(dist)
min_dists = dist.min(axis=1) #returns list. min of every point

#for every point, assign a centroid
for index_p , p in enumerate(points):
	#find min dist
	which_centroid = np.where( dist[index_p] == min_dists[index_p] )[0][0] #[0][0] is to get actual value 
#	print(min_dists[index_p])
#	print(which_centroid)

	point_centroid[tuple(p)] = which_centroid

print(point_centroid)

#calculate new centroids
#1. delete previous
#2. add new
for index_c , c in enumerate(centroids):
	 
	temp_list = []
	#if this point belongs to this centroid, then use it to update the position of this centroid
	for x in point_centroid:
		if point_centroid[x] == index_c: 
			temp_list.append(list(x))

	avg = np.mean(temp_list , axis=0)
	print("new centroid" , avg)
	pass


