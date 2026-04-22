**Propósito:** Asistencia en la lógica de programación y depuración.
**Herramientas:** ChatGPT, Claude, GitHub Copilot, Gemini.

#### 1. Generación de Lógica Aislada (Ej. Movimiento Enemigo)

**Contexto:** Nunca le pidas a la IA "hazme un juego". Pídele módulos específicos usando la jerga de ingeniería.

> **Prompt:** `Actúa como un Senior Python Developer. Escribe una clase 'Enemy' para Pygame que herede de 'pygame.sprite.Sprite'. El enemigo debe inicializarse en la parte superior de la pantalla (y < 0) en una coordenada X aleatoria. Debe moverse hacia abajo en el eje Y a una velocidad variable. Implementa el método update() y asegúrate de incluir self.kill() si el objeto sobrepasa el límite inferior de la pantalla (SCREEN_HEIGHT = 600) para liberar memoria.`

#### 2. Resolución de Colisiones (Hitboxes)

**Contexto:** Las colisiones suelen ser el mayor dolor de cabeza.

> **Prompt:** `Tengo dos grupos de sprites en Pygame: 'bullets' y 'enemies'. Escribe la línea de código exacta usando 'pygame.sprite.groupcollide' para detectar impactos. Quiero que AMBOS objetos se eliminen al chocar. Además, proporciona un bucle 'for' para iterar sobre las colisiones resultantes, sumar 10 puntos a una variable global 'score', e instanciar una animación de explosión en las coordenadas del enemigo destruido.`

#### 3. Depuración de Errores (Debugging)

**Contexto:** Cuando la pantalla se queda en negro o el juego se congela.

> **Prompt:** `Estoy recibiendo el error 'pygame.error: video system not initialized' al intentar cargar una imagen en mi archivo sprites.py. Las constantes de pantalla están en settings.py. ¿Cuál es el error en el orden de ejecución de mis imports y la inicialización de pygame.init() en mi archivo main.py? Explica la solución desde la perspectiva del ciclo de vida del software.`

#### 4. Implementación de "Juice" (Screen Shake)

**Contexto:** Para dar el toque profesional de pulido al final del taller.

> **Prompt:** `Quiero añadir un efecto de 'Screen Shake' (temblor de pantalla) en Pygame cuando el jugador reciba daño. Mi superficie principal se llama 'screen'. Escribe una función 'screen_shake(duration, intensity)' que desplace temporalmente el renderizado general unos cuantos píxeles de forma aleatoria durante X frames sin modificar las coordenadas reales de los sprites.`
>
