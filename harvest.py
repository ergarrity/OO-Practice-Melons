############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name

        self.pairings = []


    def add_pairing(self, *args):
        """Add a food pairing to the instance's pairings list."""

        for arg in args:
        	self.pairings.append(arg)


    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    musk = MelonType('musk', 1998, 'green', True, True, 'Muskmelon')
    musk.add_pairing('mint')
    all_melon_types.append(musk)

    cas = MelonType('cas', 2003, 'orange', False, False, 'Casaba')
    cas.add_pairing('strawberries', 'mint')
    all_melon_types.append(cas)

    cren = MelonType('cren', 1996, 'green', False, False, 'Crenshaw')
    cren.add_pairing('proscuitto')
    all_melon_types.append(cren)

    yw = MelonType('yw', 2013, 'yellow', False, True, 'Yellow Watermelon')
    yw.add_pairing('ice cream')
    all_melon_types.append(yw)

    return all_melon_types


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon in melon_types:
    	print("{} pairs with".format(melon.name))
    	for pairing in melon.pairings:
    		print("- {}".format(pairing))


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    melon_code_lookup = {}

    for melon in melon_types:
    	melon_code_lookup[melon.code] = melon

    return melon_code_lookup


############
# Part 2   #
############
melon_types = make_melon_types()
melons_by_id = make_melon_type_lookup(melon_types)

class Melon(object):
    """A melon in a melon harvest."""

    def __init__(self, type_of_melon, shape, color, field, harvester):
    	self.type_of_melon = type_of_melon
    	self.shape = shape
    	self.color = color
    	self.field = field
    	self.harvester = harvester

    def is_sellable(self):
    	return self.color > 5 and self.shape > 5 and self.field != 3



def make_melons(melon_types):
    """Returns a list of Melon objects."""

    melon_1 = Melon(melons_by_id['yw'], 8, 7, 2, 'Shiela')
    melon_2 = Melon(melons_by_id['yw'], 3, 4, 2, 'Shiela')
    melon_3 = Melon(melons_by_id['yw'], 9, 8, 3, 'Shiela')
    melon_4 = Melon(melons_by_id['cas'], 10, 6, 35, 'Shiela')
    melon_5 = Melon(melons_by_id['cren'], 8, 9, 35, 'Michael')
    melon_6 = Melon(melons_by_id['cren'], 8, 2, 35, 'Michael')
    melon_7 = Melon(melons_by_id['cren'], 2, 3, 4, 'Michael')
    melon_8 = Melon(melons_by_id['musk'], 6, 7, 4, 'Michael')
    melon_9 = Melon(melons_by_id['yw'], 10, 7, 3, 'Sheila')

    melon_objects = [melon_1, melon_2, melon_3, melon_4, melon_5, melon_6, melon_7, melon_8, melon_9]

    return melon_objects

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    for objct in melons:
    	sellable_phrase = ''

    	if objct.is_sellable():
    		sellable_phrase = 'CAN BE SOLD'

    	else:
    		sellable_phrase = 'NOT SELLABLE'

    	print ("Harvested by {} from Field {} {}".format(objct.harvester, objct.field, sellable_phrase))


def make_melons_from_log(file):
	""" Make melon object from text file of melon info """

	with open(file) as harvest_log:
		list_of_melons = []
		for line in harvest_log:
			line = line.strip()
			line = line.split(' ')
			shape = int(line[1])
			color = int(line[3])
			type_of_melon = melons_by_id[line[5]]
			harvester = line[8]
			field = int(line[11])
			
			list_of_melons.append(Melon(type_of_melon, shape, color, field, harvester))

	print(list_of_melons)



