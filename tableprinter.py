print("\t \t \t NAME: VAJRESH SHENOY\n\t \t \t USN: 1AY24AI034 \n\t \t \t SEC:'M'")
table_data = {
    "fruits":' apples oranges cherries banana',
    "name":' Alice  Bob     Carol    David',
    "animals":' dogs   cats    moose    goose'
}

for i,j in table_data.items():
	print(i.ljust(10),end='')
	print(j.rjust(20),end='\n')
