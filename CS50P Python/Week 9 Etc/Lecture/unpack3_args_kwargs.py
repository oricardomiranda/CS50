def f(*args, **kwargs): #It will pass all arguments like a dictionary
	print("Named:", kwargs)


f(galleons=100, sickles=50, knuts=25)
