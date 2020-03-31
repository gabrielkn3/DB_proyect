from flask import Flask, jsonify, request

from handler.BabyFoodHandler import BabyFoodHandler
from handler.Battery_Handler import BatteriesHandler
from handler.ClothingHandler import ClothingHandler
from handler.DryFoodHandler import DryFoodHandler
from handler.FuelHandler import FuelHandler
from handler.GeneratorHandler import GeneratorHandler
from handler.HeavyEquipmentHandler import HeavyEquipmentHandler
from handler.IceHandler import IceHandler
from handler.MedicalDevicesHandler import MedicalDeviceHandler
from handler.MedicationHandler import MedicationHandler
from handler.ToolHandler import ToolHandler
from handler.Water_handler import WaterHandler
from handler.listing_handler import ListingHandler
from handler.request_handler import RequestHandler
from handler.resource_handler import ResourceHandler
from handler.supplier import SupplierHandler
from handler.CannedFoodHandler import CannedFoodHandler
from handler.user import userHandler
from handler.administrator import adminHandler
from handler.requester_handler import RequesterHandler

# Import Cross-Origin Resource Sharing to enable
# services on other ports on this machine or on other
# machines to access this app
from flask_cors import CORS, cross_origin

# Activate
app = Flask(__name__)
# Apply CORS to this app
CORS(app)

#*********************************************************************PRIMARY APP FUNCTIONS*********************************************************************************************************************

#HomePage
@app.route('/')
def greeting():
    return 'Hello, this is the Resource Manager DB App!'


#GetAllResources
@app.route('/ResourceApp/resources', methods=['GET'])
def getAllResources():
        if not request.args:
            return ResourceHandler().getAllResources()
        else:
            return ResourceHandler().searchResources(request.args)

#Get,Update, or Delete Resource By ID
@app.route('/ResourceApp/resources/<int:rid>', methods=['GET'])
def getResourceById(rid):
    if request.method == 'GET':
        return ResourceHandler().getResourcesById(rid)
    # elif request.method == 'PUT':                     #Resource Updates and Deletes are managed by individual resource type handlers to guarantee consistency with resource master table
    #     return ResourceHandler().updateResource(rid, request.form)
    # elif request.method == 'DELETE':
    #     return ResourceHandler().deleteResource(rid)
    else:
        return jsonify(Error="Method not allowed."), 405

#GetSuppliersByResourceID
@app.route('/ResourceApp/resources/<int:rid>/suppliers')
def getSuppliersByResourceId(rid):
    return ResourceHandler().getSuppliersByResourceId(rid)

#GetRequestersByResourceID
@app.route('/ResourceApp/resources/<int:rid>/requesters')
def getRequestersByResourceId(rid):
    return ResourceHandler().getRequestersByResourceId(rid)

#Browse All Requests or insert new request
@app.route('/ResourceApp/requests', methods=['GET', 'POST'])
def getAllRequests():
    if request.method == 'POST':

        print("REQUEST: ", request.json)
        return RequestHandler().insertRequestJson(request.json)
    else:
        if not request.args:
            return RequestHandler().getAllRequests()

#Browse All Listings or Insert new Listing
@app.route('/ResourceApp/listings', methods=['GET', 'POST'])
def getAllListings():
    if request.method == 'POST':

        print("REQUEST: ", request.json)
        return ListingHandler().insertListingJson(request.json)
    else:
        if not request.args:
            return ListingHandler().getAllListings()

#Keyword Search Requests by Resource Name
@app.route('/ResourceApp/requests/<string:rname>', methods=['GET', 'POST'])
def getRequestsByName(rname):
    if request.method == 'GET':
        return RequestHandler().getRequestsByResourceName(rname)
    else:
        return jsonify(Error="Method not allowed."), 405

#Keyword Search Listings by Resource Name
@app.route('/ResourceApp/listings/<string:rname>', methods=['GET'])
def getListingsByName(rname):
    if request.method == 'GET':
        return ListingHandler().getListingsByResourceName(rname)
    else:
        return jsonify(Error="Method not allowed."), 405
    
