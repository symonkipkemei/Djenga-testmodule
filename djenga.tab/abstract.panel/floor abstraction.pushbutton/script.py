# -*- coding: utf-8 -*-


# METADATA
################################################################################################################################


__title__ = "Floor abstraction"

__doc__ = """ Version  1.1
Date  = 19.05.2023
___________________________________________________________________________
Description:

This tool will abstract the parmeters from the element (Floor) selected by the user into :


Element Parameters:
 - area
 - perimeter
 - thickness

Material Parameters:
- BRC Mesh
- DPM 
- River sand
- Coarse Gravel
- Cement

___________________________________________________________________________
How-to:

-> Click on the button
___________________________________________________________________________
last update:
- [24.05.2023] - 1.0 RELEASE

___________________________________________________________________________
To-Do:
-> Develop the abstract tool
___________________________________________________________________________
Author: Symon Kipkemei

"""

__author__ = "Symon Kipkemei"
__helpurl__ = "https://www.linkedin.com/in/symon-kipkemei/"

__highlight__ = 'new'

__min_revit_ver__ = 2020
__max_revit_ver__ = 2022

# IMPORTS
################################################################################################################################


# regular

# Autodesk
from Autodesk.Revit.DB import *
from Autodesk.Revit.DB import Transaction, Element, ElementId, FilteredElementCollector

# pyrevit


# custom ( Remember to include the csutom lib package to the pythonpath)


# .NET imports ( I have no idea why I am importing this)
import clr

clr.AddReference("System")
from System.Collections.Generic import \
    List  # List<ElementType>() <-it's special type of list that RevitAPI often requires

# VARIABLES
################################################################################################################################


# instance variables from revitAPI


# __revit__  used to create an instance 
app = __revit__.Application  # represents the Revit Autodesk Application
doc = __revit__.ActiveUIDocument.Document  # obj used to create new instances of elements within the active project
uidoc = __revit__.ActiveUIDocument  # obj that represent the current active project


# custom variables


# FUNCTION AND CLASSES
################################################################################################################################


# t = Transaction(doc, __title__)
# t.Start()
# Transaction guards any changes made to the revit Model
# t.commit

def get_element_data():
    """Select all the floors in the project and abstract elemental data
    :return: A dictionary with element data area, thickness, volume and perimeter
    """
    floors = FilteredElementCollector(doc).OfCategory(
        BuiltInCategory.OST_Floors).WhereElementIsNotElementType().ToElements()

    element_data = {}

    for floor in floors:
        # Built in parameters

        floor_id = floor.Id
        floor_level_id = floor.LevelId
        area = floor.get_Parameter(BuiltInParameter.HOST_AREA_COMPUTED).AsValueString()
        thickness = floor.get_Parameter(BuiltInParameter.FLOOR_ATTR_THICKNESS_PARAM).AsValueString()
        volume = floor.get_Parameter(BuiltInParameter.HOST_VOLUME_COMPUTED).AsValueString()
        perimeter = floor.get_Parameter(BuiltInParameter.HOST_PERIMETER_COMPUTED).AsValueString()

        element_data[floor_id] = {"area": area, "thickness": thickness, "volume": volume, "perimeter": perimeter}

        print("***Floor id {}  at Floor Level {}***".format(floor_id, floor_level_id))
        print("-" * 100)

        print("Area :{}".format(area))
        print("thickness :{}".format(thickness))
        print("volume :{}".format(volume))
        print("perimeter :{}".format(perimeter))

        print("-" * 100)

    return element_data


get_element_data()