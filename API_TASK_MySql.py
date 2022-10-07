from flask import Flask , request, jsonify
import mysql.connector as conn

'''
1 . Write a program to insert a record in sql table via api 
2.  Write a program to update a record via api 
3 . Write a program to delete a record via api 
4 . Write a program to fetch a record via api
5 . All the above questions you have to answer for mongoDB as well'''

app=Flask(__name__)
try:
#MySql connection

    mydb=conn.connect(host='localhost',user='root',password='mysql1234')
    cursor=mydb.cursor()

#table and database creation

    cursor.execute('CREATE DATABASE IF NOT EXISTS api_tasksql')
    cursor.execute('CREATE TABLE IF NOT EXISTS api_tasksql.api_table(name VARCHAR(20), number INT(10))')

#Question number 1:
    @app.route('/insert',methods=['POST'])
    def insert():
        if(request.method=='POST'):
            name=request.json['name']
            number=request.json['number']
            cursor.execute('insert into api_tasksql.api_table values (%s , %s)',(name,number))
            mydb.commit()
            return jsonify(str('successfully inserted'))

#Question number 2:
    @app.route('/update',methods=['POST'])
    def update():
        if(request.method=='POST'):
            get_name=request.json['get_name']
            cursor.execute('update api_tasksql.api_table set number=number+500 where name=(%s)',[get_name])
            mydb.commit()
            return jsonify(str('update successfully'))

# Question number 3:
    @app.route('/delete',methods=['POST'])
    def delete():
        if(request.method=='POST'):
            del_name=request.json['del_name']
            cursor.execute('delete from api_tasksql.api_table where name =(%s)',[del_name])
            mydb.commit()
            return jsonify(str('deleted successfully'))

#Question number 4:
    @app.route('/fetch',methods=['POST','GET'])
    def fetch():
        if(request.method=='POST'):
            cursor.execute('select * from api_tasksql.api_table')
            return jsonify (str(cursor.fetchall()))


except Exception as e:
    print(e)

if __name__ == '__main__':
    app.run(debug=True)
