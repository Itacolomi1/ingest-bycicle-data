use BycicleDB;

CREATE TABLE `person.person`(
BusinessEntityID int not null,
PersonType char(2),
NameStyle int,
Title varchar(255),
FirstName varchar(255),
MiddleName varchar(255),
LastName varchar(255),
Suffix varchar(255),
EmailPromotion tinyint,
AdditionalContactInfo varchar(255),
Demographics varchar(255),
rowguid varchar(255),
ModifiedDate datetime,
PRIMARY KEY (`BusinessEntityID`)
);

CREATE TABLE `sales.customer`(
CustomerID int not null,
PersonID int,
StoreID int,
TerritoryID tinyint,
AccountNumber varchar(255),
rowguid varchar(255),
ModifiedDate datetime,
PRIMARY KEY (`CustomerID`),
FOREIGN KEY (`PersonID`) REFERENCES `person.person` (`BusinessEntityID`)
);

CREATE TABLE `sales.salesOrderHeader`(
SalesOrderID int not null,
RevisionNumber tinyint,
OrderDate datetime,
DueDate datetime,
ShipDate datetime,
Status tinyint,
OnlineOrderFlag bit,
SalesOrderNumber varchar(255),
PurchaseOrderNumber varchar(255),
AccountNumber varchar(255),
CustomerID int,
SalesPersonID int,
TerritoryID tinyint,
BillToAddressID int,
ShipToAddressID int,
ShipMethodID tinyint,
CreditCardID int,
CreditCardApprovalCode varchar(255),
CurrencyRateID int,
SubTotal float,
TaxAmt float,
Freight float,
TotalDue float,
Comment varchar(255),
rowguid varchar(255),
ModifiedDate datetime,
PRIMARY KEY (`SalesOrderID`),
FOREIGN KEY (`CustomerID`) REFERENCES `sales.customer` (`CustomerID`)
);

CREATE TABLE `production.product`(
ProductID int not null,
Name varchar(255),
ProductNumber varchar(255),
MakeFlag bit,
FinishedGoodsFlag bit,
Color varchar(255),
SafetyStockLevel int,
ReorderPoint int,
StandardCost float,
ListPrice float,
Size varchar(255),
SizeUnitMeasureCode varchar(255),
WeightUnitMeasureCode varchar(255),
Weight float,
DaysToManufacture tinyint,
ProductLine char(1),
Class char(1),
Style char(1),
ProductSubcategoryID int,
ProductModelID int,
SellStartDate datetime,
SellEndDate datetime,
DiscontinuedDate datetime,
rowguid varchar(255),
ModifiedDate datetime,
PRIMARY KEY (`ProductID`)
);

CREATE TABLE `sales.specialOfferProduct`(
SpecialOfferID int not null,
ProductID int not null,
rowguid varchar(255),
ModifiedDate datetime,
PRIMARY KEY (`SpecialOfferID`,`ProductID`),
FOREIGN KEY (`ProductID`) REFERENCES `production.product` (`ProductID`)
);

CREATE TABLE `sales.salesOrderDetail`(
SalesOrderID int not null,
SalesOrderDetailID int not null,
CarrierTrackingNumber varchar(255),
OrderQty int,
ProductID int,
SpecialOfferID int,
UnitPrice float,
UnitPriceDiscount int,
LineTotal bigint,
rowguid varchar(255),
ModifiedDate datetime,
PRIMARY KEY (`SalesOrderID`,`SalesOrderDetailID`),
FOREIGN KEY (`ProductID`,`SpecialOfferID`) REFERENCES `sales.specialOfferProduct` (`ProductID`,`SpecialOfferID`),
FOREIGN KEY (`SalesOrderID`) REFERENCES `sales.salesOrderHeader` (`SalesOrderID`)
);








