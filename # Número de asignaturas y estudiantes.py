# Número de asignaturas y estudiantes
num_asignaturas = 3
num_estudiantes = 5

# Diccionario para almacenar las notas por asignatura
notas_por_asignatura = {f'Asignatura {i}': [] for i in range(1, num_asignaturas + 1)}

# Bucle externo para las asignaturas
for asignatura in range(1, num_asignaturas + 1):
    print(f"Asignatura {asignatura}:")

    # Bucle para registrar notas de estudiantes
    estudiante = 1
    while estudiante <= num_estudiantes:
        nota = int(input(f"Nota del estudiante {estudiante}: "))

        # Validación del rango de notas
        if 10 <= nota <= 50:
            notas_por_asignatura[f'Asignatura {asignatura}'].append(nota)
            estudiante += 1
        else:
            print("La nota debe estar entre 10 y 50.")

    print("\n")

# Calcular el promedio por asignatura y el promedio del grupo
promedio_asignatura = {}
promedio_grupo = 0

for asignatura, notas in notas_por_asignatura.items():
    promedio = sum(notas) / len(notas)
    promedio_asignatura[asignatura] = promedio
    promedio_grupo += promedio

# Mostrar promedio por asignatura y promedio del grupo
print("Promedio por asignatura:")
for asignatura, promedio in promedio_asignatura.items():
    print(f"{asignatura}: {promedio:.2f}")

promedio_grupo /= num_asignaturas
print(f"Promedio del grupo: {promedio_grupo:.2f}")

print("Fin del programa.")
