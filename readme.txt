• 使用postman 測試
GET http://localhost:5000/user?id=1 
GET http://localhost:5000/user?id=2



REST API Query Parameter GET Request using Python Flask and PostgreSQL Database

Create table

CREATE TABLE useraccount (
	id serial PRIMARY KEY,
	username VARCHAR ( 100 ) NOT NULL,
	password VARCHAR ( 100 ) NOT NULL
);

Insert data

INSERT INTO useraccount (username, password) VALUES ('tutorial101', 'pbkdf2:sha256:150000$KxxiGerN$4c37a656baa0034035a6be2cd698b5da8b036ae63eef3ab0b08b9c18b9765648');

Testing Rest API

REST API Testing is open-source web automation testing technique that is used for testing RESTful APIs for web applications. The purpose of rest api testing is to record the response of rest api by sending various HTTP/S requests to check if rest api is working fine or not. Rest api testing is done by GET, POST, PUT and DELETE methods.

Rest stands for Representational State Transfer. It is an architectural style and an approach for communication used in the development of Web Services. REST has become a logical choice for building APIs. It enables users to connect and interact with cloud services efficiently.

An API or Application Programming Interface is a set of programming instructions for accessing a web-based software application.

API is a set of commands used by an individual program to communicate with one another directly and use each other's functions to get information.

Install the Advanced Rest Client
1. Go to Google Chrome's Web Store
2. Search for "Advanced Rest Client" https://chrome.google.com/webstore/detail/advanced-rest-client/hgmloofddffdnphfgcellkdfbfbjeloo and Install the extension

install psycopg2 https://pypi.org/project/psycopg2/
Psycopg is the most popular PostgreSQL database adapter for the Python programming language.
(venv) PS C:\flaskmyproject> pip install psycopg2