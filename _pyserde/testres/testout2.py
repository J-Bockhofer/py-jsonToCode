class L_0_56_1:
    def __init__(self, id:int, isMain:str, mainVariationId:str, itemId:int, categoryVariationId:int, marketVariationId:int, clientVariationId:int, salesPriceVariationId:int, supplierVariationId:int, warehouseVariationId:int, position:int, isActive:str, number:str, model:str, externalId:str, parentVariationId:str, parentVariationQuantity:str, availability:int, estimatedAvailableAt:str, purchasePrice:int, createdAt:str, updatedAt:str, relatedUpdatedAt:str, priceCalculationId:str, priceCalculationUUID:str, picking:str, stockLimitation:int, isVisibleIfNetStockIsPositive:str, isInvisibleIfNetStockIsNotPositive:str, isAvailableIfNetStockIsPositive:str, isUnavailableIfNetStockIsNotPositive:str, mainWarehouseId:int, maximumOrderQuantity:str, minimumOrderQuantity:str, intervalOrderQuantity:str, availableUntil:str, releasedAt:str, unitCombinationId:int, name:str, weightG:int, weightNetG:int, widthMM:int, lengthMM:int, heightMM:int, extraShippingCharge1:str, extraShippingCharge2:str, unitsContained:int, palletTypeId:str, packingUnits:str, packingUnitTypeId:str, transportationCosts:int, storageCosts:int, customs:str, operatingCosts:str, vatId:int, bundleType:str, automaticClientVisibility:int, isHiddenInCategoryList:str, defaultShippingCosts:int, mayShowUnitPrice:str, movingAveragePrice:int, propertyVariationId:str, automaticListVisibility:int, isVisibleInListIfNetStockIsPositive:str, isInvisibleInListIfNetStockIsNotPositive:str, singleItemCount:int, availabilityUpdatedAt:str, tagVariationId:str, hasCalculatedBundleWeight:str, hasCalculatedBundleNetWeight:str, hasCalculatedBundlePurchasePrice:str, hasCalculatedBundleMovingAveragePrice:str, customsTariffNumber:str, salesRank:str):
        self.id = id
        self.isMain = isMain
        self.mainVariationId = mainVariationId
        self.itemId = itemId
        self.categoryVariationId = categoryVariationId
        self.marketVariationId = marketVariationId
        self.clientVariationId = clientVariationId
        self.salesPriceVariationId = salesPriceVariationId
        self.supplierVariationId = supplierVariationId
        self.warehouseVariationId = warehouseVariationId
        self.position = position
        self.isActive = isActive
        self.number = number
        self.model = model
        self.externalId = externalId
        self.parentVariationId = parentVariationId
        self.parentVariationQuantity = parentVariationQuantity
        self.availability = availability
        self.estimatedAvailableAt = estimatedAvailableAt
        self.purchasePrice = purchasePrice
        self.createdAt = createdAt
        self.updatedAt = updatedAt
        self.relatedUpdatedAt = relatedUpdatedAt
        self.priceCalculationId = priceCalculationId
        self.priceCalculationUUID = priceCalculationUUID
        self.picking = picking
        self.stockLimitation = stockLimitation
        self.isVisibleIfNetStockIsPositive = isVisibleIfNetStockIsPositive
        self.isInvisibleIfNetStockIsNotPositive = isInvisibleIfNetStockIsNotPositive
        self.isAvailableIfNetStockIsPositive = isAvailableIfNetStockIsPositive
        self.isUnavailableIfNetStockIsNotPositive = isUnavailableIfNetStockIsNotPositive
        self.mainWarehouseId = mainWarehouseId
        self.maximumOrderQuantity = maximumOrderQuantity
        self.minimumOrderQuantity = minimumOrderQuantity
        self.intervalOrderQuantity = intervalOrderQuantity
        self.availableUntil = availableUntil
        self.releasedAt = releasedAt
        self.unitCombinationId = unitCombinationId
        self.name = name
        self.weightG = weightG
        self.weightNetG = weightNetG
        self.widthMM = widthMM
        self.lengthMM = lengthMM
        self.heightMM = heightMM
        self.extraShippingCharge1 = extraShippingCharge1
        self.extraShippingCharge2 = extraShippingCharge2
        self.unitsContained = unitsContained
        self.palletTypeId = palletTypeId
        self.packingUnits = packingUnits
        self.packingUnitTypeId = packingUnitTypeId
        self.transportationCosts = transportationCosts
        self.storageCosts = storageCosts
        self.customs = customs
        self.operatingCosts = operatingCosts
        self.vatId = vatId
        self.bundleType = bundleType
        self.automaticClientVisibility = automaticClientVisibility
        self.isHiddenInCategoryList = isHiddenInCategoryList
        self.defaultShippingCosts = defaultShippingCosts
        self.mayShowUnitPrice = mayShowUnitPrice
        self.movingAveragePrice = movingAveragePrice
        self.propertyVariationId = propertyVariationId
        self.automaticListVisibility = automaticListVisibility
        self.isVisibleInListIfNetStockIsPositive = isVisibleInListIfNetStockIsPositive
        self.isInvisibleInListIfNetStockIsNotPositive = isInvisibleInListIfNetStockIsNotPositive
        self.singleItemCount = singleItemCount
        self.availabilityUpdatedAt = availabilityUpdatedAt
        self.tagVariationId = tagVariationId
        self.hasCalculatedBundleWeight = hasCalculatedBundleWeight
        self.hasCalculatedBundleNetWeight = hasCalculatedBundleNetWeight
        self.hasCalculatedBundlePurchasePrice = hasCalculatedBundlePurchasePrice
        self.hasCalculatedBundleMovingAveragePrice = hasCalculatedBundleMovingAveragePrice
        self.customsTariffNumber = customsTariffNumber
        self.salesRank = salesRank
    def to_dict(self)->dict:
        return {"id": self.id, "isMain": self.isMain, "mainVariationId": self.mainVariationId, "itemId": self.itemId, "categoryVariationId": self.categoryVariationId, "marketVariationId": self.marketVariationId, "clientVariationId": self.clientVariationId, "salesPriceVariationId": self.salesPriceVariationId, "supplierVariationId": self.supplierVariationId, "warehouseVariationId": self.warehouseVariationId, "position": self.position, "isActive": self.isActive, "number": self.number, "model": self.model, "externalId": self.externalId, "parentVariationId": self.parentVariationId, "parentVariationQuantity": self.parentVariationQuantity, "availability": self.availability, "estimatedAvailableAt": self.estimatedAvailableAt, "purchasePrice": self.purchasePrice, "createdAt": self.createdAt, "updatedAt": self.updatedAt, "relatedUpdatedAt": self.relatedUpdatedAt, "priceCalculationId": self.priceCalculationId, "priceCalculationUUID": self.priceCalculationUUID, "picking": self.picking, "stockLimitation": self.stockLimitation, "isVisibleIfNetStockIsPositive": self.isVisibleIfNetStockIsPositive, "isInvisibleIfNetStockIsNotPositive": self.isInvisibleIfNetStockIsNotPositive, "isAvailableIfNetStockIsPositive": self.isAvailableIfNetStockIsPositive, "isUnavailableIfNetStockIsNotPositive": self.isUnavailableIfNetStockIsNotPositive, "mainWarehouseId": self.mainWarehouseId, "maximumOrderQuantity": self.maximumOrderQuantity, "minimumOrderQuantity": self.minimumOrderQuantity, "intervalOrderQuantity": self.intervalOrderQuantity, "availableUntil": self.availableUntil, "releasedAt": self.releasedAt, "unitCombinationId": self.unitCombinationId, "name": self.name, "weightG": self.weightG, "weightNetG": self.weightNetG, "widthMM": self.widthMM, "lengthMM": self.lengthMM, "heightMM": self.heightMM, "extraShippingCharge1": self.extraShippingCharge1, "extraShippingCharge2": self.extraShippingCharge2, "unitsContained": self.unitsContained, "palletTypeId": self.palletTypeId, "packingUnits": self.packingUnits, "packingUnitTypeId": self.packingUnitTypeId, "transportationCosts": self.transportationCosts, "storageCosts": self.storageCosts, "customs": self.customs, "operatingCosts": self.operatingCosts, "vatId": self.vatId, "bundleType": self.bundleType, "automaticClientVisibility": self.automaticClientVisibility, "isHiddenInCategoryList": self.isHiddenInCategoryList, "defaultShippingCosts": self.defaultShippingCosts, "mayShowUnitPrice": self.mayShowUnitPrice, "movingAveragePrice": self.movingAveragePrice, "propertyVariationId": self.propertyVariationId, "automaticListVisibility": self.automaticListVisibility, "isVisibleInListIfNetStockIsPositive": self.isVisibleInListIfNetStockIsPositive, "isInvisibleInListIfNetStockIsNotPositive": self.isInvisibleInListIfNetStockIsNotPositive, "singleItemCount": self.singleItemCount, "availabilityUpdatedAt": self.availabilityUpdatedAt, "tagVariationId": self.tagVariationId, "hasCalculatedBundleWeight": self.hasCalculatedBundleWeight, "hasCalculatedBundleNetWeight": self.hasCalculatedBundleNetWeight, "hasCalculatedBundlePurchasePrice": self.hasCalculatedBundlePurchasePrice, "hasCalculatedBundleMovingAveragePrice": self.hasCalculatedBundleMovingAveragePrice, "customsTariffNumber": self.customsTariffNumber, "salesRank": self.salesRank}
    @classmethod
    def from_dict(cls, data:dict):
        if "id" in data and "isMain" in data and "mainVariationId" in data and "itemId" in data and "categoryVariationId" in data and "marketVariationId" in data and "clientVariationId" in data and "salesPriceVariationId" in data and "supplierVariationId" in data and "warehouseVariationId" in data and "position" in data and "isActive" in data and "number" in data and "model" in data and "externalId" in data and "parentVariationId" in data and "parentVariationQuantity" in data and "availability" in data and "estimatedAvailableAt" in data and "purchasePrice" in data and "createdAt" in data and "updatedAt" in data and "relatedUpdatedAt" in data and "priceCalculationId" in data and "priceCalculationUUID" in data and "picking" in data and "stockLimitation" in data and "isVisibleIfNetStockIsPositive" in data and "isInvisibleIfNetStockIsNotPositive" in data and "isAvailableIfNetStockIsPositive" in data and "isUnavailableIfNetStockIsNotPositive" in data and "mainWarehouseId" in data and "maximumOrderQuantity" in data and "minimumOrderQuantity" in data and "intervalOrderQuantity" in data and "availableUntil" in data and "releasedAt" in data and "unitCombinationId" in data and "name" in data and "weightG" in data and "weightNetG" in data and "widthMM" in data and "lengthMM" in data and "heightMM" in data and "extraShippingCharge1" in data and "extraShippingCharge2" in data and "unitsContained" in data and "palletTypeId" in data and "packingUnits" in data and "packingUnitTypeId" in data and "transportationCosts" in data and "storageCosts" in data and "customs" in data and "operatingCosts" in data and "vatId" in data and "bundleType" in data and "automaticClientVisibility" in data and "isHiddenInCategoryList" in data and "defaultShippingCosts" in data and "mayShowUnitPrice" in data and "movingAveragePrice" in data and "propertyVariationId" in data and "automaticListVisibility" in data and "isVisibleInListIfNetStockIsPositive" in data and "isInvisibleInListIfNetStockIsNotPositive" in data and "singleItemCount" in data and "availabilityUpdatedAt" in data and "tagVariationId" in data and "hasCalculatedBundleWeight" in data and "hasCalculatedBundleNetWeight" in data and "hasCalculatedBundlePurchasePrice" in data and "hasCalculatedBundleMovingAveragePrice" in data and "customsTariffNumber" in data and "salesRank" in data:
            
            return cls(data["id"], data["isMain"], data["mainVariationId"], data["itemId"], data["categoryVariationId"], data["marketVariationId"], data["clientVariationId"], data["salesPriceVariationId"], data["supplierVariationId"], data["warehouseVariationId"], data["position"], data["isActive"], data["number"], data["model"], data["externalId"], data["parentVariationId"], data["parentVariationQuantity"], data["availability"], data["estimatedAvailableAt"], data["purchasePrice"], data["createdAt"], data["updatedAt"], data["relatedUpdatedAt"], data["priceCalculationId"], data["priceCalculationUUID"], data["picking"], data["stockLimitation"], data["isVisibleIfNetStockIsPositive"], data["isInvisibleIfNetStockIsNotPositive"], data["isAvailableIfNetStockIsPositive"], data["isUnavailableIfNetStockIsNotPositive"], data["mainWarehouseId"], data["maximumOrderQuantity"], data["minimumOrderQuantity"], data["intervalOrderQuantity"], data["availableUntil"], data["releasedAt"], data["unitCombinationId"], data["name"], data["weightG"], data["weightNetG"], data["widthMM"], data["lengthMM"], data["heightMM"], data["extraShippingCharge1"], data["extraShippingCharge2"], data["unitsContained"], data["palletTypeId"], data["packingUnits"], data["packingUnitTypeId"], data["transportationCosts"], data["storageCosts"], data["customs"], data["operatingCosts"], data["vatId"], data["bundleType"], data["automaticClientVisibility"], data["isHiddenInCategoryList"], data["defaultShippingCosts"], data["mayShowUnitPrice"], data["movingAveragePrice"], data["propertyVariationId"], data["automaticListVisibility"], data["isVisibleInListIfNetStockIsPositive"], data["isInvisibleInListIfNetStockIsNotPositive"], data["singleItemCount"], data["availabilityUpdatedAt"], data["tagVariationId"], data["hasCalculatedBundleWeight"], data["hasCalculatedBundleNetWeight"], data["hasCalculatedBundlePurchasePrice"], data["hasCalculatedBundleMovingAveragePrice"], data["customsTariffNumber"], data["salesRank"])
        else:
            raise KeyError("Invalid data for L_0_56_1")
