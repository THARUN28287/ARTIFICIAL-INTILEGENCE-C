
def decision_tree(study_hours, attendance):
    if study_hours <= 3:
        return "Fail"
    elif attendance >= 80:
        return "Pass"
    else:
        return "Fail"

study_hours = 5
attendance = 85

prediction = decision_tree(study_hours, attendance)

print("Study Hours:", study_hours)
print("Attendance:", attendance, "%")
print("Prediction:", prediction)