# Filters for dashboard, NEXT PHASE
# @app.route('/ResourceApp/Dashboard/Daily', methods=['GET'])
#
# @app.route('/ResourceApp/Dashboard/Trending>', methods=['GET'])
#
# @app.route('/ResourceApp/Dashboard/Regions', methods=['GET'])




#************************************************************SUPPLIER*********************************************************************

@app.route ('/ResourceApp/suppliers', methods=['GET', 'POST'])

#Get All Suppliers or REGISTER AS A SUPPLIER
def getAllSuppliers():
    if request.method == 'POST':
        print("REQUEST: ", request.form)
        return SupplierHandler().insertSupplier(request.form)
    else:
        if not request.args:
            return SupplierHandler().getAllSuppliers()
        else:
            return jsonify(Error="Method not allowed, try other route"), 405

@app.route('/ResourceApp/suppliers/location', methods=['GET'])
def getSupplierByLocation():
    if request.method == 'GET':
        return SupplierHandler().searchSuppliers(request.form)
    else:
        return jsonify(Error="Method not allowed, try other route"), 405





@app.route('/ResourceApp/suppliers/<int:sid>/',
           methods=['GET', 'PUT', 'DELETE'])
def getSupplierById(sid):
    if request.method == 'GET':
        return SupplierHandler().getSupplierById(sid)
    elif request.method == 'PUT':
        return SupplierHandler().updateSupplier(sid, request.form)
    elif request.method == 'DELETE':
        return SupplierHandler().deleteSupplier(sid)
    else:
        return jsonify(Error = "Method not allowed"), 405



@app.route('/ResourceApp/suppliers/<int:sid>/resources')
def getResourcesBySupplierId(sid):
    return SupplierHandler().getResourcesBySupplierId(sid)



#*********************************************************REQUESTER****************************************************************************************************************


#Get All Requesters or REGISTER AS A REQUESTER
@app.route ('/ResourceApp/requesters', methods=['GET', 'POST'])
def getAllRequesters():
    if request.method == 'POST':
        print("REQUEST: ", request.form)
        return SupplierHandler().insertSupplier(request.form)
    else:
        if not request.args:
            return RequesterHandler().getAllRequesters()
        else:
            return jsonify(Error="Method not allowed, try other route"), 405



@app.route('/ResourceApp/requesters/<int:reqid>/',
           methods=['GET', 'PUT', 'DELETE'])
def getRequesterById(reqid):
    if request.method == 'GET':
        return RequesterHandler().getRequesterById(reqid)
    elif request.method == 'PUT':
        return RequesterHandler().updateRequester(reqid, request.form)
    elif request.method == 'DELETE':
        return RequesterHandler().deleteRequester(reqid)
    else:
        return jsonify(Error = "Method not allowed"), 405



@app.route('/ResourceApp/requesters/location', methods=['GET'])
def getRequestersByLocation():
    if request.method == 'GET':
        return RequesterHandler().searchRequesters(request.form)
    else:
        return jsonify(Error="Method not allowed, try other route"), 405




#Requested items
@app.route('/ResourceApp/requesters/<int:reqid>/resources')
def getResourcesByRequesterId(reqid):
    return RequesterHandler().getResourcesByRequesterId(reqid)







#************************************************************MEDICAL DEVICES******************************************************************************
@app.route('/ResourceApp/resources/medicaldevices', methods=['GET', 'POST'])
def getAllMedicalDevices():
    if request.method == 'POST':
        
        print("REQUEST: ", request.json)
        return MedicalDeviceHandler().insertMedicalDeviceJson(request.json)
    else:
        if not request.args:
            return MedicalDeviceHandler().getAllMedicalDevices()


@app.route('/ResourceApp/resources/medicaldevices/<int:mdid>', methods=['GET', 'PUT', 'DELETE'])
def getMedicalDevicesById(mdid):
    if request.method == 'GET':
        return MedicalDeviceHandler().getMedicalDevicesById(mdid)
    elif request.method == 'PUT':
        return MedicalDeviceHandler().updateMedicalDevice(mdid, request.form)
    elif request.method == 'DELETE':
        return MedicalDeviceHandler().deleteMedicalDevice(mdid)
    else:
        return jsonify(Error="Method not allowed."), 405


