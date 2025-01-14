motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
# motorcycles.append('ducati')
# print(motorcycles)
motorcycles.insert(0, 'ducati')
print(motorcycles)
# del motorcycles[0]
# print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(popped_motorcycle)
last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
# motorcycles.remove('ducati')
# print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")