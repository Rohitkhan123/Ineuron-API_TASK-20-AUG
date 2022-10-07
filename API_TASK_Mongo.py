import pymongo
from flask import Flask,request,jsonify

app=Flask(__name__)

#MongoDb connection
try:
    client= pymongo.MongoClient('mongodb+srv://mongodb:Rohit123@cluster0.4jhuusd.mongodb.net/?retryWrites=true&w=majority')
    db=client.test
    database=client['Api_Task']
    collection=database['Api_table']
# TASK Number 1:
    @app.route('/insert/mongo',methods=['POST'])
    def insert():
        if (request.method=='POST'):
            name=request.json['name']
            number=request.json['number']
            collection.insert_one({name:number})
            return jsonify(str('inserted'))

# TASK
    @app.route("/testfun")
    def test():
        get_name = request.args.get("get_name")
        mobile_number = request.args.get("mobile")
        mail_id = request.args.get('mail_id')

        return jsonify("this is my first function for get {} {} {}".format(get_name, mobile_number, mail_id))

except Exception as e:
    print(e)

if __name__=='__main__':
    app.run(debug=True)