import re

Length_Dic = {}

CalculateExpress = []

RULE_PATTERN = '([a-z]+) = ([0-9]+\.?[0-9]*)'

PATTERN = re.compile('([-+]?[0-9]+\.?[0-9]*)([a-z]+)')

def inputHandler():
	isReadRule = True
	inputFile = file('./input.txt', 'r')
	for line in inputFile:
		if line == '\n':
			isReadRule = False
			continue
		if isReadRule:
			ruleGroup = re.search(RULE_PATTERN, line)
			if ruleGroup is not None:
				Length_Dic[ruleGroup.group(1)] = float(ruleGroup.group(2))
		else:
			CalculateExpress.append(re.sub(r'\n*', '', line))
	inputFile.closed


def convertLength(lengthSet):
	length = float(lengthSet[0])
	for key in Length_Dic.keys():
		if lengthSet[1].rfind(key) >= 0:
			length = Length_Dic[key] * length
			break
		elif 'feet' == lengthSet[1]:
			print(Length_Dic['foot'])
			length = Length_Dic['foot'] * length
			break
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
	inputHandler()
	outputFile = open('./output.txt', 'w')
	outputFile.writelines('yushio1984@gmail.com \n\n')
	for line in CalculateExpress:
		outputFile.writelines('%s\n' % calculateExpress(line))
	outputFile.closed

if __name__ == '__main__':
	main()
	

