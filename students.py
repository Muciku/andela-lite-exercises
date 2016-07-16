student = {"name": ["Esther", "Njogu"], "DOB": 1900, "Tel": "0738937339"}

print "My last name is {}".format(student.get("name")[1])
print "My name is {}".format(student.get("name"))
print "The cell number is {}".format(student.get("Tel"))
print "I was born in the year " + "making me" + " years old"