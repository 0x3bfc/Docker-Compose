# Flask MySQL application

Test flask services using the following RestFul API 

Create Database
----------------

	http://localhost:8081/createdb?hostname=mysqlhost

Create and Initiate Users Table
--------------------------------

	http://localhost:8081/createtbl

Insert New User:
----------------

	http://localhost:8081/insert?username=ahmed&email=ahmed@gmail.com&phone=02-9454402333&fax=+4438383

Select all Users
----------------

	http://localhost:8081/users

Select specific user
--------------------

	http://localhost:8081/user?username=ahmed
