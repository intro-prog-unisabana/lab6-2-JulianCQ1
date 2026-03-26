def student_averages(estudiantes):
    promedios = {}
    for estudiante, notas in estudiantes.items():
        average = sum(notas.values()) / len(notas)
        promedios[estudiante] = average
    return promedios
def assignment_averages(estudiantes):
    total = {}
    cuenta = {}
    for asignatura in estudiantes.values():
        for materia, nota in asignatura.items():
            if asignatura not in total:
                total[asignatura] = 0
                cuenta[asignatura] = 0
            total[materia] = total.get(materia, 0) + nota
            cuenta[materia] = cuenta.get(materia, 0) + 1
    resultado = {}
    for asignatura in total:
        resultado[asignatura] = total[asignatura] / cuenta[asignatura]
        return resultado
   