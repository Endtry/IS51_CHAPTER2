# print("one", "two", "three", sep=", ")
# print("Hello", end=" ")
# print("World!")
# print("a\tb\tc")
# print("a\tb\tc\nd\te\tf")
# print("\\Hello World!\\") # "Hello World!"
str1 = "There are {0}% probability that the stock market will crash tomorrow and {1}% probability that it will rally!"
print(str1.format(10, 50))

print("{0:^5s}{1:<20s}{2:>3s}".format("Rank", "Player", "HR"))
print("{0:^5n}{1:<20s}{2:>3n}".format(1, "Barry Bonds", 762))
print("{0:^5n}{1:<20s}{2:>3n}".format(1, "Barry Bonds", 762))
print("{0:^5n}{1:<20s}{2:>3n}".format(1, "Barry Bonds", 762))

str2 = "The population of {0:s} is {1:.2%} of the U.S. population."
print(str2.format("Texas", 26448000/309000000))

# Of the total U.S population, 8.56% of households resides in Texas

print("Of the total U.S population, {0:.2%} of households resides in {1:s}".format(26448000/309000000, "Texas"))