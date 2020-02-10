import math

victim = [12.9246893731,77.566223144]

#possib = [12.92197576175, 77.567188739]

#raw_data.update()

# the raw_data is going to have the key=id , data = location[latitude,longitude]

raw_data = { 1235 : [12.92423972, 77.56808996] ,
			 '4512': [12.9252226806,77.56481766],
			 '12': [12.926613457,77.562618255],
			 '456213': [12.922869845,77.565021514]
 }



# sorted_data = {  }


def dictsort(data): 
	
	 global processed_data 
	 processed_data = {  } 
	   
	 # Note that it will sort in lexicographical order 
	 # For mathematical way, change it to float 
	 processed_data =  sorted(data.items(), key = lambda kv:(kv[1], kv[0]))
	 #print(processed_data)



#calculation of distance and updation of raw_data

for key in raw_data :

	vertical_distance = (victim[0]-raw_data[key][0]) * 111.363650794
	horizontal_distance = (victim[1]-raw_data[key][1]) * 111.363650794 * math.cos(victim[0])

	distance = math.sqrt((vertical_distance*vertical_distance) + (horizontal_distance * horizontal_distance))
	#print(distance)

	raw_data[key] = distance #updating the raw_data with distance.


#calling the sort function.
dictsort(raw_data)
print(processed_data)












