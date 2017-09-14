reader = open("occupations.csv", "r")
data = reader.read()
#print data
reader.close()

dataList = data.split('\r\n')
dataList = dataList[:-1]
print dataList

dict = {}
for x in dataList:
    if x[0] == '"':
        temp = x.split('"')
        dict[temp[1]] = temp[2][1:]

print dict
        


