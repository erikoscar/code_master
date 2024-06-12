import numpy as np
import LCOH
import LCOD

capex = 7388 # EUR/kW
Pe = 36600 # kWe
r = 0.08
hours_in_a_year = 8765.81277
Cp = 0.94
el_price = 70 # EUR/MWh
power_consumption = 0.736 # kWh/kg fuel

Fuel = np.ones(31) * Pe * hours_in_a_year * Cp/power_consumption # kg
COE = np.ones(31) * Pe * 0.001 * hours_in_a_year * Cp * el_price # EUR
OPEX = np.ones(31) * capex * Pe * 0.06 # EUR
CAPEX = np.zeros(31)

Fuel[0] = 0
COE[0] = 0
OPEX[0] = 0
CAPEX[0] = capex * Pe

for i in range(1, 31):
    Fuel[i] = Fuel[i]/((1 + r)**i)
    COE[i] = COE[i]/((1 + r)**i)
    OPEX[i] = OPEX[i]/((1 + r)**i)
    CAPEX[i] = CAPEX[i]/((1 + r)**i)

LCOFT = sum(COE+CAPEX+OPEX)/sum(Fuel)


print(f"LCOFT: {LCOFT} EUR/kg")
print(f"LCOEF: {LCOD.LCOD + LCOH.LCOH + LCOFT} EUR/kg")