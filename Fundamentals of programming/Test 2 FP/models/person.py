class Person:
    def __init__(self, id, immunization, status):
        self.id = id
        self.immunization = immunization
        self.status = status
        self.days = -1 if self.status == "healthy" else 0
 
    def __str__(self):
        if self.status == "ill":
            return "{} -> Immunization: {}; Status: {}; Days since getting ill: {}".format(self.id, self.immunization, self.status, self.days)
        else:
            return "{} -> Immunization: {}; Status: {};".format(self.id, self.immunization, self.status)