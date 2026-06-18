import pandas as pd
from numpy import *

irks = pd.read_csv("data/irks_ntol1e-06_w_stats.csv")

GL = irks[irks["rk_type"]=="GaussLegendre"]
Radau = irks[irks["rk_type"]=="RadauIIA"]

GL1 = GL[GL["rk_stages"] == 1]
GL2 = GL[GL["rk_stages"] == 2]
GL3 = GL[GL["rk_stages"] == 3]

Radau1 = Radau[Radau["rk_stages"] == 1]
Radau2 = Radau[Radau["rk_stages"] == 2]
Radau3 = Radau[Radau["rk_stages"] == 3]

day = 60*60*24

for i, dt in enumerate(GL1["dt"]):
    itsGL1 = GL1["Iterations per timestep"].iloc[i]
    itsGL2 = GL2["Iterations per timestep"].iloc[i]
    itsGL3 = GL3["Iterations per timestep"].iloc[i]

    totitsGL1 = itsGL1*day/dt
    totitsGL2 = itsGL2*day/dt
    totitsGL3 = itsGL3*day/dt

    print(f'{dt} & {itsGL1:.2f} & {totitsGL1:.2f} & {itsGL2:.2f} & {totitsGL2:.2f} & {itsGL3:.2f} & {totitsGL3:.2f} \\\\')

print("")
for i, dt in enumerate(Radau1["dt"]):
    itsRadau1 = Radau1["Iterations per timestep"].iloc[i]
    itsRadau2 = Radau2["Iterations per timestep"].iloc[i]
    itsRadau3 = Radau3["Iterations per timestep"].iloc[i]

    totitsRadau1 = itsRadau1*day/dt
    totitsRadau2 = itsRadau2*day/dt
    totitsRadau3 = itsRadau3*day/dt

    print(f'{dt} & {itsRadau1:.2f} & {totitsRadau1:.2f} & {itsRadau2:.2f} & {totitsRadau2:.2f} & {itsRadau3:.2f} & {totitsRadau3:.2f} \\\\')
