if __name__ == "__main__":
	main()
	import numpy as np
	import random

	# Using Python 3 for division

	x= np.random.randint(1,7)
	print (x)
	y= np.random.randint(1,7)
	print (y)

	counter=0
	for i in range (1000000):
	    x= np.random.randint(1,7)
	    y= np.random.randint(1,7)
 	   if x==6:
	        if y==6:
            counter=counter+1
	fraction = counter/1000000
	print (fraction,"or", Fraction(counter/1000000))
	print ("Difference from 1/36 is ", abs(fraction - (1/36)))

