# structural-phylogenetics-bootstrap
Scripts for preparing, running and processing MD and MC trajectories and for running the structure-based 'bootstrap' to gauge the robustness of structural phylogenetic relationships.

Note: The boostrap scripts currently supplied are specifically designed for MD trajectories, but it should be straightforward to adapt it for MC trajectories. The scripts for applying the bootstrap procedure to MC output are currently unavailable due to COVID-19 restrictions on movement but will be added as soon as possible. In the meantime, please raise issues on github if you require help.

--MD--
GMX :: Shell scripts for preparing (s1.sh) and equilibrating and running (s2.sh) MD simulations of a protein using VMD (via TCL scripts) and GROMACS, and the required GROMACS mdp and CHARMM36 force field files.
RMSD :: Python and tcl scripts for calculating the RMSD values from the MD simulation trajectory.


--MC--
The command for running PHAISTOS to use MC to generate alternative conformations for a protein.


--Bootstrap--
Scripts for running the structure-based 'bootstrap'. A very detailed README is provided that is quite explicit about everything that needs to be done and also provides a way to automate the entire procedure. Note that a particular directory structure needs to be followed. The bootstrap process should run well on a PC with some cores to spare or a single node of an HPC machine. It is not designed for cross-node calculations.
