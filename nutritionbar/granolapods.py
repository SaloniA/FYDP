import A4988

def newRequestCallback(pval, fval, cval):
	print("New Request Received:")
	print("Protein: " +str(pval) + "%")
	print("Fat: " +str(fval) + "%")
	print("Carbs: " + str(cval) + "%")
	#Insert code to execute when a new request is received.

	#Recipe selection
	# Controller 1 for cup dispenser
	# Controller 2 for dispenser 1 
	# Controller 3 for dispenser 2
	# Controller 4 for dispenser 3
	# Controller 5 for gantry cart motor 

	A4988.turnMotor(left, 200, 1) #cup dispenser

	A4988.turnMotor(right, 100, 5) #until hall effect sensor triggered

	A4988.turnMotor(dir, steps, 2) #dispenser 1, according to recipe

	A4988.turnMotor(dir, steps, 5) #until next hall effect sensor triggered

	A4988.turnMotor(dir, steps, 3) #dispenser 2 according to recipe

	A4988.turnMotor(dir, steps, 5) #until final hall effect sensor

	A4988.turnMotor(dir, steps, 4) #dispenser 3 according to recipe

	A4988.turnMotor(dir, steps, 5) #until limit switch at end

	A4988.turnMotor(dir, steps, 5) #until first limit switch - reset

