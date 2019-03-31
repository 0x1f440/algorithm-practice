stick = 0
part = 0
counter = 0

x = str(input())

while counter+1 < x.__len__():
	if x[counter] == '(':
		if x[counter+1] == '(':
			stick = stick + 1
			part = part + 1
		else:
			part = part + stick
			counter = counter + 1
	else:
			stick = stick - 1

	counter = counter + 1

print(part)