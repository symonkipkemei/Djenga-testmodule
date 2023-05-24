Project Name: Djenga

Project  Description: Abstracting Material data from BIM Models in real-time.

Project Link: https://github.com/symonkipkemei/Djenga.git



**Business and Market Needs**
______________________________________________________________________________________________________________________________________

- Architects /Builders /Designers and  Quantity Surveyors want real-time access to material data of their buildings for better control of the design and cost outcome.

Sustainable Development Goals
-  Sustainable Cities and Communities (SDG 11)
- Responsible Consumption and Production (SDG 12)

Long term goal
- Fully democratize access to real-time material data for buildings.
- Improve optimization of building materials for every built project by 50%


 Success Criteria
- If we can achieve 30% of building material optimization, and have 400 monthly users

Leverage
- Construction and building technology is decentralized, taps into and dominates the building material sector for East Africa



**Mapping Out User Journey**
______________________________________________________________________________________________________________________________________
Identify the user 

- The user: Architects, Designers, Quantity Surveyors, Contractors, Builders, master-builder
- The Modeler: Generates Revit models 

Identify the actions

- Architect - Designs and generate a model, Get material data, compare one type of slab to another, Optimize design to use more/less material
- Contractor- Determine how many material elements are needed to fabricate/construct a wall/slab etc
- Quantity Surveyor- Get a spreadsheet of all quantities of material in Excel format. To edit and fill up the appropriate rates
- Client /builder- Get a spreadsheet of all quantities of material  for bidding and pricing  by different suppliers/hardware



A pain and Gain Map
 
- Action: Get material Data
- Pains : Traditionally material data is provided after the design is complete and not during design stage , quantity surveyor does take off to determine quantities data from drawings , quantity surveryor calculates materials needed for each element.
- Gains. Get realtime material data from BIM models , Get accurate material estimates, Optimize material usage early in the design stage, 


**Features to build**
______________________________________________________________________________________________________________________________________

User Needs:
- Realtime Quantities of materials needed to construct an element; start with floor slab.....,start with a bungalow house

User wants:
1. Materials needed to construct different elements
2. Generate excel spreadsheet of all quantities of materials with an empty rates column.
3. Compare change of material quantities through the lifetime of the design (Every time get material data is requested, a previous version of the same is saved)
4. Generative design on how to optimize/install/place each material 



**Building Tools**
______________________________________________________________________________________________________________________________________

1. Python 2.7/ IronPython /RevitPythonShell
2. Pyrevit
3. RevitAPI
4. Autodesk Revit 2022 /Revit Lookup
5. Panda


**Building Process - Iteration 01**
______________________________________________________________________________________________________________________________________


1. Abstract the area, thickness, perimeter, and volume of the ground slab from the Revit Model using revitAPI
2. DPM (Damp Proof Membrane): Function to abstract the dpm length required, dpm length remaining       
2. BRC Mesh: Function to abstract BRC Mesh required  ( The length of the BRC Mesh) to cover the entire slab and ( How many rolls of BRC Mesh), What length of BRC  Mesh remains.
3. Concrete: Function to abstract the volume of sand, ballast, and cement needed, and further abstract the relative unit-Bags of cement.
4. Share data: project data: project_name, project_unit_area; element_data: element-category, element_type, and  material_data:  ( Note that the type of element influences the materials to be used)
5. An add-in/plug-in with the following features:
    1. Element  choice- i.e User selects an element for analysis i.e Floor
    2. Element Type - User specifies element type i.e concrete ground floor slab
    3. Element Abstract -Generates a list for all materials required, with their quantities and their units of measure i.e cement, the volume of cement, bags of cement
   4. Element Export - Export as pdf or Excel format for pricing , quotation and sharing; write the list into Excel with Panda