# Do some NVT heating
gmx grompp -v -f charmm_nvt_heat.mdp -c protein-EM-solvated-ion.gro -p protein.top -o protein-PR.tpr
gmx mdrun -v -deffnm Heat_NVT -s protein-PR.tpr
######################################################################################################
# Do some NPT equilibration
gmx grompp -v -f charmm_npt_eq.mdp -c Heat_NVT.gro -t Heat_NVT.cpt -p protein.top -o protein-PR-NVT.tpr
gmx mdrun -v -deffnm Heat_NPT -s protein-PR-NVT.tpr
######################################################################################################
# Do some NPT production
gmx grompp -v -f charmm_npt_prod.mdp -c Heat_NPT.gro -t Heat_NPT.cpt -p protein.top -o protein-PR-NPT.tpr
gmx mdrun -v -deffnm Heat_NPT_prod -s protein-PR-NPT.tpr