@app.route('/ResourceApp/resources/medicaldevices/Name/<string:mdname>', methods=['GET'])
def getMedicalDevicesByName(mdname):
    if request.method == 'GET':
        return MedicalDeviceHandler().getMedicalDevicesByName(mdname)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/ResourceApp/resources/medicaldevices/Brand/<string:mdbrand>', methods=['GET'])
def getMedicalDevicesByBrand(mdbrand):
    if request.method == 'GET':
        return MedicalDeviceHandler().getMedicalDevicesByBrand(mdbrand)
    else:
        return jsonify(Error="Method not allowed."), 405

##***********************************************MEDICATION**********************************************************************

@app.route('/ResourceApp/resources/medication', methods=['GET', 'POST'])
def getAllMedication():
    if request.method == 'POST':
        
        print("REQUEST: ", request.json)
        return MedicationHandler().insertMedicationJson(request.json)
    else:
        if not request.args:
            return MedicationHandler().getAllMedication()

@app.route('/ResourceApp/resources/medication/<int:mid>', methods=['GET', 'PUT', 'DELETE'])
def getMedicationById(mid):
    if request.method == 'GET':
        return MedicationHandler().getMedicationById(mid)
    elif request.method == 'PUT':
        return MedicationHandler().updateMedication(mid, request.form)
    elif request.method == 'DELETE':
        return MedicationHandler().deleteMedication(mid)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/ResourceApp/resources/medication/Name/<string:mname>', methods=['GET'])
def getMedicationByName(mname):
    if request.method == 'GET':
        return MedicationHandler().getMedicationByName(mname)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/ResourceApp/resources/medication/Dosage/<string:mdosage>', methods=['GET'])
def getMedicationByDosage(mdosage):
    if request.method == 'GET':
        return MedicationHandler().getMedicationByDosage(mdosage)
    else:
        return jsonify(Error="Method not allowed."), 405

##***********************************************BABY_FOOD**********************************************************************

@app.route('/ResourceApp/resources/babyfood', methods=['GET', 'POST'])
def getAllBabyFood():
    if request.method == 'POST':
        
        print("REQUEST: ", request.json)
        return BabyFoodHandler().insertBabyFoodJson(request.json)
    else:
        if not request.args:
            return BabyFoodHandler().getAllBabyFood()

@app.route('/ResourceApp/resources/babyfood/<int:bfid>', methods=['GET', 'PUT', 'DELETE'])
def getBabyFoodById(bfid):
    if request.method == 'GET':
        return BabyFoodHandler().getBabyFoodById(bfid)
    elif request.method == 'PUT':
        return BabyFoodHandler().updateBabyFood(bfid, request.form)
    elif request.method == 'DELETE':
        return BabyFoodHandler().deleteBabyFood(bfid)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/ResourceApp/resources/babyfood/brand/<string:bfbrand>', methods=['GET'])
def getBabyFoodByBrand(bfbrand):
    if request.method == 'GET':
        return BabyFoodHandler().getBabyFoodByBrand(bfbrand)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/ResourceApp/resources/babyfood/flavor/<string:bfflavor>', methods=['GET'])
def getBabyFoodByFlavor(bfflavor):
    if request.method == 'GET':
        return BabyFoodHandler().getBabyFoodByFlavor(bfflavor)
    else:
        return jsonify(Error="Method not allowed."), 405

##***********************************************CANNED_FOOD**********************************************************************

@app.route('/ResourceApp/resources/cannedfood', methods=['GET', 'POST'])
def getAllCannedFood():
    if request.method == 'POST':
        
        print("REQUEST: ", request.json)
        return CannedFoodHandler().insertCannedFoodJson(request.json)
    else:
        if not request.args:
            return CannedFoodHandler().getAllCannedFood()

@app.route('/ResourceApp/resources/cannedfood/<int:cfid>', methods=['GET', 'PUT', 'DELETE'])
def getCannedFoodById(cfid):
    if request.method == 'GET':
        return CannedFoodHandler().getCannedFoodById(cfid)
    elif request.method == 'PUT':
        return CannedFoodHandler().updateCannedFood(cfid, request.form)
    elif request.method == 'DELETE':
        return CannedFoodHandler().deleteCannedFood(cfid)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/ResourceApp/resources/cannedfood/brand/<string:cfbrand>', methods=['GET'])
