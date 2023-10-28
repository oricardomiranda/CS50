class Cat:
	MEOWS = 3 #This indicates a constant. But not mandatory, just convention

	def meow(self):
		for _ in range(Cat.MEOWS):
			print("meow")

cat = Cat()
cat.meow()
