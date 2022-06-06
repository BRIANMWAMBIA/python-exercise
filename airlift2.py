#First flight with passengers less than 100
class First_below(object):
	def below(self,data):
		minimum=100
		for key in data:
			size=len(data[key])
			if size>1:
				j=0
				while j<size:
					if int(data[key][j][2])<minimum:
						return ' '.join(data[key][j])
					j+=1
			elif data[key][0][2]<minimum:
				return ' '.join(data[key][0])

#Airline with the most total number of passengers
class Total (object):
	highest_total=0
	airline=""
	def total(self,data):
		for ky in data:
			total=0
			size=len(data[ky])
			if size>1:
				j=0
				while j<size:
					total+=int(data[ky][j][2])
					j+=1
			else:
				total+=int(data[ky][0][2])
			if total>self.highest_total:
				self.highest_total=total
				self.airline=ky
		return f"{self.airline} {self.highest_total}"
#Flight with the most passengers
class Most_passenger (object):
	def most_passengers(self,data):
		flight=[]
		most_passengers=0
		for key in data:
			l=len(data[key])
			if l>1:
				#loop
				i=0
				while i<l:
					passengers=int(data[key][i][2])
					if passengers>most_passengers:
						self.most_passengers=passengers
						self.flight=data[key][i]
					i+=1
			elif int(data[key][0][2])>most_passengers:
				self.most_passengers=int(data[key][0][2])
				self.flight=data[key][0]
		return ' '.join(self.flight)

	#Number of Flights to "Frankfurt"	
class flights_to_Frankfurt (object):
	count=0
	def flights (self,data):
		for key in data:
			l=len(data[key])
			if l>1:
				#loop
				i=0
				while i<l:
					if data[key][i][1]=="Frankfurt":
						self.count+=1
					i+=1
			elif data[key][0][1]=="Frankfurt":
				self.count+=1
		return self.count
#Openning and reading the input.txt
with open('document.txt', 'r') as file:
	f=file.readlines() 
	#thislist = list(txt)
	newlist = []
	#removing the escape chareacters from the list
	for line in f:
		 if line[-1] == '\n':
		     newlist.append(line[:-1])
		 else:
			 newlist.append(line)
	#print(len(newlist))
	#print(newlist)
	i=0
	
	length=len(newlist)
	data={}
	#print(length)
	#creating a dictionary of the flights
	while i<length:
		#print(i)
		record=newlist[i].split(" ")
		#print(record)
	
		if record[0] in data.keys():
			#print("yes")

			value=data[record[0]]
			#print(value)
			value.append(record)
			#print(value)
			data[record[0]]=value
			#print(data[record[0]])
		else:
			data[record[0]]=[]
			data[record[0]].append(record)
		i+=1
	
	#Answers
#Airline with the most total number of passengers
	totalInstance=Total()
	total_highest=totalInstance.total(data)
	#First flight with passengers less than 100
	minimumInstance=First_below()
	minimum=minimumInstance.below(data)	
	#Number of Flights to "Frankfurt"	
	frankfurtInstance= flights_to_Frankfurt()
	frankfurt=frankfurtInstance.flights(data)
	#Flight with the most passengers
	most_passengersInstance= Most_passenger()
	most_passenger=most_passengersInstance.most_passengers(data)
	
	
#stdout
	#print(count)
	#print(trip)
	print(frankfurt)
	print(most_passenger)
	print(minimum)
	print(total_highest)
	
	
   




		
		
   
	 
	
	