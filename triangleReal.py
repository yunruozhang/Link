endString = input("请输入边界值:")
startValue = 1
while int(endString) and int(endString) >= 3 :
	endValue = int(endString)
	triImg = []
	triImgLine = []
	index = startValue
	indexLine = startValue 
	
	while index <= endValue :
		while indexLine <= index :
			if indexLine == 1 :
				if index == 1 :
					triImgLine.append("")
				else :	
					triImgLine.append("|")
			elif indexLine > 1 and indexLine < index :
				if index == endValue :
					triImgLine.append("_")
				else :
					triImgLine.append(" ")
			else :
				triImgLine.append("\\")
			indexLine = indexLine + 1
		triImg.append(triImgLine)
		triImgLine = [] 
		indexLine = startValue
		index = index + 1

	for element in triImg :
		for elementLine in element :
			print(elementLine,end='')
		print("")

	endString = input("请输入边界值:")
