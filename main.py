
from flask import Flask, jsonify, render_template, request
from knn_model.utils import MedicalInsurance
import config

app = Flask(__name__)

@app.route('/')
def hello_flask():
    print("Welcome to Flask")
    
    return render_template("index.html")

@app.route('/pred_insurance', methods =["POST","GET"])
def get_predict_charges():
    if request.method == "GET":

        print("We are using GET method")

        data = request.form
        print("Data-->",data)

        # age = int(data["age"])
        # sex = data["sex"]
        # bmi = eval(data["bmi"])
        # children = int(data["children"])
        # smoker = data["smoker"]
        # region = data["region"]

        age = eval(request.args.get("age"))
        sex = request.args.get("sex")
        bmi = eval(request.args.get("bmi"))
        children = int(request.args.get("children"))
        smoker = request.args.get("smoker")
        region = request.args.get("region")

        print("age,sex,bmi,children,smoker,region\n",age,sex,bmi,children,smoker,region)

        mic = MedicalInsurance(age,sex,bmi,children,smoker,region)
        charges = mic.get_predicted_charges()
        # return jsonify({"Result": f"Medical insurance charges is {charges} RS only"})
        return render_template("index.html", prediction = charges)

    else:
        print("We are using POST Method")
        
        age = eval(request.form.get("age"))
        sex = request.form.get("sex")
        bmi = eval(request.form.get("bmi"))
        children = int(request.form.get("children"))
        smoker = request.form.get("smoker")
        region = request.form.get("rergion")

        print("age,sex,bmi,children,smoker,region\n",age,sex,bmi,children,smoker,region)

        mic = MedicalInsurance(age,sex,bmi,children,smoker,region)
        charges = mic.get_predicted_charges()
        # return jsonify({"Result": f"Medical insurance charges is {charges} RS only"})
        return render_template("index.html", prediction = charges)





if __name__ == "__main__":
    app.run(host = '0.0.0.0',port = config.PORT_NUMBER, debug = True)