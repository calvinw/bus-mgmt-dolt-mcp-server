DROP VIEW IF EXISTS `completed`;
CREATE VIEW `completed` AS
SELECT
    o.`order_id`,
    p.`name`,
    p.`price`,
    o.`customer`,
    o.`quantity`,
    o.`order_date`,
    o.`completed`
FROM
    orders o
JOIN
    products p ON o.`product_id` = p.`product_id`
WHERE
    o.`completed` = 1;

DROP VIEW IF EXISTS `inprogress`;
CREATE VIEW `inprogress` AS
SELECT
    o.`order_id`,
    o.`customer`,
    p.`name`,
    p.`price`,
    o.`quantity`,
    o.`order_date`,
    o.`completed`
FROM
    orders o
JOIN
    products p ON o.`product_id` = p.`product_id`
WHERE
    o.`completed` = 0;
