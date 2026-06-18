# Part 1
#1
agent_name = "jj"
mission_code = 654213
distance_to_target = 18.5
mission_active_status = True
#2
print(f"agent name:{agent_name}, mission code:{mission_code}, distance to target:{distance_to_target}, mission active status:{mission_active_status}")
#3
print(type(agent_name))
print(type(mission_code))
print(type(distance_to_target))
print(type(mission_active_status))
#4
travel_distance = distance_to_target*2
print(f"travel distance:{travel_distance}")
#5
fuel_usage = 1 #liret/KM
fuel_needed = fuel_usage*travel_distance
print(f"fuel needed:{fuel_needed}")
#6
total_fuel = 150
remaining_fuel = total_fuel-fuel_needed
print(f"remaining fuel:{remaining_fuel}")
#7
countdown_conversion = input("How long until your mission start in seconds?")
countdown_conversion = int(countdown_conversion)
conversion_to_minutes = countdown_conversion / 60
conversion_to_hours = conversion_to_minutes / 60
print(f"your mission start at {conversion_to_hours} hours in a minutes {conversion_to_minutes} in a seconds {countdown_conversion}")
#8
distance_formatting = input("How far is it in KM?")
distance_formatting = int(distance_formatting)
distance_at_mails = distance_formatting*0.6
print(f"distance at mails:{distance_at_mails}")
#9
update_agent_name = input("give me new name?")
print(f"agent new name:{update_agent_name} ,agent old name:{agent_name}")