def getCannedFoodByBrand(cfbrand):
    if request.method == 'GET':
        return CannedFoodHandler().getCannedFoodByBrand(cfbrand)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/ResourceApp/resources/cannedfood/name/<string:cfname>', methods=['GET'])
def getCannedFoodByFlavor(cfname):
    if request.method == 'GET':
        return CannedFoodHandler().getCannedFoodByName(cfname)
    else:
        return jsonify(Error="Method not allowed."), 405

##***********************************************DRY_FOOD**********************************************************************

@app.route('/ResourceApp/resources/dryfood', methods=['GET', 'POST'])
def getAllDryFood():
    if request.method == 'POST':
        
        print("REQUEST: ", request.json)
        return DryFoodHandler().insertDryFoodJson(request.json)
    else:
        if not request.args:
            return DryFoodHandler().getAllDryFood()

@app.route('/ResourceApp/resources/dryfood/<int:dfid>', methods=['GET', 'PUT', 'DELETE'])
def getDryFoodById(dfid):
    if request.method == 'GET':
        return DryFoodHandler().getDryFoodById(dfid)
    elif request.method == 'PUT':
        return DryFoodHandler().updateDryFood(dfid, request.form)
    elif request.method == 'DELETE':
        return DryFoodHandler().deleteDryFood(dfid)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/ResourceApp/resources/dryfood/brand/<string:dfbrand>', methods=['GET'])
def getDryFoodByBrand(dfbrand):
    if request.method == 'GET':
        return DryFoodHandler().getDryFoodByBrand(dfbrand)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/ResourceApp/resources/dryfood/name/<string:dfname>', methods=['GET'])
def getDryFoodByFlavor(dfname):
    if request.method == 'GET':
        return DryFoodHandler().getDryFoodByName(dfname)
    else:
        return jsonify(Error="Method not allowed."), 405


##***********************************************ICE**********************************************************************

@app.route('/ResourceApp/resources/ice', methods=['GET', 'POST'])
def getAllIce():
    if request.method == 'POST':
        
        print("REQUEST: ", request.json)
        return IceHandler().insertIceJson(request.json)
    else:
        if not request.args:
            return IceHandler().getAllIce()

@app.route('/ResourceApp/resources/ice/<int:iid>', methods=['GET', 'PUT', 'DELETE'])
def getIceById(iid):
    if request.method == 'GET':
        return IceHandler().getIceById(iid)
    elif request.method == 'PUT':
        return IceHandler().updateIce(iid, request.form)
    elif request.method == 'DELETE':
        return IceHandler().deleteIce(iid)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/ResourceApp/resources/ice/type/<string:itype>', methods=['GET'])
def getIceByType(itype):
    if request.method == 'GET':
        return IceHandler().getIceByType(itype)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/ResourceApp/resources/ice/weight/<string:iweight>', methods=['GET'])
def getIceByWeight(iweight):
    if request.method == 'GET':
        return IceHandler().getIceByWeight(iweight)
    else:
        return jsonify(Error="Method not allowed."), 405



##***********************************************TOOL**********************************************************************

@app.route('/ResourceApp/resources/tool', methods=['GET', 'POST'])
def getAllTool():
    if request.method == 'POST':
        
        print("REQUEST: ", request.json)
        return ToolHandler().insertToolJson(request.json)
    else:
        if not request.args:
            return ToolHandler().getAllTool()

@app.route('/ResourceApp/resources/tool/<int:tid>', methods=['GET', 'PUT', 'DELETE'])
def getToolById(tid):
    if request.method == 'GET':
        return ToolHandler().getToolById(tid)
    elif request.method == 'PUT':
        return ToolHandler().updateTool(tid, request.form)
    elif request.method == 'DELETE':
        return ToolHandler().deleteTool(tid)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/ResourceApp/resources/tool/brand/<string:tbrand>', methods=['GET'])
