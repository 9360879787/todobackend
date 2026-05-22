from flask import Flask
import mysql.connector

def connection():
    return mysql.connector.connect(
        host =' sridharmysql.mysql.database.azure.com',
        port = 3306,
        user = 'sridharAdmin',
        password = '##Ssujitha2007',
        database = 'todolist'
)