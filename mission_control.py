agent_name = "jj"
mission_code = 654213
distance_to_target = 18.5
mission_active_status = True
print(f"agent name:{agent_name}, mission code:{mission_code}, distance to target:{distance_to_target}, mission active status:{mission_active_status}")
print(type(agent_name))
print(type(mission_code))
print(type(distance_to_target))
print(type(mission_active_status))
travel_distance = distance_to_target*2
print(f"travel distance:{travel_distance}")
fuel_usage = 1 #liret/KM
fuel_needed = fuel_usage*travel_distance
print(f"fuel needed:{fuel_needed}")
total_fuel = 150
remaining_fuel = total_fuel-fuel_needed
print(f"remaining fuel:{remaining_fuel}")


