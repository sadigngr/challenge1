import sys

def read(path,sample = ""):
	a,t,g,c = 0,0,0,0
	dnaDict = {}
	dnaList = []
	tagList = []
	ilk = True
	with open(path, 'r') as f:
		for l in f.readlines():
			if l[0] != ">":
				a += l.count('A')
				t += l.count('T')
				g += l.count('G')
				c += l.count('C')
			else:
				tagList.append(l)
				dnaList.append((a,t,g,c))
				a,t,g,c = 0,0,0,0

		dnaList.append((a,t,g,c))
		
		for i in range(len(tagList)):
			dnaDict[tagList[i].strip()] = dnaList[i+1]

	if sample != "":
		try:
			return dnaDict[str(sample)]

		except KeyError:

			print("Girdiğiniz örnek, dosyada yer almıyor.")
	else:
		return dnaDict

if __name__ == '__main__':
	try:
		print(read(sys.argv[1],sys.argv[2]))
	except IndexError:
		print(read(sys.argv[1]))