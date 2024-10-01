student = { 
    "first name" : "Ola", 
    "last name" : "Nordmann",
    "favourite course" : "Programmering 1" 
} 

print(f"{student["first name"]} {student["last name"]}")

student["favourite course"] = "ITF10219 Programmering 1"

student["alder"] = 23

print(student.items())