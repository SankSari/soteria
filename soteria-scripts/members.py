def findMembers(volunteerList, memberList):
	# takes a json of member ids and their distances from the volunteer as json
	count = 0
	memcount = 0
	finalList = []
	# memberlist.sort()
	for key in memberList:
		# if(memcount > 10):
			# break
		print(memcount)
		finalList[count].append(memberList[memcount]['id'])
		if(memcount%10 == 0):
			count = count + 1
		memcount = memcount + 1
	print (finalList)

findMembers(21, [{ 'id': 1, 'dist':200 }, { 'id': 2, 'dist': 300}])