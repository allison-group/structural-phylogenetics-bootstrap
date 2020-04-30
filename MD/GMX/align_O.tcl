set pdb [lindex $argv 0]
mol load pdb $pdb
set sel [atomselect top all]
$sel moveby [vectinvert [measure center $sel]]
$sel writepdb origin.pdb
$sel delete
