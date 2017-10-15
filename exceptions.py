student = {
    "Name": "Shantanu",
    "Age": 21,
    "feedback": None
}

student["lastName"] = "Kamath"


try:
    lastName = student["lastName"]
    new_var = 3 + student["lastName"]
except KeyError:
    print("Error finding last name")
except TypeError as error:
    print("Cant add these two together", error)
except Exception:
    print("Unknown exception")

print("This code executes")