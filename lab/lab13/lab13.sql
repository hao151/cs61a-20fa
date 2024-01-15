.read data.sql


CREATE TABLE average_prices AS
  SELECT category, avg(MSRP) as average_price from products group by category;


CREATE TABLE lowest_prices AS
  SELECT store, item, min(price) from inventory group by item;


CREATE TABLE shopping_list AS
  select name, store from lowest_prices,
  (SELECT name, min(MSRP / rating) from products group by category) as lowest_price
  where item = name;


CREATE TABLE total_bandwidth AS
  SELECT sum (Mbs) from shopping_list, stores where shopping_list.store = stores.store;

