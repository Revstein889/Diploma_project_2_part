#Для этого: выведи список логинов курьеров с количеством их заказов в статусе «В доставке» (поле inDelivery = true).
SELECT c.login,
    COUNT(o.id) AS "deliveryCount"
FROM "Couriers" AS c
    LEFT JOIN "Orders" AS o ON c.id = o."courierId"
GROUP BY c.login;

#Для этого: выведи все трекеры заказов и их статусы.

SELECT track,
       CASE
           WHEN finished = true THEN 2
           WHEN cancelled = true THEN -1
           WHEN "inDelivery" = true THEN 1
                   ELSE 0
       END
FROM "Orders";

