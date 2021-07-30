import spacy
from flask import Flask,request,jsonify
from flask_restful import Resource,Api


#Creating a app and api of Flask

app=Flask(__name__)
api=Api(app)




class Greet(Resource): 
    def get(self): 
        returnjson={ 'status':200,
        'msg': 'Use /check to check plagirism between 2 text samples' }

        return jsonify(returnjson)
#Check Plagirism class

class CheckPlagirism(Resource):
    def get(self): 
        returnjson={ 'status':200,
        'msg': 'Pass username password and texts as a post method to api to check the similarity' }

        return jsonify(returnjson)
    def post(self):
        #get json data passed through post request
        passed_data=request.get_json()

        #Extracting data from the posted data
        username=passed_data['username']
        password=passed_data['password']
        
        text1=passed_data['text1']   #this is ideal text 
        text2=passed_data['text2']   #this is the text to be checked 

        if username == 'admin'  and password== 'pass':

                #Creating natural language processors using spacy
                    
                naturalLangProcessor = spacy.load("en_core_web_sm")
                
                text1=naturalLangProcessor(text1)
                
                text2=naturalLangProcessor(text2)

                similarities = text1.similarity(text2)

                retJson={'status': 200,
                'msg':'Similarity found in the texts is {} %'.format(similarities*100)
                }
                return jsonify(retJson)
        else:
            retJson={'status':401,'msg': 'Check credentials or make sure you are registered ... try again '}
            return jsonify(retJson) 

api.add_resource(Greet,'/')
api.add_resource(CheckPlagirism,'/check')

app.run(debug=True)