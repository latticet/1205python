-- A. 查询卖的最贵的商品的名称
SELECT goods_name FROM ecs_goods WHERE shop_price=
(SELECT MAX(shop_price) FROM ecs_goods);


-- B. 查询商品品牌为”仓品”的 所有商品名称和商品价格
SELECT goods_name, shop_price FROM ecs_goods WHERE
brand_id = 
(SELECT brand_id FROM ecs_brand WHERE brand_name = '仓品');


-- C. 查询商品品牌为”仓品”的 所有商品名称和商品价格 按照价格降序排列
SELECT goods_name, shop_price FROM ecs_goods WHERE
brand_id = 
(SELECT brand_id FROM ecs_brand WHERE brand_name = '仓品')
ORDER BY shop_price DESC;

-- D. 查询每个商品品牌的商品数量
-- 以记录数作为商品数量统计
SELECT brand_id, count(*) FROM ecs_goods GROUP BY brand_id;

-- 以goods_number数作为商品数量统计
SELECT brand_id, SUM(goods_number) FROM ecs_goods 
GROUP BY brand_id;

-- 和ecs_brand表做连接查询
SELECT b.brand_name, count(g.goods_id) 
FROM ecs_goods g, ecs_brand b 
WHERE g.brand_id = b.brand_id
GROUP BY g.brand_id;

-- E. 查询商品品牌对应的商品数量大于5的商品品牌名称
SELECT b.brand_name, count(g.goods_id) 
FROM ecs_goods g, ecs_brand b 
WHERE g.brand_id = b.brand_id
GROUP BY g.brand_id HAVING count(g.goods_id) > 5;
