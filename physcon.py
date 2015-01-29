from fuzzywuzzy import process

cs = dict()
us = dict()

def values(const):

	choices = cs.keys()
	choice = process.extractOne(const.to_lower.replace(' ','_'), choices)

	if choice[1] < 100:
		print('Values: Matched {0} to {1}'.format(const, choice[0]))

	return cs[choice]


def units(const):
	choices = us.keys()
	choice = process.extractOne(const, choices)

	if choice[1] < 100:
		print('Units: Matched {0} to {1}'.format(const, choice[0]))

	return us[choice]


# Quantum physics

cs['planck_constant'] = 6.6261e-34
us['planck_constant'] = 'J s-1'
h = cs['planck_constant']

cs['planck_constant_divided_2_pi'] = 1.0546e-34
us['planck_constant_divided_2_pi'] = 'J s-1'
cs['hbar'] = cs['planck_constant_divided_2_pi']
us['hbar'] = us['planck_constant_divided_2_pi'] 
hbar = cs['planck_constant_divided_2_pi']

cs['bohr_magneton'] = 9.27400968e-24
us['bohr_magneton'] = 'J T-1'
muB = cs['bohr_magneton']

cs['bohr_radius'] = 5.2917721092e-11
us['bohr_radius'] = 'm'
RB = cs['bohr_radius']
a = cs['bohr_radius']

cs['flux_quantum'] = 2.067833758e-15
us['flux_quantum'] = 'Wb'
phi0 = cs['flux_quantum']

cs['rydberg_energy'] = 2.1799e-18
us['rydberg_energy'] = 'J'
Ry = cs['rydberg_energy']

cs['rydberg_wavenumber_constant'] = 1.0974e7
us['rydberg_wavenumber_constant'] = 'J'
RH = cs['rydberg_wavenumber_constant']

cs['quantized_hall_resistance'] = 2.5813e4
us['quantized_hall_resistance'] = 'Ohm'
R0 = cs['quantized_hall_resistance']


# QED

cs['fine_structure_constant'] = 7.2974e-3
us['fine_structure_constant'] = ''
alpha = cs['fine_structure_constant']

# Masses

cs['mass_of_electron'] = 9.10938291e-31
us['mass_of_electron'] = 'kg'
me = cs['mass_of_electron']

cs['mass_of_proton'] = 1.672621777e-27
us['mass_of_proton'] = 'kg'
mp = cs['mass_of_proton']

cs['atomic_mass_unit'] = 1.660538921e-27
us['atomic_mass_unit'] = 'kg'
amu = cs['atomic_mass_unit']

cs['newton_gravitational_constant'] = 6.6743e-11	
us['newton_gravitational_constant'] = 'm3 kg-1 s-2'
G = cs['newton_gravitational_constant']

cs['acceleration_of_gravity'] = 9.8066
us['acceleration_of_gravity'] = 'm s-2'
g = cs['acceleration_of_gravity']

# Electromagnetism

cs['elementary_charge'] = 1.6022e-19
us['elementary_charge'] = 'C'
e = cs['elementary_charge']

cs['elementary_charge_in_cgs_units'] = 4.80320425e-10
us['elementary_charge_in_cgs_units'] = 'statC'
esu = cs['elementary_charge_in_cgs_units']

cs['speed_of_light'] = 299792458
us['speed_of_light'] = 'm s-1'
c = cs['speed_of_light']

cs['permittivity_of_free_space'] = 8.8542e-12
us['permittivity_of_free_space'] = 'F m-1'
epsilon0 = cs['permittivity_of_free_space']

cs['permeability_of_free_space'] = 1.2566e-6
us['permeability_of_free_space'] = 'N A-2'
mu0 = cs['permeability_of_free_space']

# Statistical Physics

cs['avogadros_constant'] = 6.0221e23
us['avogadros_constant'] = ''
NA = cs['avogadros_constant']

cs['Boltzmanns_constant'] =  1.3807e-23 
us['avogadros_constant'] = 'J K-1'
kB = cs['Boltzmanns_constant']

cs['gas_constant'] = 8.3145
us['gas_constant'] = 'J K-1'
R =  cs['gas_constant']

cs['atmospheric_standard_pressure'] = 1.0132e5
us['atmospheric_standard_pressure'] = 'N m-2'
atm = cs['atmospheric_standard_pressure']

cs['stefan-boltzmann_constant'] = 5.6704e-8
us['stefan-boltzmann_constant'] = 'W m-2 K-4'
sigma = cs['stefan-boltzmann_constant']

# Astrophysics

cs['astronomical_unit'] = 1.4960e11
us['astronomical_unit'] = 'm'
AU = cs['astronomical_unit']

cs['parsec'] = 3.0857e16
us['parsec'] = 'm'
parsec = cs['parsec']

cs['wiens_displacement_law_constant'] = 2.8978e-3 
us['wiens_displacement_law_constant'] = 'm K'
b = cs['wiens_displacement_law_constant']

# unit conversions

cs['electron_volt'] = cs['elementary_charge']
us['electron_volt'] = 'J'
eV = e 						

cs['angstrom'] = 1e-10
us['angstrom'] = 'm'
angstrom = cs['angstrom']

cs['calorie'] = 4.184
us['calorie'] = 'J'
calorie = cs['calorie']

# Solar system

cs['mass_of_the_sun'] = 1.9884e30
us['mass_of_the_sun'] = 'kg'
Msun = cs['mass_of_sun']

cs['radius_of_the_sun'] = 6.9600e8	
us['radius_of_the_sun'] = 'm'
Rsun = cs['radius_of_the_sun']

cs['solar_luminosity'] = 3.8427e26
us['solar_luminosity'] = 'W'
Lsun = cs['solar_luminosity']

cs['mass_of_the_earth'] = 5.9722e24
us['mass_of_the_earth'] = 'kg'
Mearth = cs['mass_of_earth']

cs['radius_of_the_earth'] = 6.3781e6
us['radius_of_the_earth'] = 'm'
Rearth = cs['radius_of_the_earth']

cs['year'] = 3.1557e7
us'year'] = 's'
year = cs['year']





