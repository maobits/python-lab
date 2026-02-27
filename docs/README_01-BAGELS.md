# 🧠 BAGELS

## Proyecto 01 – Arquitectura Mental Programada en Python

---

## 📌 Descripción General

**Bagels** es un juego de lógica deductiva desarrollado en Python donde el usuario debe adivinar un número secreto de _N dígitos sin repetir_, utilizando pistas estructuradas:

- **Pico** → Dígito correcto en posición incorrecta
- **Fermi** → Dígito correcto en posición correcta
- **Bagels** → Ningún dígito es correcto

Este proyecto forma parte del modelo educativo de **Arquitectura Mental y Tecnológica para Negocios** del Instituto Maobits.

---

## 🎯 Objetivo del Proyecto

Este proyecto tiene como propósito:

- Aplicar pensamiento lógico estructurado
- Comprender ciclos y control de flujo
- Implementar validación de datos
- Diseñar funciones modulares
- Desarrollar un motor básico de inferencia lógica
- Entender arquitectura de control de estado

---

## 🏗️ Arquitectura del Sistema

El sistema está dividido en capas claras:

1. **Configuración del sistema**
   - Constantes: `NUM_DIGITOS`, `MAX_INTENTOS`

2. **Controlador principal**
   - `main()`

3. **Generador de número secreto**
   - `obtener_numero_secreto()`

4. **Motor de inferencia**
   - `obtener_pistas()`

5. **Validación de entrada**
   - Control de longitud y tipo de dato

6. **Gestión de intentos**
   - Control de recursos limitados

---

## 📂 Estructura del Proyecto

```bash
bagels/
│
├── bagels.py
├── README.md
├── .venv/
└── docs/ (futuro)
```

Este proyecto está diseñado para crecer dentro de un repositorio estructurado con múltiples proyectos prácticos.

---

## ⚙️ Configuración del Entorno

### 1️⃣ Crear entorno virtual

```bash
python3 -m venv .venv
```

### 2️⃣ Activar entorno

```bash
source .venv/bin/activate
```

### 3️⃣ Ejecutar proyecto

```bash
python bagels.py
```

---

## 🔧 Configuración del Juego

Puedes modificar los parámetros del sistema:

```python
NUM_DIGITOS = 3
MAX_INTENTOS = 10
```

Ejemplos:

- Cambiar a 4 dígitos:

```python
NUM_DIGITOS = 4
```

- Aumentar intentos:

```python
MAX_INTENTOS = 15
```

---

## 🧠 Conceptos Técnicos Aplicados

- Ciclos `while`
- Condicionales `if / elif / else`
- Validación con `isdecimal()`
- Listas y manipulación de strings
- `random.shuffle()`
- Modularidad
- Separación de responsabilidades
- Control de flujo y estados

---

## 📊 Modelo de Inferencia Lógica

Ejemplo:

Número secreto: `429`
Intento: `243`

Resultado:

```
Pico Pico
```

Proceso:

- 2 está en el número pero mal posicionado
- 4 está en el número pero mal posicionado
- 3 no está presente

---

## 🏛️ Marco Académico

Este proyecto se utiliza como ejercicio base dentro del modelo:

**Arquitectura Mental y Tecnológica para Negocios**

Permite introducir conceptos de:

- Modelamiento lógico
- Sistemas determinísticos
- Control de decisiones
- Pensamiento estructurado

---

## 👤 Autor – Instituto Maobits

**Mauricio Chara Hurtado**
Empresario del sector de las ciencias de la computación
Fundador del Instituto Maobits

Integrando desarrollo de software, producción audiovisual y marketing digital
para la transformación empresarial y educativa.

Más de 10 años de experiencia en desarrollo de soluciones tecnológicas.
Liderazgo Estratégico & Visionario.
Experiencia Técnica & Multidisciplinar.

---

## 📚 Créditos de Obra Base

Basado en el proyecto “Bagels”
del libro **“The Big Book of Small Python Projects”**
Autor: Al Sweigart
Disponible en:
[https://inventwithpython.com/bigbookpython/](https://inventwithpython.com/bigbookpython/)

Licencia: Creative Commons

---

## 📌 Próximos Proyectos (Roadmap)

Este es el Proyecto 01.
Próximamente:

- Proyecto 02 – Búsqueda Binaria
- Proyecto 03 – Simulador de Sistema de Inventario
- Proyecto 04 – Motor de Decisiones Empresariales
- Proyecto 05 – Arquitectura de Datos en Python

---

## 🧩 Licencia del Proyecto

Este repositorio se distribuye bajo fines educativos dentro del modelo Instituto Maobits.

El proyecto base respeta la licencia Creative Commons del autor original.

---

## 🚀 Filosofía del Repositorio

Este repositorio no solo contiene código.

Contiene:

- Arquitectura mental aplicada
- Modelos estructurados
- Pensamiento lógico empresarial
- Fundamentos sólidos para proyectos más complejos

---

# 🔥 Estado del Proyecto

✔ Funcional
✔ Modular
✔ Escalable
✔ Documentado
✔ Listo para extender
