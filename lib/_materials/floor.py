

def get_brc_mesh(floor_area):
    pass


def get_coarse_soft_cement_vol(concrete_mixing_ratio,volume):
    #type: (tuple,float) -> tuple
    """
    :param concrete_mixing_ratio: ratio of cement, soft_agg, coarse_agg
    :param volume: volume of the concrete in m3
    :return: respective volume of cement,soft_agg, coarse_agg
    """
    cement_ratio = concrete_mixing_ratio[0]
    soft_agg_ratio = concrete_mixing_ratio[1]
    coarse_agg_ratio = concrete_mixing_ratio[2]
    concrete_ratio = cement_ratio + soft_agg_ratio + coarse_agg_ratio

    volume = volume * 1000000000

    cement_volume = round((cement_ratio/concrete_ratio) * volume, 2)
    soft_agg_volume = round((soft_agg_ratio/concrete_ratio) * volume, 2)
    coarse_agg_volume = round((coarse_agg_ratio/concrete_ratio) * volume, 2)

    return cement_volume, soft_agg_volume, coarse_agg_volume


def get_cement_units(cement_volume):
    """ Abstract number of cement bags from a given volume of cement
    :param cement_volume: Volume of cement in m3
    :return: Number of  50kg bags
    """
    # approx density of cement kg/m3
    cement_density = 1440

    # 1m3 = 1440kg
    # how about a 50kg bg

    volume_of_50kg_bag = 50/1440
    no_of_bags = cement_volume/volume_of_50kg_bag

    return no_of_bags


def get_coarse_units():
    pass



def get_soft_units():
    pass


def get_brc_mesh(floor_area_mm):
    """
    Get the number of BRC mesh roll needed
    :param floor_area: The floor area
    :return: the number of rolls
    """
    width = convert_to_mm(2.1)
    length  = convert_to_mm(48)
    area_brc_mesh = width * length
    area_brc_mesh_overlap = 300 * length

    area_brc_mesh_covered = area_brc_mesh - area_brc_mesh_overlap
    no_brc_mesh_roll = convert_to_mm2(floor_area_mm)/area_brc_mesh_covered

    return  no_brc_mesh_roll
    #factor in the overlap distance between BRC MESH
    #standard length is 2.1m wide and 48m long

def get_dpm():
    pass

def convert_to_mm(units):
    """
    converts units to mm
    :param units: units in m
    :return: units in mm
    """
    return  units * 1000
def convert_to_mm2(units):
    """
    convert m2 to mm2
    :param units:
    :return:
    """
    return  units * 1000 * 1000

def main():
    conc_mix_ratio = (1, 2, 4)
    volume_of_mix = 1.78
    cement, soft_agg, coarse_agg = get_coarse_soft_cement_vol(conc_mix_ratio, volume_of_mix)

    print(cement)

    bags = get_cement_units(cement)
    print (bags)


if __name__ == "__main__":
    print (get_brc_mesh(9))

