# Taller: Creación de Videojuegos Retro con IA 🕹️🤖

**Semana de Ingeniería en Sistemas Computacionales - Tecnológico de Pachuca**

Este repositorio contiene el código base y la estructura para el taller práctico de desarrollo de videojuegos estilo **"Space Shooter"** utilizando Python, Pygame e Inteligencia Artificial Generativa.

---

## 🎯 Objetivo

Desarrollar un prototipo funcional de videojuego retro en aproximadamente 2 horas, utilizando IA para:

* Generación de assets (sprites, sonido, música)
* Asistencia en la lógica de programación
* Optimización del código

---

## 🧱 Estructura del Proyecto

```
retro-game-ai-workshop/
├── .gitignore
├── README.md
├── requirements.txt
├── docs/
├── src/
├── assets/
└── ai-prompts/
```

---

## 🚀 Requisitos Previos

* Python 3.10 o superior
* Editor de código (recomendado: Visual Studio Code)
* Terminal o línea de comandos

---

## ⚙️ Instalación

### 1. Clonar el repositorio

```bash
git clone <URL_DEL_REPOSITORIO>
cd retro-game-ai-workshop
```

---

### 2. Crear entorno virtual

```bash
python -m venv venv
```

---

### 3. Activar entorno virtual

**Windows:**

```bash
venv\Scripts\activate
```

**Mac/Linux:**

```bash
source venv/bin/activate
```

---

### 4. Instalar dependencias

```bash
pip install -r requirements.txt
```

> Si el archivo `requirements.txt` aún no existe:

```bash
pip install pygame
```

---

## ▶️ Ejecución del Proyecto

⚠️ IMPORTANTE: El proyecto usa estructura con carpeta `src`

Ejecuta desde la raíz del proyecto:

```bash
python -m src.main
```

---

## 🧠 Uso de Inteligencia Artificial

Durante el taller se utilizará IA para:

* Generar sprites (personajes, enemigos)
* Crear efectos de sonido
* Generar música estilo retro
* Apoyar en la escritura de código

Los prompts utilizados se documentan en:

```
ai-prompts/
```

---

## 🎮 Tecnologías utilizadas

* Python
* Pygame
* Herramientas de IA generativa

---

## 🧑‍🏫 Notas del Taller

* No se requiere experiencia previa en videojuegos
* Se recomienda seguir las instrucciones paso a paso
* El enfoque es práctico y orientado a resultados

---

## ⚠️ Problemas comunes

### Error: módulo no encontrado

Asegúrate de ejecutar:

```bash
python -m src.main
```

---

### Error: pygame no instalado

```bash
pip install pygame
```

---

### Error: entorno virtual no activado

Verifica que aparezca `(venv)` en la terminal.

---

## 📄 Licencia

Uso educativo.
