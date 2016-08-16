if __name__ == "__main__":
	main()
	import numpy as np
	
	G= 6.67 * 10 **-11
	M= 5.97 * 10 **24
	R= float(6371000)
	
	T= float(input("Time in seconds"))
	h = (((G * M * (T**2)) / (4 * (np.pi)**2))**(1/3)) - R
	print (h, "meters")

	T_day = float (24*60*60)
	T_sidereal = float (23.93 *60 *60)
	h_day = (((G * M * (T_day **2)) / (4 * (np.pi)**2))**(1/3)) - R
	h_sidereal= (((G * M * (T_sidereal **2)) / (4 * (np.pi)**2))**(1/3)) - R
	difference = h_day - h_sidereal
	print (difference, "meters")