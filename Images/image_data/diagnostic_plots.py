from numpy import *
import matplotlib.pyplot as pp
import pandas as pd

files = [("w5_diagnostics.csv", "Williamson 5"),
         ("w6_diagnostics.csv", "Williamson 6")]

Area = 6371220**2*4*pi

for ff in files:
    df = pd.read_csv(ff[0])
    Energy0 = df["Energy"][0]
    df['Normalised Divergence'] = df.apply(
        lambda row: row.Divergence/Area**0.5, axis=1)
    df.plot(x="Step", y="Energy", xlabel="Timestep",
            ylabel="Relative Energy Error", title=ff[1])
    pp.show()

    df.plot(x="Step", y="Normalised Divergence", xlabel="Timestep",
            ylabel="Divergence RMS", title=ff[1])
    pp.show()
