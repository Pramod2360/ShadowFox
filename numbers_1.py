formatted = format(145, 'o')
print("format(145, 'o') ->", formatted)
print("Representation used: octal")
r = 84
pi = 3.14
area = pi * r * r
water_liters = area * 1.4
print("\nPond area (sqm):", area)
print("Total water (liters) - without decimal:", int(water_liters))
distance = 490  
time_min = 7
time_sec = time_min * 60
speed_m_s = distance / time_sec
print("\nSpeed (m/s) without decimal:", int(speed_m_s))