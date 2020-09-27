
f = open("2_fixed_data.json" , 'a')


for n in range(10,45) :
	corr_f = open("D:/epic/py/tram/trash/falied_3/"+str(n)+"_data.json")
	fix_tool = corr_f.readlines()
	for x in fix_tool :
		f.write(str(x))
	print(f"file {n} attached")
	corr_f.close()

f.close()
print("done")