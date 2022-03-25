
total_heads = int(input("Enter number of heads :"))
total_legs = int(input("Enter number of legs :"))

if total_legs < total_heads or total_legs == 0 or total_heads == 0 or total_legs % 2 != 0:
    print("Invalid input !")
else:
    rabbits = (total_legs - (2 * total_heads)) / 2
    chickens = total_heads - rabbits
    print("Number of Rabbits in farm are : " + str(rabbits))
    print("Number of Chickens in farm are : " + str(chickens))
