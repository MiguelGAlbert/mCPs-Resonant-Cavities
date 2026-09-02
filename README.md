# Millicharged-Dark-Matter Haloscope Recast

This repository contains the manuscript sources for a master thesis project. The code is used to recast published axion-photon haloscope limit data into projected sensitivity constraints on millicharged dark matter. C and power.ipynb also compute the mDM response to different cavity modes of a circular cylindrical cavity and CandPowerRec does the same for rectangular cavities.

The recast is intended to reproduce the haloscope sensitivity data shown in previous haloscope experiments. Experiments with splitted cavities are not suitable since in the mDM case the conducting walls may distorb the incident wave.

The output files contain two columns: the millicharged-dark-matter mass `m_phi` in eV and the corresponding fractional-charge limit `epsilon_m = e_m/e`.

IMPORTANT: The Axion-photon limits come from https://cajohare.github.io/AxionLimits/, as some of the base code.
