old_print = print()

def print(object_u):
	global result
	result = object_u 

def run_user_script():
	result = "Нәтиже result деген айнымалыға сақталу керек"
	result = 5 + 5
	return result