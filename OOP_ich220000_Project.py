#!/usr/bin/env python
# coding: utf-8

# In[1]:


MAX_RENTAL_PERIOD = 24

DISCOUNT_THRESHOLD = 2
DISCOUNT_PERCENT = 15   

HOURLY_RATE = 10
DAILY_RATE = 20  
WEEKLY_RATE = 50


class ScooterRentalShop:

    def __init__(self, num_scooters):
        self.num_scooters = num_scooters
        self.rented_scooters = 0

    def display_rental_options(self):
        print(f"""
        Scooter Rental Options: (max 24 hours)  
        1. Rent hourly (Rate: $10/hour)
        2. Rent daily (Rate: $20/day)     
        3. Rent weekly (Rate: $50/week)
        """)

    def rent_scooters(self, num_scooters, rental_time, num_periods=1):
        if self.rented_scooters + num_scooters > self.num_scooters:
            print("Sorry, we only have {} scooters available to rent.".format(self.num_scooters - self.rented_scooters))
            return

        if rental_time == 1 and num_periods > MAX_RENTAL_PERIOD:
            print(f"Cannot rent for more than {MAX_RENTAL_PERIOD} hours")
            return

        if rental_time == 1:
            rental_duration = "hour"
            amount_due = HOURLY_RATE * num_scooters * num_periods
       
        elif rental_time == 2:
            rental_duration = "day"
            amount_due = DAILY_RATE * num_scooters * num_periods
   
        elif rental_time == 3:
            rental_duration = "week"
            amount_due = WEEKLY_RATE * num_scooters * num_periods

        if num_scooters > DISCOUNT_THRESHOLD:  
            discount = amount_due * (DISCOUNT_PERCENT/100)
            amount_due -= discount
            print("You qualify for a {}% discount!".format(DISCOUNT_PERCENT))

        print("Renting {} scooter(s) for {} {}. Total amount due: ${}".format(num_scooters, num_periods, rental_duration, amount_due))
        
        self.rented_scooters += num_scooters
    def return_scooters(self, num_scooters):
        if self.rented_scooters < num_scooters:
            print("Cannot return more scooters than currently rented!")
            return
        
        print("Thanks for returning the scooter(s)!")
        self.rented_scooters -= num_scooters
    
    def emergency_stop(self):
        print("Emergency stop initiated. Ending program.")
        exit()
        
def main():

    shop = ScooterRentalShop(100)
    
    while True:
        shop.display_rental_options()
        
        customer_name = input("Enter customer name: ")
        num_scooters = int(input("How many scooters would you like to rent? "))        
        rental_time = int(input("For how long (Enter 1 for hour, 2 for day, or 3 for week)? ")) 
        
        if rental_time == 1:
            rental_duration = "hour"
        elif rental_time == 2:
            rental_duration = "day"
        elif rental_time == 3:
            rental_duration = "week"

        num_periods = int(input("For how many {} (1, 2, etc.)? ".format(rental_duration)))  
        print()
        
        shop.rent_scooters(num_scooters, rental_time, num_periods)
        
        return_scooters = input("Would you like to return scooters (y/n)? ")
        if return_scooters == 'y':
            num_return = int(input("How many scooters would you like to return? "))
            shop.return_scooters(num_return)
            
        stop = input("Continue rentals (y/n)? ") 
        print()
        if stop != 'y':
            break
        
    shop.emergency_stop()
        
if __name__ == "__main__":
    main()


# In[ ]:





# In[ ]:





# In[6]:





# In[ ]:





# In[ ]:




