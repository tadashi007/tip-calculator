print("Welcome to tip calculator by tadashi\n")
bill=float(input("What was your bill ?\n"))
tip=float(input("how much you want to pay as tip 10,12,20 \n"))
people=int(input("Number of people\n"))
total=(bill+tip)/people
print(f"each have to pay total of {total}")