def getToolByBrand(tbrand):
    if request.method == 'GET':
        return ToolHandler().getToolByBrand(tbrand)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/ResourceApp/resources/tool/name/<string:tname>', methods=['GET'])
def getToolByName(tname):
    if request.method == 'GET':
        return ToolHandler().getToolByName(tname)
    else:
        return jsonify(Error="Method not allowed."), 405

##***********************************************WATER**********************************************************************

@app.route('/ResourceApp/resources/water', methods=['GET', 'POST'])
def getAllWater():
    if request.method == 'POST':
        
        print("REQUEST: ", request.json)
        return WaterHandler().insertWaterJson(request.json)
    else:
        if not request.args:
            return WaterHandler().getAllWater()


@app.route('/ResourceApp/resources/water/<int:wid>', methods=['GET', 'PUT', 'DELETE'])
def getWaterById(wid):
    if request.method == 'GET':
        return WaterHandler().getWaterById(wid)
    elif request.method == 'PUT':
        return WaterHandler().updateWater(wid, request.form)
    elif request.method == 'DELETE':
        return WaterHandler().deleteWater(wid)
    else:
        return jsonify(Error="Method not allowed."), 405


@app.route('/ResourceApp/resources/water/size/<string:wsize>', methods=['GET'])
def getWaterBySize(wsize):
    if request.method == 'GET':
        return WaterHandler().getWaterBySize(wsize)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/ResourceApp/resources/water/brand/<string:wbrand>', methods=['GET'])
def getWaterByBrand(wbrand):
    if request.method == 'GET':
        return WaterHandler().getWaterByBrand(wbrand)
    else:
        return jsonify(Error="Method not allowed."), 405


##***********************************************HEAVY EQUIPMENT**********************************************************************

@app.route('/ResourceApp/resources/heavyequipment', methods=['GET', 'POST'])
def getAllHeavyEquipment():
    if request.method == 'POST':
        
        print("REQUEST: ", request.json)
        return HeavyEquipmentHandler().insertHeavyEquipmentJson(request.json)
    else:
        if not request.args:
            return HeavyEquipmentHandler().getAllHeavyEquipment()


@app.route('/ResourceApp/resources/heavyequipment/<int:hid>', methods=['GET', 'PUT', 'DELETE'])
def getHeavyEquipmentById(hid):
    if request.method == 'GET':
        return HeavyEquipmentHandler().getHeavyEquipmentById(hid)
    elif request.method == 'PUT':
        return HeavyEquipmentHandler().updateHeavyEquipment(hid, request.form)
    elif request.method == 'DELETE':
        return HeavyEquipmentHandler().deleteHeavyEquipment(hid)
    else:
        return jsonify(Error="Method not allowed."), 405


@app.route('/ResourceApp/resources/heavyequipment/name/<string:hname>', methods=['GET'])
def getHeavyEquipmentByName(hname):
    if request.method == 'GET':
        return HeavyEquipmentHandler().getHeavyEquipmentByName(hname)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/ResourceApp/resources/heavyequipment/brand/<string:hbrand>', methods=['GET'])
def getHeavyEquipmentByBrand(hbrand):
    if request.method == 'GET':
        return HeavyEquipmentHandler().getHeavyEquipmentByBrand(hbrand)
    else:
        return jsonify(Error="Method not allowed."), 405

##***********************************************FUEL**********************************************************************

@app.route('/ResourceApp/resources/fuel', methods=['GET', 'POST'])
def getAllFuel():
    if request.method == 'POST':
        
        print("REQUEST: ", request.json)
        return FuelHandler().insertFuelJson(request.json)
    else:
        if not request.args:
            return FuelHandler().getAllFuel()


@app.route('/ResourceApp/resources/fuel/<int:fid>', methods=['GET', 'PUT', 'DELETE'])
def getFuelById(fid):
    if request.method == 'GET':
        return FuelHandler().getFuelById(fid)
    elif request.method == 'PUT':
        return FuelHandler().updateFuel(fid, request.form)
    elif request.method == 'DELETE':
        return FuelHandler().deleteFuel(fid)
    else:
        return jsonify(Error="Method not allowed."), 405


