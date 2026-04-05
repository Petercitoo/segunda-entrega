def processing_students(students):
    for student in students.copy():
        elim = False
        for key, value in student.items():
    #Si el nombre no cumple condicion, se elimina el estudiante.       
            if key ==  "name":
                if value is None or value.strip() == "":
                    elim = True
    #Si la nota no cumple condicion, se elimina el estudiante.        
            elif key == "grade":
                if value is None or value.strip() == "" or not value.isnumeric():
                    elim = True
        if elim:
            students.remove(student)
        else:
    #Actualiza y formatea el nombre y el estado si el estudiante es valido.   
            student.update({"name": student["name"].title().strip(), "status": student["status"].title().strip()})
    #Ordena la lista de estudiantes en base a la nota.        
    students.sort(key=lambda x: int(x["grade"]), reverse=True)
    vistos = set()
    resultado = []
    #Procesa nuevamente los estudiantes, los agrega a vistos para evitar repetidos con nota menor
    #Y luego los agrega a resultado
    for student in students:
        if student["name"] not in vistos:
            vistos.add(student["name"])
            resultado.append(student)
    return resultado