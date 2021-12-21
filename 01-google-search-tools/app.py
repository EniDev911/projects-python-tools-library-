from googlesearch import search


print('Welcome to the Google search tools\n\n')


query = input("What do you want to google:\n")
results = []
print()
# Iterating the results
for i in search(query, start=0, stop=10):
	print(i)
	results.append(i)

	with open('results.txt', 'w+') as xfile:
		for j in results:
			xfile.write('%s\n' % j)

print()
