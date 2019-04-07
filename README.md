#First Project In Full Stack web Developer nanodegree("log analysis")
in this project , we create apython code to run queries to answer this questions

##Questions
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?  
###Requirements
-Python 2.7
-Postgresql  
-psycopg2
#### views_code:

CREATE VIEW tv as 
select DATE(time) , count(*) as
tv from log 
GROUP by date(time);


CREATE VIEW eview as 
select DATE(time),count(*) as 
eview from log 
where status like '404 NOT FOUND'
GROUP by date(time) ; 

#####How to run:
-create two View called eview  and tv 
-craete new python file in IDE which use to write python code
-run VM
-create database newdata.sql in VM using command >>$ 'psql -d news -f newsdata.sql'
-run command >>$'psql -d news -f Vpro.sql' in VM to create view
-craete python file with query to excute 
-run python code using VM using command >> $'python ngwa.py'
-done





