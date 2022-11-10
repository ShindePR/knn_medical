import pickle
import json
import numpy as np
import pandas as pd
import config


class MedicalInsurance():
    def __init__(self,age,sex,bmi,children,smoker,region):
        self.age = age
        self.sex = sex
        self.bmi = bmi
        self.children = children
        self.smoker = smoker
        self.region = "region_" + region


    def load_file(self):
        with open (config.PICKLE_FILE_PATH,'rb') as f:
            self.mic_model = pickle.load(f)

        with open (config.SCALAR_FILE_PATH,'rb') as f:
            self.scalar = pickle.load(f)

        with open (config.JSON_FILE_PATH,'r') as f:
            self.medical_data = json.load(f)
    def get_predicted_charges(self):
        self.load_file()  #calling method

        region_index = self.medical_data['columns'].index(self.region)
        array = np.zeros(len(self.medical_data["columns"]))
        array[0] = self.age
        array[1] = self.medical_data['sex'][self.sex]
        array[2] = self.bmi
        array[3] = self.children
        array[4] = self.medical_data['smoker'][self.smoker]
        array[region_index] = 1

        print("Array-->",array)
        test_array = self.scalar.transform([array])
        print("testa _array",test_array)

        predicted_charge = self.mic_model.predict(test_array)[0]
        return np.around(predicted_charge,2)

if __name__ == "__main__":
    
    age = 60
    sex = 'male'
    bmi = 25.5
    children = 2
    smoker = 'no'
    region = 'southwest'

    mic = MedicalInsurance(age,sex,bmi,children,smoker,region)
    charges = mic.get_predicted_charges()
    print(f"Medical insurance charges is {charges} RS only")