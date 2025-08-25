# --car specifications 

engine_type ="mHawk (CRDi)"
displacement = "2198 cc"
max_power = "172.45bhp@3500 rpm"
max_torque = "400 Nm @ 1750-2750 rpm"
cylinders = 4
valves_per_cylinder = 4
turbo_charger = True
transmission = "Automatic"
gearbox = "6-Speed"
driver_type = "4WD"

# car specifications using f-strings

print(f" ---- Car  Specifications -----")
print(f"Engine Type       :   {engine_type} ")
print(f"Displacement      :   {displacement}   ")
print(f"Max Power         :   {max_power}") 
print(f"Max Torque        :   {max_torque}")
print(f"No. of Cylinders  :   {cylinders}")
print(f"Valves per Cylinder:  {valves_per_cylinder}")
print(f"Turbo Charger     :   {'Yes' if turbo_charger else 'No'}")
print(f"Transmission Type :   {transmission}")
print(f"Gearbox           :   {gearbox}")
print(f"Drive Type        :   {driver_type}")


