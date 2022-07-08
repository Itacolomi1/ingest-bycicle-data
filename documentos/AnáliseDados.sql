
use BycicleDB;

-- Análise 1
SELECT 
	SalesOrderID as id, 
	COUNT(*) AS qtd 
FROM `sales.salesOrderDetail` as sod
GROUP BY SalesOrderID
HAVING qtd >= 3;

-- Análise 2

SELECT * FROM (
  SELECT p.DaysToManufacture AS dtm,
         ROW_NUMBER() OVER(PARTITION BY p.DaysToManufacture ORDER BY sum(sod.OrderQty) DESC) as pos,
         p.Name as name,
         sum(sod.OrderQty) AS qtd
  FROM `sales.specialOfferProduct` AS sop 
  INNER JOIN `production.product` AS p ON sop.ProductID = p.ProductID
  INNER JOIN `sales.salesOrderDetail` AS sod ON sop.SpecialOfferID = sod.SalesOrderDetailID
  GROUP BY name
  ) as by_pos
WHERE pos <= 3 LIMIT 3;

-- Análise 3

SELECT c.CustomerID as id, 
       p.FirstName as nomeCliente, 
       COUNT(*) AS qtd 
FROM `sales.salesOrderHeader` as soh
INNER JOIN	`sales.customer` as c ON soh.CustomerID = c.CustomerID
INNER JOIN `person.person` as p ON c.PersonID = p.BusinessEntityID 
GROUP BY c.PersonID
ORDER BY qtd DESC;

-- Análise 4
SELECT sod.ProductID as id, 
       p.Name as nomeProduto,
       sum(OrderQty) OVER(PARTITION BY sod.ProductID) AS qtd_id,
       soh.OrderDate,  
       sum(OrderQty) OVER(PARTITION BY soh.OrderDate) AS qtd_OrderDate
FROM `sales.salesOrderDetail` AS sod
INNER JOIN `sales.salesOrderHeader` as soh ON sod.SalesOrderID  = soh.SalesOrderID 
INNER JOIN `production.product` AS p ON sod.ProductID = p.ProductID 
GROUP BY sod.ProductID, soh.OrderDate
ORDER BY soh.OrderDate;

-- Análise 5
SELECT SalesOrderID, DATE(OrderDate), TotalDue 
FROM `sales.salesOrderHeader` AS soh 
WHERE DATE(OrderDate) BETWEEN DATE('2011-09-01') AND DATE('2011-09-30') AND TotalDue > 1.000
ORDER BY TotalDue DESC;





