set gro [lindex $argv 0]
set xtc [lindex $argv 1]
set id [lindex $argv 2]

mol load gro $gro
mol addfile $xtc waitfor all

set nf [molinfo top get numframes]

set Ref [atomselect top "name CA" frame 0]

set f [open $id.dat a]
for {set i 0} {$i < $nf} {incr i} {
	set sel [atomselect top "name CA" frame $i]
	set mx [measure fit $sel $Ref]
	$sel move $mx
	set RMSD [measure rmsd $sel $Ref]
	puts $f $id\t$i\t$RMSD
	$sel delete
}
close $f

