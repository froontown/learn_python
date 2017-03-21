def make_sammich(*ingredients):
	print("This sammich has got:")
	for ingredient in ingredients:
		print(f"- {ingredient}")

make_sammich('bacon', 'turkey', 'avocado', 'lettuce', 'tomato', 'mayo', 'honey mustard', 'tobasco', 'alfalfa sprouts')

print('====')

def build_profile(first, last, **data):
	profile={}
	profile ['first_name'] = first
	profile ['last_name'] = last
	for k, v in data.items():
		profile[k] = v
	return profile

my_profile = build_profile('froon', 'town', address='massachusetts', height='normal', sense_of_humor='through the roof')
print(my_profile)