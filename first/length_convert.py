import re

Length_Dic = {
	'inches' : 0.0254,
	'feet' : 0.3048,
	'yards' : 0.9144,
	'miles' : 1609.344,
	'centimeters' : 0.01,
	'meters' : 1,
	'kilometers' : 1000
}

PATTERN = re.compile('([-+]?[0-9]+\.?[0-9]*)([a-z]+)')

def convertLength(lengthSet):
	length = float(lengthSet[0])
	unit = lengthSet[1]

	length = Length_Dic[unit] * length
	return length

def calculateExpress(expressStr):
	adjustExpress = re.sub(r'\s', '', expressStr)
	adjustExpress = re.sub(r'--', '+', adjustExpress)
	adjustExpress = re.sub(r'\+-', '-', adjustExpress)
	adjustExpress = re.sub(r'-\+', '-', adjustExpress)
	adjustExpress = re.sub(r'\+\+', '+', adjustExpress)

	expressGroup = re.findall(PATTERN, adjustExpress)
	calculateList = []
	for expressItem in expressGroup:
		calculateList.append(convertLength(expressItem)) 
		
	result = sum(calculateList)
	return '%.2f m' % result

def main():
	outputFile = open('./output.txt', 'w')
	outputFile.writelines('yushio1984@gmail.com \n\n')
	inputFile = file('./input.txt', 'r')
	for line in inputFile:
		outputFile.writelines('%s\n' % calculateExpress(line))
	outputFile.closed
	inputFile.closed

if __name__ == '__main__':
	main()
	

