age = int(input("Enter your age: ")) 
# we use int() to convert the user's input, which is initilly a string, int0 an integer 
std = input("Are you student(yes or no): ").lower()
if age <= 12:
    print("You are elegible for a discount on the movie ticket.")
elif 13 <= age <=18 and std == "yes" :
    print("You are elegible for a discount on the movie ticket.")
else :
    print("You are elegible for a discount on the movie ticket. ")