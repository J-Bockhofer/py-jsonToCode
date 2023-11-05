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
