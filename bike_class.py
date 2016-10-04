class Bike(object):
	def __init__(self, price, max_speed):
		print "Created a new Bike!!!"

		self.price = price
		self.max_speed = max_speed
		self.miles = 0

	def displayInfo(self):
		print "Price:\t\t\t", self.price
		print "Max Speed:\t\t", self.max_speed
		print "Total Miles:\t", self.miles

	def ride(self):
		print "Riding..."
		self.miles += 10
		print "Current mileage:", self.miles

	def reverse(self):
		print "Reversing..."
		if self.miles > 5:
			self.miles -= 5
		else:
			self.miles = 0
		print "Current mileage:", self.miles

huffy = Bike("$40", "88MPH")
# huffy.displayInfo()
huffy.ride()
huffy.reverse()
huffy.reverse()
huffy.reverse()


