import numpy as np
import matplotlib.pyplot as plt

# Configuración
N = 200  # cantidad de valores
np.random.seed(42)  # para reproducibilidad

# Archivo de registro
with open("simulacion.txt", "w", encoding="utf-8") as f:
    f.write("Simulación de distribución triangular\n")
    f.write("f(x) = x-1 si 1≤x≤2, 3-x si 2<x≤3\n\n")
    f.write(f"Total de valores simulados: {N}\n\n")
    f.write("Iteración | u | Fórmula usada | Resultado x\n")
    f.write("----------------------------------------------\n")

# Lista de resultados
resultados = []

# Generar valores
for i in range(1, N + 1):
    u = np.random.rand()  # número uniforme entre 0 y 1
    
    # Determinar la fórmula según el rango de u
    if u <= 0.5:
        x = 1 + np.sqrt(2 * u)
        formula = "x = 1 + sqrt(2u)"
    else:
        x = 3 - np.sqrt(2 * (1 - u))
        formula = "x = 3 - sqrt(2(1 - u))"
    
    resultados.append(x)

    # Mensaje de iteración
    mensaje = f"{i:03d} | u={u:.5f} | {formula} | x={x:.5f}"
    print(mensaje)
    with open("simulacion.txt", "a", encoding="utf-8") as f:
        f.write(mensaje + "\n")

# Calcular estadísticas
media = np.mean(resultados)
varianza = np.var(resultados, ddof=1)

print("\n--- Estadísticas ---")
print(f"Media simulada: {media:.4f}")
print(f"Varianza simulada: {varianza:.4f}")

with open("simulacion.txt", "a", encoding="utf-8") as f:
    f.write("\n--- Estadísticas ---\n")
    f.write(f"Media simulada: {media:.4f}\n")
    f.write(f"Varianza simulada: {varianza:.4f}\n")

# Graficar histograma
# Graficar histograma con detalles extra
plt.figure(figsize=(10, 6))

plt.hist(
    resultados,
    bins=50,
    density=True,
    edgecolor='black',
    alpha=0.75,
    linewidth=0.6
)

plt.title("Histograma de 200 valores simulados", fontsize=14)
plt.xlabel("x", fontsize=12)
plt.ylabel("Frecuencia relativa", fontsize=12)

# Más divisiones en el eje X
plt.xticks(np.linspace(min(resultados), max(resultados), 12))

# Más divisiones en el eje Y
plt.yticks(np.linspace(0, plt.gca().get_ylim()[1], 20))

# Grid más detallado
plt.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.4)

# Estilo de ticks
plt.tick_params(axis='both', direction='inout', length=6, width=1)

plt.tight_layout()
plt.savefig("histograma.png", dpi=300)
plt.show()
