import numpy as np

capex_plant = 322 # EUR/kW
capex_stack = 170.2 # EUR/kW
Pe = 1486500 # kW
r = 0.08
hours_in_a_year = 8765.81277
Cp = 0.94
el_price = 70 # EUR/MWh
efficiency = 50 # kWh/kg H2

H2 = np.ones(31) * Pe * hours_in_a_year * Cp/efficiency # kg
COE = np.ones(31) * Pe * 0.001 * hours_in_a_year * Cp * el_price # EUR
OPEX = np.ones(31) * capex_plant * Pe * 0.05 # EUR
CAPEX = np.zeros(31)


H2[0] = 0
COE[0] = 0
OPEX[0] = 0
CAPEX[0] = capex_plant * Pe
CAPEX[9] = capex_stack * Pe
CAPEX[18] = capex_stack * Pe
CAPEX[27] = capex_stack * Pe

for i in range(1, 31):
    H2[i] = H2[i]/((1 + r)**i)
    COE[i] = COE[i]/((1 + r)**i)
    OPEX[i] = OPEX[i]/((1 + r)**i)
    CAPEX[i] = CAPEX[i]/((1 + r)**i)

LCOH = sum(COE+CAPEX+OPEX)/sum(H2)
print(F"LCOH {LCOH} EUR/kg")
