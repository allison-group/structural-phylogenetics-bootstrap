# Move structure to origin
vmd -dispdev text -eofexit -args < align_O.tcl input_0.pdb
# Set up structure to have slvent boundary and generate a GRO
gmx editconf -f origin.pdb -o origin.gro -bt cubic -d 1.5
# Using charmmff add water model -- and generte the first topology file defining protein structure
gmx pdb2gmx -f origin.gro -o input_1.gro -p protein.top -ignh -ff charmm36-nov2016 -water tip3p
# Setup a minimization run
gmx grompp -v -f min_sd.mdp -c input_1.gro -p protein.top -o protein-EM-vacuum.tpr -maxwarn 1
# Actually run the minimization
gmx mdrun -v -deffnm protein-EM-vacuum -c protein-EM-vacuum.gro 
# Solvate system
gmx solvate -cp protein-EM-vacuum.gro -cs spc216.gro -p protein.top -o protein-water.gro
# Sometimes there may be waters in the protein core --- get rid of those
vmd -dispdev text -eofexit -args < del_wat_inside.tcl protein-water.gro
# clean up gro file
./fix_gro.py
# Since we added waters - set up minimization -- 
gmx grompp -v -f min_sd.mdp -c protein-water-hollow-mod.gro -p protein.top -o protein-water-hollow-mod.tpr -maxwarn 1
# Add ions
gmx genion -s protein-water-hollow-mod.tpr -o protein-solvated-ion.gro -neutral -pname NA -nname CL -p protein.top << EOF
SOL
EOF
# Since we added ions we need to redo grompp for some reason I need to do this twice -- (think fix!!)
gmx grompp -v -f min_sd.mdp -c protein-solvated-ion.gro -p protein.top -o protein-EM-solvated-ion.tpr
# Now minimize the neutralised-solvated-protein
gmx mdrun -v -deffnm protein-EM-solvated-ion -c protein-EM-solvated-ion.gro