@app.route('/ResourceApp/resources/fuel/type/<string:ftype>', methods=['GET'])
def getFuelByType(ftype):
    if request.method == 'GET':
        return FuelHandler().getFuelByType(ftype)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/ResourceApp/resources/fuel/octane/<string:octane>', methods=['GET'])
def getFuelByOctance(octane):
    if request.method == 'GET':
        return FuelHandler().getFuelByOctane(octane)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/ResourceApp/resources/fuel/quantity/<string:fquantity>', methods=['GET'])
def getFuelByQuantity(fquantity):
    if request.method == 'GET':
        return FuelHandler().getFuelByQuantity(fquantity)
    else:
        return jsonify(Error="Method not allowed."), 405



##***********************************************GENERATOR**********************************************************************

@app.route('/ResourceApp/resources/generator', methods=['GET', 'POST'])
def getAllGenerator():
    if request.method == 'POST':
        
        print("REQUEST: ", request.json)
        return GeneratorHandler().insertGeneratorJson(request.json)
    else:
        if not request.args:
            return GeneratorHandler().getAllGenerator()

@app.route('/ResourceApp/resources/generator/<int:gid>', methods=['GET', 'PUT', 'DELETE'])
def getGeneratorById(gid):
    if request.method == 'GET':
        return GeneratorHandler().getGeneratorById(gid)
    elif request.method == 'PUT':
        return GeneratorHandler().updateGenerator(gid, request.form)
    elif request.method == 'DELETE':
        return GeneratorHandler().deleteGenerator(gid)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/ResourceApp/resources/generator/fueltype/<string:gfueltype>', methods=['GET'])
def getGeneratorByFuelType(gfueltype):
    if request.method == 'GET':
        return GeneratorHandler().getGeneratorByFuelType(gfueltype)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/ResourceApp/resources/generator/poweroutput/<string:gpoweroutput>', methods=['GET'])
def getGeneratorByPowerOutput(gpoweroutput):
    if request.method == 'GET':
        return GeneratorHandler().getGeneratorByPowerOutput(gpoweroutput)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/ResourceApp/resources/countbyresourceid')
def getCountByResourceId():
    return ResourceHandler().getCountByResourceId()

##************************************************CLOTHING***************************************************************

@app.route('/ResourceApp/resources/clothing', methods=['GET', 'POST'])
def getAllClothing():
    if request.method == 'POST':
        
        print("REQUEST: ", request.json)
        return ClothingHandler().insertClothingJson(request.json)
    else:
        if not request.args:
            return ClothingHandler().getAllClothing()


@app.route('/ResourceApp/resources/clothing/<int:clid>', methods=['GET', 'PUT', 'DELETE'])
def getClothingById(clid):
    if request.method == 'GET':
        return ClothingHandler().getClothingById(clid)
    elif request.method == 'PUT':
        return ClothingHandler().updateClothing(clid, request.form)
    elif request.method == 'DELETE':
        return ClothingHandler().deleteClothing(clid)
    else:
        return jsonify(Error="Method not allowed."), 405


@app.route('/ResourceApp/resources/clothing/brand/<string:clbrand>', methods=['GET'])
def getClothingByBrand(clbrand):
    if request.method == 'GET':
        return ClothingHandler().getClothingByBrand(clbrand)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/ResourceApp/resources/clothing/name/<string:clname>', methods=['GET'])
def getClothingByName(clname):
    if request.method == 'GET':
        return ClothingHandler().getClothingByName(clname)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/ResourceApp/resources/clothing/size/<string:clsize>', methods=['GET'])
def getClothingBySize(clsize):
    if request.method == 'GET':
        return ClothingHandler().getClothingBySize(clsize)
    else:
        return jsonify(Error="Method not allowed."), 405

##********************************************************BATTERIES*********************************************************************************

@app.route('/ResourceApp/resources/batteries', methods=['GET', 'POST'])
def getAllBatteries():
    if request.method == 'POST':
        
        print("REQUEST: ", request.json)
        return BatteriesHandler().insertBatteriesJson(request.json)
    else:
        if not request.args:
            return BatteriesHandler().getAllBatteries()


