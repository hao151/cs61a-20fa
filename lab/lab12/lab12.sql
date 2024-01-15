.read data.sql


CREATE TABLE bluedog AS
  SELECT color, pet from students where color = 'blue' and pet = 'dog';

CREATE TABLE bluedog_songs AS
  SELECT color, pet, song from students where color = 'blue' and pet = 'dog';


CREATE TABLE smallest_int AS
  SELECT time, smallest from students where smallest > 2 order by smallest LIMIT 20;


CREATE TABLE matchmaker AS
  SELECT table1.pet, table1.song, table1.color, table2.color from students as table1, students as table2 where 
  table1.time < table2.time and table1.pet = table2.pet and table1.song = table2.song;


CREATE TABLE sevens AS
select stu.seven from
  (select students.time, students.seven, students.number from students where students.number = 7) as stu,
  (SELECT numbers.'7', numbers.time from numbers where numbers.'7' = 'True') as num 
  where stu.time = num.time;

