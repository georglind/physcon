## PhysCon

A library of physical constants and units. 

Requirements are fuzzywuzzy, which can be installed by 

    pip install fuzzywuzzy

The library is used simply like:

    import physcon

    physcon.e      # --> returns 1.6022e-19
    physcon.Rsun   # --> returns 6.9600e8

In addition physcon supplied two methods which mathc constant values and units to a `search_string` through `values(search_string)` and `units(search_string)`. 

    import physcon

    physcon.values('Planck's constant')
	# --> returns 6.6261e-34

    physcon.units(('Planck's constant')
	# --> returns 'J s'
