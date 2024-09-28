#get the current date

from datetime import datetime

#calculate the volume tire

import   math

tire_volume = ""

width = float(input((f"Enter the width of the tire in mm(e.g:,205): ")))
aspect_ratio = float(input("Enter the aspect ratio of the tire (e.g., 60): "))
diameter = float(input("Enter the diameter of the wheel in inches (e.g., 15): "))


#the general formula for tire volume
tire_volume = (math.pi * width ** 2 * aspect_ratio * (width * aspect_ratio + 2540 * diameter))/10000000

print(f"The tire_volume is:{tire_volume:.2f}liters")

if tire_volume < float(width ** 2 * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) :
    print(f"The tire_volume is great.")
elif tire_volume >  float(width ** 2 * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) :
    print(f"The tire_volume is not great.")

else:
    print(f"Bad answer.")


current_date = datetime.now().date()


#open a volume.txt file
with open ("volume.txt" , "at") as volume_file:
    print(tire_volume, file=volume_file)
    print(f"{current_date}, {width}, {aspect_ratio}, {diameter}, {tire_volume:.2f}\n")



