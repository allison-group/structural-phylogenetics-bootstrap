cd Trajectories/Trials/
pwd
set list_ [glob *.vals]
foreach i $list_ {
	set vals ""
	set id_ [lindex [split $i .] 0]
	set fp [open $i r]
	fconfigure $fp -buffering line
	gets $fp data
	while {$data != ""} {
	     lappend vals $data
	     gets $fp data
	}
	close $fp
	mol load gro ../$id_.gro
	mol addfile ../$id_.xtc waitfor all
	set mid_ [molinfo top get id]
	set c -1
	foreach j $vals {
		incr c
		set sel [atomselect top all frame $j]
		$sel writepdb trial_$c/$id_.pdb
		$sel delete 
	}
	mol delete $mid_
}