@app.route('/ResourceApp/resources/batteries/<int:bid>', methods=['GET', 'PUT', 'DELETE'])
def getBatteriesById(bid):
    if request.method == 'GET':
        return BatteriesHandler().getBatteriesById(bid)
    elif request.method == 'PUT':
        return BatteriesHandler().updateBatteries(bid, request.form)
    elif request.method == 'DELETE':
        return BatteriesHandler().deleteBatteries(bid)
    else:
        return jsonify(Error="Method not allowed."), 405


@app.route('/ResourceApp/resources/batteries/brand/<string:bbrand>', methods=['GET'])
def getBatteriesByBrand(bbrand):
    if request.method == 'GET':
        return BatteriesHandler().getBatteriesByBrand(bbrand)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/ResourceApp/resources/batteries/type/<string:btype>', methods=['GET'])
def getBatteriesByType(btype):
    if request.method == 'GET':
        return BatteriesHandler().getBatteriesByType(btype)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/ResourceApp/resources/batteries/life/<string:blife>', methods=['GET'])
def getBatteriesByLife(blife):
    if request.method == 'GET':
        return BatteriesHandler().getBatteriesByLife(blife)
    else:
        return jsonify(Error="Method not allowed."), 405

#************************************************************ Users & Administrators ******************************************************************************

@app.route('/ResourceApp/user', methods=['GET', 'POST'])
def getAllUsers():
    if request.method == 'POST':
        return userHandler().insertUser(request.form)
    else:
        return userHandler().getAllUsers()

#Get All Admins or REGISTER AS ADMIN
@app.route('/ResourceApp/user/administrator', methods=['GET', 'POST'])
def getAllAdmins():
    if request.method == 'POST':
        return adminHandler().insertAdmin(request.form)
    else:
        return adminHandler().getAllAdmins()

@app.route('/ResourceApp/user/id/<int:uid>', methods=['GET', 'PUT', 'DELETE'])
def getUserById(uid):
    if request.method == 'GET':
        return userHandler().getUserById(uid)
    elif request.method == 'PUT':
        return userHandler().updateUser(uid, request.form)
    elif request.method == 'DELETE':
        return userHandler().deleteUser(uid)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/ResourceApp/user/administrator/adminId/<int:aid>', methods=['GET', 'PUT', 'DELETE'])
def getAdminByAid(aid):
    if request.method == 'GET':
        return adminHandler().getAdminByAdminId(aid)
    elif request.method == 'PUT':
        pass
    elif request.method == 'DELETE':
        return adminHandler().deleteAdmin(aid)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/ResourceApp/user/administrator/userId/<int:uid>', methods=['GET', 'PUT', 'DELETE'])
def getAdminByUid(uid):
    if request.method == 'GET':
        return adminHandler().getAdminByUserId(uid)
    elif request.method == 'PUT':
        pass
    elif request.method == 'DELETE':
        pass
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/ResourceApp/user/username/<string:username>', methods=['GET'])
def getUserByUsername(username):
    if request.method == 'GET':
        return userHandler().getUserByUsername(username)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/ResourceApp/user/firstname/<string:fname>', methods=['GET'])
def getUserByfame(fname):
    if request.method == 'GET':
        return userHandler().getUserByFirstName(fname)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/ResourceApp/user/lastname/<string:lname>', methods=['GET'])
def getUserBylname(lname):
    if request.method == 'GET':
        return userHandler().getUserByLastName(lname)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/ResourceApp/user/email/<string:email>', methods=['GET'])
def getUserByEmail(email):
    if request.method == 'GET':
        return userHandler().getUserByEmail(email)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/ResourceApp/user/phone/<int:phone>', methods=['GET'])
def getUserByPhone(phone):
    if request.method == 'GET':
        return userHandler().getUserByPhoneNumber(phone)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/ResourceApp/user/address/<string:address>', methods=['GET'])
def getUserByAddress(address):
    if request.method == 'GET':
        return userHandler().getUserByAddress(address)
    else:
        return jsonify(Error="Method not allowed."), 405

if __name__ == '__main__':
    app.run()