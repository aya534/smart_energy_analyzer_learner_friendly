#step: inputs from the user

price= float(input("Plz enter the price per Kwh: "))
total_daily_kwh= 0
count= 0
names= []
kwh_daily_list= []
watts_list= []
hours_list= []
DAYS= 30
BUDGET= 50
TIER_LIMIT = 300
TIER_MULTIPLIER = 1.5

#Menu for the user
while True:
      print()
      print("1. Add Appliance")
      print("2. View total")
      print("3. Exit")
      choice= input("Enter your choice: ")

      #The process of adding an appliance
      if choice == "1":
            name= input("Appliance name: ").strip().title()
            if name in names:
                print(name, "is already added!")
                continue        

            watts= float(input("Power (watts): "))
            while watts <= 0:                                   
                print("Watts must be more than 0!")                
                watts= float(input("Power (watts): "))

            hours= float(input("Hours per day: "))
            while hours <= 0 or hours > 24:
                print("Hours must be between 0 and 24!")
                hours= float(input("Hours per day: "))

            kwh_daily= (watts * hours)/1000
            total_daily_kwh= total_daily_kwh + kwh_daily
            count= count + 1

            names.append(name)   
            watts_list.append(watts)
            hours_list.append(hours)
            kwh_daily_list.append(kwh_daily)

            print("Added", name)
            print("Short code:", name[:3].upper())

      #The process of viewing total
      elif choice == "2":
            monthly_kwh= total_daily_kwh * DAYS
            if monthly_kwh <= TIER_LIMIT:
                cost = monthly_kwh * price
            else:
                normal_part = TIER_LIMIT * price
                extra_part = (monthly_kwh - TIER_LIMIT) * price * TIER_MULTIPLIER
                cost = normal_part + extra_part

            print("Appliances:", count)
            print("Monthly energy:", monthly_kwh, "Kwh")
            print("Monthly cost:", cost)
            if cost > BUDGET:
                print("Warning: Your monthly cost exceeds your budget ")

            print("Names:", names)
            print("Power (watts):", watts_list)
            print("Hours:", hours_list)
            print("Daily energy (kWh):", kwh_daily_list)

            if len(names) > 0:
                print("Max daily energy:", max(kwh_daily_list))
                print("Min hours:", min(hours_list))
                print("All names:", ", ".join(names))

            longest= names[0]
            for n in names:
                if len(n) > len(longest):
                    longest= n
            print("Longest name:", longest, "-", len(longest), "letters")

      #stopping the program
      elif choice =="3":
           print("See you later!")
           break

      else:
           print("Invalid choice. Please try again.")


