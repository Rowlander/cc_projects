class Patient:
    def __init__(self, name, age, sex, bmi, num_of_children, smoker):
        try:
            if not type(name) == str:
                raise ValueError
            else:
                self.name = name
        except ValueError:
            print("Name must be string")
        try:
            if not type(age) == int:
                raise TypeError
            else:
                self.age = age
            if not type(sex) == int:
                raise TypeError
            else:
                self.sex = sex
            if not type(bmi/1) == float:
                raise TypeError
            else:
                self.bmi = bmi
            if not type(num_of_children) == int:
                raise TypeError
            else:
                self.num_of_children = num_of_children
            if not type(smoker) == int:
                raise TypeError
            else:
                self.smoker = smoker
        except TypeError:
            print("All but the name input must be numerical")
    # add more parameters here
    def estimated_insurance_cost(self):
        try:
          estimated_cost = (250 * self.age) - (128 * self.sex) + (370 * self.bmi) + (425 * self.num_of_children) + (24000 * self.smoker) - 12500
        except TypeError:
          print("Update Input values must be numerical")
        print(f"{self.name}'s estimated insurance cost is {estimated_cost} dollars.")

    def update_age(self, new_age):
        self.age = new_age
        print(f"{self.name} is now {self.age} years old.")
        self.estimated_insurance_cost()

    def update_num_children(self, new_num):
        self.num_of_children = new_num
        if self.num_of_children > 1:
            print(f"{self.name} now has {self.num_of_children} children.")
        else:
            print(f"{self.name} now has {self.num_of_children} child.")
        self.estimated_insurance_cost()

    def update_bmi(self, new_bmi):
        self.bmi = new_bmi
        print(f"{self.name} new BMI is {self.bmi}. ")
        self.estimated_insurance_cost()

    def update_smoker(self, new_smoker_status):
        self.smoker = new_smoker_status
        if self.smoker == 0:
            print(f"{self.name} stopped smoking")
        else:
            print(f"{self.name} started smoking")
        self.estimated_insurance_cost()

    def patient_profile(self):
        patient_information = {}
        patient_information["Name"] = self.name
        patient_information["Age"] = self.age
        patient_information["Sex"] = self.sex
        patient_information["BMI"] = self.bmi
        patient_information["Number of Children"] = self.num_of_children
        patient_information["Smoker"] = self.smoker
        return patient_information

patient1 = Patient("Joris Mook", 32, 1, 22.2, 2, 1)
patient1.estimated_insurance_cost()
patient1.update_age(33)
patient1.update_num_children(3)
patient1.update_bmi(25.6)
patient1.update_smoker(0)
print(patient1.patient_profile())
