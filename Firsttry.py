
#Import data file into list of single characters
#can't figure out how to remove /n, but is workable for now

fO = open('smallfile.txt', 'rU')
lst = list(fO.read())
#print lst

#def split_list(alist, wanted_parts=1):
#    length = len(alist)
#    return [ alist[i*length // wanted_parts: (i+1)*length // wanted_parts] 
#             for i in range(wanted_parts) ]

def split_list(l, n):
    n = max(1, n)
    return [l[i:i + n] for i in range(0, len(l), n)]

#Dim parse uses split_list to create dimensional parse.
#so a square would be parsed into 1 list

num_dim = 6 #number of dimensions
lngth = int(len(lst)/num_dim)
dim_parse = split_list(lst, lngth)

print "Length of original array", len(lst)
print "Length of array holding dimensions", len(dim_parse)
print "length of an indvidual dimension dim_parse", len(dim_parse[0])

#plane_parse uses split_list to create a list for each height of the plane
#so a 4 X 4 square has heigh = 4, so 4 lists.

plane_depth = int(len((dim_parse[0])) ** 0.5) #need to find a way to tie this to number of dimensions and length of data
plane_depth_length = int((len(dim_parse[0]))/plane_depth)
print "Plane depth length", plane_depth_length
plane_parse = []

for i in range(0,len(dim_parse)):
    plane_parse.append(split_list(dim_parse[i], plane_depth_length))


print "Number of dimensions.", num_dim
print "Length of plane_parse array.", len(plane_parse)
print "Length of a single plane", len(plane_parse[0])
print "Length of a single height within plane", len(plane_parse[0][0])
#print plane_parse[0][0]
#print "XXXXXXXXXXXXXXXXXXX"
#print plane_parse[0]

#print plane_parse[0][1][0]
counter = 0
overshoots = 0
squares = 0
cubes = 0

#look for squares in current dimensional space
max_sqr_sz = 100
for n in range(1, max_sqr_sz):
    #print "square size ", n
    for d in range(0, len(plane_parse)):
        #print "dimension level ", d
        for p in range(0, len(plane_parse[d])):
            #print "plane height ", p
            topr = len(plane_parse[d][p])
            for c in range(0,topr):
                #print "character level", c
                pos = plane_parse[d][p][c]
                #print pos
                try:
                    if pos == plane_parse[d][p][c+n]:
                        counter = counter+1
                        #print "LINE FOUND"
                        #print "size =", n, " position = ", d,p,c
                        if pos == plane_parse[d][p+n][c]:
                            if pos == plane_parse[d][p+n][c+n]:
                                squares = squares + 1
                                for dl in range(0, len(plane_parse)):
                                    if pos == plane_parse[n+dl][p][c]:
                                        print "dimension 1 line found"
                                        if pos == plane_parse[n+dl][p+n][c]:
                                            print "dimension 1 something"
                                            if pos == plane_parse[n+dl][p][c+n]:
                                                print "FOUND CUBE!!!!!!!!!!"
                                                cubes = cubes + 1
                                                # doesn't capture cubes
                except IndexError:
                        overshoots = overshoots + 1                
        
    
    
print counter
print squares
print cubes
print overshoots

#create for / if loop that adds things to an array if they are equal
#can then report the length of the array to report how many dimensions the structure is
