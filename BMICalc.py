
class BMI_Calculator:

    def __init__(self):
        self.height = 0
        self.weight = 0
        pass

    def set_height(self, height):
        height = input("How tall are you (feet inches): ")

        feet = int(height[0])
        if feet < 0 or feet > 10:
            raise KeyError
        inches = int(height[2] + height[3])
        if inches < 0 or inches < 12:
            raise KeyError
        height = (feet * 12) + inches
        meters = height*.0254
        height = meters * meters
    
        return self.height

    def get_height(self):
        return self.height

    def set_weight(self, weight):
        #weight = int(input("How much do you weigh in pounds: "))
        if weight <= 0 or weight > 600:
            raise KeyError()
        else:
            self.weight = weight*.45359
            return self.weight

    def get_weight(self):
        return self.weight

    def BMI_category(self, BMI):
        if (BMI < 18.5):
            category = "Underweight"
        if (BMI >= 18.5 and BMI <= 24.9):
            category = "Normal weight"
        if (BMI >= 25 and BMI <= 29.9):
            category = "Overweight"
        if (BMI >= 30):
            category = "Obese"
        return category


    def BMICalc(welf, weight, height):
        BMI = weight/height
        return BMI