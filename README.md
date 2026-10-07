# Millicharged-Dark-Matter Haloscope Recast

This repository contains the manuscript sources for a master thesis project. The code is used to recast published axion-photon haloscope limit data into projected sensitivity constraints on millicharged dark matter. C and power.ipynb also compute the mDM response to different cavity modes of a circular cylindrical cavity and Rectangular_CandPower.ipynb does the same for rectangular cavities.

The recast is intended to reproduce the haloscope sensitivity data shown in previous haloscope experiments. Experiments with splitted cavities are not suitable since in the mDM case the conducting walls may distorb the incident wave.

The output files contain two columns: the millicharged-dark-matter mass `m_phi` in eV and the corresponding fractional-charge limit `epsilon_m = e_m/e`.

IMPORTANT: The Axion-photon limits come from https://cajohare.github.io/AxionLimits/, as some of the base code.

Aditional information:
The cavity parameters used for the computation of the inferred sensitivity are compiled in the following table:

<img width="926" height="407" alt="image" src="https://github.com/user-attachments/assets/f555bcd5-58b8-41bc-9b90-58c344fd5078" />

Here ``n.s.'' denotes that no single representative value is specified for the corresponding data set. The legacy ADMX entry is retained because it is included in the plot, with the radius assumed to be a=0.21m. Entries lacking either a usable published form factor C or a cavity radius are omitted from the table because they are not included in the plot. The main-cavity radius follows the ADMX resonator geometry described. For the later main-cavity runs, the quoted 106L is the empty volume entering the axion-power normalization after excluding the tuning rods, whereas the geometric barrel volume remains approximately 139L for a=0.2095m and length 1.014m. For HAYSTAC, a=0.051m follows from the 10.2cm inner diameter of the cylindrical cavity, whereas the Phase II volume is the unfilled volume after excluding the tuning rod. The Phase IIc,d Q_L value is inferred from the reported averages Q_0~44000 and beta~8.5. In applying the mass rescaling, the TE_{011} frequency is evaluated using the corresponding ideal cylindrical dimensions; for Sidecar and the simple cylindrical QUAX entries, the effective length is inferred from the listed volume and radius. The CAPP-1 values correspond to CAPP-8TB; CAPP-6 to the DFSZ-sensitive CAPP-12TB run; CAPP-9 to the tunable TM_020 search; and CAPP-MAX to the combined wide scan with the 37L cavity. The quoted CAPP-MAX diameter is the outer diameter of its thin-wall cavity. ORGAN Phase~1a uses a cylindrical tuning-rod cavity, whereas Phase~1b uses a rectangular box cavity with a movable wall. All cylindrical configurations are projected onto TE_{011}. ORGAN Phase~1b is instead mapped from
TM_{110} to TE_{201} because of its rectangular cavity geometry. For CAPP-MAX, the reported range corresponds to Q_0, whereas Q_L is measured point by point. The 106L ADMX and 1.545L HAYSTAC values are the unfilled volumes used in their axion-power normalizations.