class L_0_57_1:
    def __init__(self, lang:str, name1:str, name2:str, name3:str, shortDescription:str, metaDescription:str, description:str, technicalData:str, urlPath:str, keywords:str):
        self.lang = lang
        self.name1 = name1
        self.name2 = name2
        self.name3 = name3
        self.shortDescription = shortDescription
        self.metaDescription = metaDescription
        self.description = description
        self.technicalData = technicalData
        self.urlPath = urlPath
        self.keywords = keywords
    def to_dict(self)->dict:
        return {"lang": self.lang, "name1": self.name1, "name2": self.name2, "name3": self.name3, "shortDescription": self.shortDescription, "metaDescription": self.metaDescription, "description": self.description, "technicalData": self.technicalData, "urlPath": self.urlPath, "keywords": self.keywords}
    @classmethod
    def from_dict(cls, data:dict):
        if "lang" in data and "name1" in data and "name2" in data and "name3" in data and "shortDescription" in data and "metaDescription" in data and "description" in data and "technicalData" in data and "urlPath" in data and "keywords" in data:
            
            return cls(data["lang"], data["name1"], data["name2"], data["name3"], data["shortDescription"], data["metaDescription"], data["description"], data["technicalData"], data["urlPath"], data["keywords"])
        else:
            raise KeyError("Invalid data for L_0_57_1")
