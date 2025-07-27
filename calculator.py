class Calculator:
    def __init__(self):
        self.equation = ""

    def add(self, val):
        if val == "AC":
            self.equation = ""
        elif val == "=":
            try:
                # Prevent unsafe evaluation (optional)
                if self.equation.strip() != "":
                    self.equation = str(eval(self.equation))
            except:
                self.equation = "Error"
        else:
            # Append number or operator
            self.equation += val

    def get_equation(self):
        return self.equation
