import datetime
student = {"name": ["Esther", "Njogu"], "Birthdate": datetime.date(1900,01,01), "Tel": "0733"}

print "My last name is {}".format(student.get("name")[1])
print "While my full name is {} {}".format(student.get("name")[0], student.get("name")[1])
# using print "My name is {}".format(student.get("name"))
# the following will make the ouput come out as 
#My name is ['Esther', 'Njogu']

print "My cell number is {}".format(student.get("Tel"))
print "I was born on {} ".format(student.get("Birthdate")) + "making me {} ".format(datetime.date.today().year-student.get("Birthdate").year) + " years old"