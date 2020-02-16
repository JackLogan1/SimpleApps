print("Version 1.0")
print("What would you like to do?")
print("1.Calculator")
print("2.Time App")
print("3.Breathing Session")
choice = input("Choice:")
if choice == '1': 
	import calc	
elif choice == '2': 
	import timeapp
elif choice == '3': 
	import breath
else: 
	print("Can't do that")