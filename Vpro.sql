CREATE VIEW tv as 
select DATE(time) , count(*) as
tv from log 
GROUP by date(time);


CREATE VIEW eview as 
select DATE(time),count(*) as 
eview from log 
where status like '404 NOT FOUND'
GROUP by date(time) ; 



