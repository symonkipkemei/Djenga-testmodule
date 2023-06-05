

from __future__ import division

# Converting units from m to mm for high level accuracy results
# all units intercepted from the model are
# length == mm
#   area == m2
# volume == m3

def convert_length(units):
    """
    converts length from m to mm
    :param units: units in m
    :return: units in mm
    """
    return units * 1000

def convert_area(units):
    """
    convert area from m2 to mm2
    :param units:
    :return:
    """
    return units * 1000 * 1000


def convert_volume(units):
    # type: (float) -> float
    """
    Convert volume from m3 to mm3
    :param units:
    :return:
    """
    return units * 1000 * 1000 * 1000


# get quantities of trucks/lorries/tippers/wheel-barrows

def volume_tipper():
    """
    Calculates the volume of a tipper, define the size of a tipper in the manual
    :return: the volume of a tipper in m3
    """
    length = 5.1
    width = 2.3
    height = 1.2

    area = length * width
    volume = area * height

    return volume





# all abstraction calculations are done in mm


def get_coarse_soft_cement_vol(concrete_mixing_ratio,volume):
    # type: (tuple,float) -> tuple
    """
    break down the total volume of a ground slab into the subsequent cement, soft- agg and coarse -agg ratio
    :param concrete_mixing_ratio: ratio of cement, soft_agg, coarse_agg
    :param volume: volume of the concrete in m3
    :return: respective volume of cement,soft_agg, coarse_agg
    """
    cement_ratio = concrete_mixing_ratio[0]
    soft_agg_ratio = concrete_mixing_ratio[1]
    coarse_agg_ratio = concrete_mixing_ratio[2]
    concrete_ratio = cement_ratio + soft_agg_ratio + coarse_agg_ratio

    cement_volume = round((cement_ratio/concrete_ratio) * volume, 3)
    soft_agg_volume = round((soft_agg_ratio/concrete_ratio) * volume, 3)
    coarse_agg_volume = round((coarse_agg_ratio/concrete_ratio) * volume, 3)
    return cement_volume, soft_agg_volume, coarse_agg_volume


def get_cement_bags_units(cement_volume):
    """ Abstract number of cement bags from a given volume of cement
    :param cement_volume: Volume of cement in m3
    :return: Number of  50kg bags
    """
    # approx density of cement kg/m3
    cement_density = 1440

    # the mass of a cement bag
    cement_bag_kg = 50

    # the volume of a cement bag
    volume_of_50kg_bag = cement_bag_kg/cement_density

    # no of bags based on volume
    no_of_bags = cement_volume/volume_of_50kg_bag

    return int(no_of_bags)


def get_aggregate_tippers(agg_volume, tipper_volume):
    """
    Abstract the number of tippers needed to construct a ground slab
    :param agg_volume: The total volume of aggregate needed
    :param tipper_volume: The total volume of a single tipper
    :return: The number of tippers needed
    """

    no_tippers = agg_volume / tipper_volume

    return no_tippers


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




def main():
    conc_mix_ratio = (1, 2, 4)
    volume_of_mix = 1.78
    cement, soft_agg, coarse_agg = get_coarse_soft_cement_vol(conc_mix_ratio, volume_of_mix)

    print(cement)

    bags = get_cement_units(cement)
    print (bags)


if __name__ == "__main__":
    print (get_brc_mesh(9))

