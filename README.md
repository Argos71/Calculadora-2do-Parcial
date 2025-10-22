# 🖥️ Calculadora GUI de Simulación y Distribuciones

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&style=for-the-badge)
![Tkinter](https://img.shields.io/badge/Tkinter-GUI-orange?style=for-the-badge)
![NumPy](https://img.shields.io/badge/NumPy-Numerics-brightgreen?style=for-the-badge)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Plotting-red?style=for-the-badge)

---

Esta aplicación es un **software de escritorio en Python** que combina **generación de distribuciones aleatorias, simulación de autómatas celulares y modelado de propagación de COVID-19**.  
Está diseñada para facilitar **experimentación educativa y análisis de fenómenos dinámicos**, ofreciendo un control completo sobre parámetros, visualización y exportación de resultados.

---

## ⚙️ Funcionamiento General del Sistema

El sistema está organizado en **módulos independientes**, cada uno con su propia interfaz y panel de configuración, pero integrados en una ventana principal.  

### Arquitectura del Sistema

1. **Interfaz Gráfica (GUI)**
   - Construida con **Tkinter**, organiza los módulos en pestañas o secciones.
   - Cada módulo tiene:
     - Entradas de parámetros
     - Botones de acción (`Generar`, `Simular`, `Exportar`)
     - Panel de visualización gráfica
     - Indicaciones sobre cómo configurar cada parámetro

2. **Módulos Numéricos**
   - **Generación de distribuciones**:
     - Funciona mediante **NumPy** para distribución aleatoria avanzada o un **LCG propio** para aprendizaje de generadores lineales congruentes.
     - Permite modificar semilla, tamaño de muestra y parámetros específicos de cada distribución.
   - **Autómatas celulares**:
     - 1D y 2D (Juego de la Vida)
     - Reglas de evolución configurables (`regla Wolfram` para 1D, `B/S` para 2D)
   - **Simulación epidemiológica**:
     - Modelo basado en celda con estados discretos (`susceptible`, `infectado`, `recuperado`, `fallecido`)
     - Evolución paso a paso según parámetros probabilísticos

3. **Visualización y Resultados**
   - Uso de **Matplotlib** para graficar:
     - Histogramas de variables aleatorias
     - Evolución temporal de autómatas
     - Mapas de propagación de COVID-19
   - Paneles de visualización en tiempo real permiten **observar cambios dinámicos**
   - Exportación de datos a **CSV o Excel** para análisis externo

4. **Control y Gestión de Datos**
   - Validación de entradas de usuario
   - Guardado automático de parámetros de simulación
   - Posibilidad de **reiniciar simulaciones** sin reiniciar la aplicación

---

## 🔹 Detalle por Módulo

### 1️⃣ Generador de Distribuciones Aleatorias

- **Tipos de distribución:**
  - **Continuas:** Normal, Uniforme, Exponencial, Weibull, Gamma, Erlang
  - **Discretas:** Bernoulli, Binomial, Poisson, Uniforme discreta
- **Funcionamiento:**
  1. El usuario selecciona el tipo de distribución y el generador (NumPy o LCG)
  2. Ingresa parámetros específicos (media, desviación, probabilidad, tamaño de muestra, etc.)
  3. Presiona **Generar** → el sistema calcula la muestra y la grafica
  4. Opcionalmente, exporta los datos

---

### 2️⃣ Autómata Celular 1D

- **Configuración:**
  - Tamaño del autómata (número de celdas)
  - Regla de Wolfram (0-255)
  - Estado inicial (aleatorio o personalizado)
- **Evolución:**
  - Cada celda se actualiza según su vecindario y la regla seleccionada
  - Visualización paso a paso en una **matriz de estados**
- **Exportación:**
  - CSV con historial de estados por paso

---

### 3️⃣ Juego de la Vida 2D

- **Configuración:**
  - Dimensiones del grid (N×N)
  - Reglas B/S (Birth/Survive) personalizadas
  - Estado inicial aleatorio (~35% celdas vivas)
- **Evolución:**
  - Celdas vivas/muertas actualizadas según vecindario
  - Posibilidad de ejecutar paso a paso o en modo automático
- **Visualización:**
  - Tablero actualizado dinámicamente
  - Colores diferenciados para vivos y muertos
- **Exportación:**
  - PNG del tablero actual o CSV de estados

---

### 4️⃣ Simulación COVID-19 2D

- **Estados de las celdas:**
  - Vacío, Susceptible, Infectado, Recuperado, Fallecido
- **Parámetros de configuración:**
  - Tamaño del grid
  - Densidad de población
  - Probabilidad de contagio y muerte
  - Días para recuperación
  - Pasos de simulación
- **Proceso de simulación:**
  1. El sistema inicializa la población según los parámetros
  2. Cada paso:
     - Infectados pueden contagiar vecinos según probabilidad
     - Se actualiza estado de recuperación o muerte
  3. Se actualiza la visualización y los gráficos
- **Resultados:**
  - Gráficas de evolución de infectados, recuperados y fallecidos
  - Exportación de datos para análisis externo

---

## 🛠️ Instalación y Ejecución

1. Clonar repositorio:

```bash
https://github.com/Argos71/Calculadora-2do-Parcial.git
cd calculadora-gui-simulacion
```

2. Instalar dependencias:

```bash
pip install numpy pandas matplotlib pillow openpyxl
```

1. Ejecutar la aplicación:

```bash
python CalculadoraSegundoParcial.py

```
