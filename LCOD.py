import numpy as np

capex = 28014 # EUR/kW
Pe =  16700 # kWe
r = 0.08
hours_in_a_year = 8765.81277
Cp = 0.94
el_price = 70 # EUR/MWh
Power_consumption = 0.43 # kWh/kg CO2

CO2 = np.ones(31) * Pe * hours_in_a_year * Cp/Power_consumption # kg
COE = np.ones(31) * Pe * 0.001 * hours_in_a_year * Cp * el_price # EUR
OPEX = np.ones(31) * capex * Pe * 0.06 # EUR
CAPEX = np.zeros(31)

CO2[0] = 0
COE[0] = 0
OPEX[0] = 0
CAPEX[0] = capex * Pe

for i in range(1, 31):
    CO2[i] = CO2[i]/((1 + r)**i)
    COE[i] = COE[i]/((1 + r)**i)
    OPEX[i] = OPEX[i]/((1 + r)**i)
    CAPEX[i] = CAPEX[i]/((1 + r)**i)

LCOD = sum(COE+CAPEX+OPEX)/sum(CO2)
print(F"LCOD {LCOD} EUR/kg")