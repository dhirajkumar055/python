glob=78
def globally():
 glob=7
 print(glob)
 global glob
 glob=4
 print(glob)
globally()
print(glob)