class L_0:
    def __init__(self, id:int, position:int, manufacturerId:int, stockType:int, add_cms_page:str, storeSpecial:int, condition:int, amazonFedas:str, updatedAt:str, free1:str, free2:str, free3:str, free4:str, free5:str, free6:str, free7:str, free8:str, free9:str, free10:str, free11:str, free12:str, free13:str, free14:str, free15:str, free16:str, free17:str, free18:str, free19:str, free20:str, customsTariffNumber:str, producingCountryId:int, revenueAccount:int, couponRestriction:int, flagOne:int, flagTwo:int, ageRestriction:int, createdAt:str, amazonProductType:int, ebayPresetId:int, ebayCategory:int, ebayCategory2:int, ebayStoreCategory:int, ebayStoreCategory2:int, amazonFbaPlatform:int, feedback:int, gimahhot:str, maximumOrderQuantity:int, isSubscribable:str, rakutenCategoryId:int, isShippingPackage:str, conditionApi:int, isSerialNumber:str, isShippableByAmazon:str, ownerId:str, itemType:str, mainVariationId:int, variations:list[L_0_56_1], texts:list[L_0_57_1]):
        self.id = id
        self.position = position
        self.manufacturerId = manufacturerId
        self.stockType = stockType
        self.add_cms_page = add_cms_page
        self.storeSpecial = storeSpecial
        self.condition = condition
        self.amazonFedas = amazonFedas
        self.updatedAt = updatedAt
        self.free1 = free1
        self.free2 = free2
        self.free3 = free3
        self.free4 = free4
        self.free5 = free5
        self.free6 = free6
        self.free7 = free7
        self.free8 = free8
        self.free9 = free9
        self.free10 = free10
        self.free11 = free11
        self.free12 = free12
        self.free13 = free13
        self.free14 = free14
        self.free15 = free15
        self.free16 = free16
        self.free17 = free17
        self.free18 = free18
        self.free19 = free19
        self.free20 = free20
        self.customsTariffNumber = customsTariffNumber
        self.producingCountryId = producingCountryId
        self.revenueAccount = revenueAccount
        self.couponRestriction = couponRestriction
        self.flagOne = flagOne
        self.flagTwo = flagTwo
        self.ageRestriction = ageRestriction
        self.createdAt = createdAt
        self.amazonProductType = amazonProductType
        self.ebayPresetId = ebayPresetId
        self.ebayCategory = ebayCategory
        self.ebayCategory2 = ebayCategory2
        self.ebayStoreCategory = ebayStoreCategory
        self.ebayStoreCategory2 = ebayStoreCategory2
        self.amazonFbaPlatform = amazonFbaPlatform
        self.feedback = feedback
        self.gimahhot = gimahhot
        self.maximumOrderQuantity = maximumOrderQuantity
        self.isSubscribable = isSubscribable
        self.rakutenCategoryId = rakutenCategoryId
        self.isShippingPackage = isShippingPackage
        self.conditionApi = conditionApi
        self.isSerialNumber = isSerialNumber
        self.isShippableByAmazon = isShippableByAmazon
        self.ownerId = ownerId
        self.itemType = itemType
        self.mainVariationId = mainVariationId
        self.variations = variations
        self.texts = texts
    def to_dict(self)->dict:
        return {"id": self.id, "position": self.position, "manufacturerId": self.manufacturerId, "stockType": self.stockType, "add_cms_page": self.add_cms_page, "storeSpecial": self.storeSpecial, "condition": self.condition, "amazonFedas": self.amazonFedas, "updatedAt": self.updatedAt, "free1": self.free1, "free2": self.free2, "free3": self.free3, "free4": self.free4, "free5": self.free5, "free6": self.free6, "free7": self.free7, "free8": self.free8, "free9": self.free9, "free10": self.free10, "free11": self.free11, "free12": self.free12, "free13": self.free13, "free14": self.free14, "free15": self.free15, "free16": self.free16, "free17": self.free17, "free18": self.free18, "free19": self.free19, "free20": self.free20, "customsTariffNumber": self.customsTariffNumber, "producingCountryId": self.producingCountryId, "revenueAccount": self.revenueAccount, "couponRestriction": self.couponRestriction, "flagOne": self.flagOne, "flagTwo": self.flagTwo, "ageRestriction": self.ageRestriction, "createdAt": self.createdAt, "amazonProductType": self.amazonProductType, "ebayPresetId": self.ebayPresetId, "ebayCategory": self.ebayCategory, "ebayCategory2": self.ebayCategory2, "ebayStoreCategory": self.ebayStoreCategory, "ebayStoreCategory2": self.ebayStoreCategory2, "amazonFbaPlatform": self.amazonFbaPlatform, "feedback": self.feedback, "gimahhot": self.gimahhot, "maximumOrderQuantity": self.maximumOrderQuantity, "isSubscribable": self.isSubscribable, "rakutenCategoryId": self.rakutenCategoryId, "isShippingPackage": self.isShippingPackage, "conditionApi": self.conditionApi, "isSerialNumber": self.isSerialNumber, "isShippableByAmazon": self.isShippableByAmazon, "ownerId": self.ownerId, "itemType": self.itemType, "mainVariationId": self.mainVariationId, "variations": [x.to_dict() for x in self.variations], "texts": [x.to_dict() for x in self.texts]}
    @classmethod
    def from_dict(cls, data:dict):
        if "id" in data and "position" in data and "manufacturerId" in data and "stockType" in data and "add_cms_page" in data and "storeSpecial" in data and "condition" in data and "amazonFedas" in data and "updatedAt" in data and "free1" in data and "free2" in data and "free3" in data and "free4" in data and "free5" in data and "free6" in data and "free7" in data and "free8" in data and "free9" in data and "free10" in data and "free11" in data and "free12" in data and "free13" in data and "free14" in data and "free15" in data and "free16" in data and "free17" in data and "free18" in data and "free19" in data and "free20" in data and "customsTariffNumber" in data and "producingCountryId" in data and "revenueAccount" in data and "couponRestriction" in data and "flagOne" in data and "flagTwo" in data and "ageRestriction" in data and "createdAt" in data and "amazonProductType" in data and "ebayPresetId" in data and "ebayCategory" in data and "ebayCategory2" in data and "ebayStoreCategory" in data and "ebayStoreCategory2" in data and "amazonFbaPlatform" in data and "feedback" in data and "gimahhot" in data and "maximumOrderQuantity" in data and "isSubscribable" in data and "rakutenCategoryId" in data and "isShippingPackage" in data and "conditionApi" in data and "isSerialNumber" in data and "isShippableByAmazon" in data and "ownerId" in data and "itemType" in data and "mainVariationId" in data and "variations" in data and "texts" in data:
            classlist = [L_0_57_1.from_dict(classdata) for classdata in data.get("texts", [])]
            return cls(data["id"], data["position"], data["manufacturerId"], data["stockType"], data["add_cms_page"], data["storeSpecial"], data["condition"], data["amazonFedas"], data["updatedAt"], data["free1"], data["free2"], data["free3"], data["free4"], data["free5"], data["free6"], data["free7"], data["free8"], data["free9"], data["free10"], data["free11"], data["free12"], data["free13"], data["free14"], data["free15"], data["free16"], data["free17"], data["free18"], data["free19"], data["free20"], data["customsTariffNumber"], data["producingCountryId"], data["revenueAccount"], data["couponRestriction"], data["flagOne"], data["flagTwo"], data["ageRestriction"], data["createdAt"], data["amazonProductType"], data["ebayPresetId"], data["ebayCategory"], data["ebayCategory2"], data["ebayStoreCategory"], data["ebayStoreCategory2"], data["amazonFbaPlatform"], data["feedback"], data["gimahhot"], data["maximumOrderQuantity"], data["isSubscribable"], data["rakutenCategoryId"], data["isShippingPackage"], data["conditionApi"], data["isSerialNumber"], data["isShippableByAmazon"], data["ownerId"], data["itemType"], data["mainVariationId"], classlist, classlist)
        else:
            raise KeyError("Invalid data for L_0")
