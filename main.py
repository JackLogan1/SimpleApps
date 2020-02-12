print("Version 1.0")
print("What would you like to do?")
print("1.Solve a Problem")
print("2.Write Something")
print("3.Countdown from a number")
print("4.Instructions")
choice = input()
if choice == '1': 	
	import calc	
elif choice == '2': 
	import word
elif choice == '3': 
	import timer
elif choice == '4':
	import instructions
else: 
	print("Can't do that")