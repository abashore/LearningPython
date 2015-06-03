__author__ = 'Adam'

# integer variable
cars = 100

# floating point variable
space_in_a_car = 4.0

# integer variable
drivers = 30

# integer variable
passengers = 90

# simple math subtracting drivers from the total number of cars
cars_not_driven = cars - drivers

# storing information about which cars will have drivers
cars_driven = drivers

# total number of cars with drivers multiplied by seats in each car.
carpool_capacity = cars_driven * space_in_a_car

# this is dividing all the passengers by the number of cars that have drivers.
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

