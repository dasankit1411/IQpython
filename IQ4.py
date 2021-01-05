#Write a Python program to sort a list of dictionaries using Lambda.
#Original list of dictionaries
d1=[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2',
'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
sort_d=sorted(d1,key=lambda x:x["color"])
print(sort_d)