months = {0:"Jan", 1:"feb"}
print(months.get(0,"not a key"))
print(months.get(3,"not a key"))

for key in months.keys():
    print(key)

for val in months.values():
    print(val)

for key, val in months.items():
    print("{}   :  {}".format(key,val))