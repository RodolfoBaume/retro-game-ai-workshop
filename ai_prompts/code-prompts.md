**Propósito:** Asistencia en la lógica de programación y depuración.
**Herramientas:** ChatGPT, Claude, GitHub Copilot, Gemini.

# 🚀 Guía de Desarrollo: Bit-AI Shooter (Paso a Paso)

**Tecnológico de Pachuca - Ingeniería en Sistemas Computacionales**

Para construir el juego en menos de 2 horas, seguiremos un flujo de trabajo estructurado. Copia y pega estos *prompts* en las herramientas de IA correspondientes.

---

## FASE 1: Dirección de Arte (Generación de Assets Visuales)

**Herramientas recomendadas:** Bing Image Creator (DALL-E 3) o Leonardo.ai.
*Instrucción:* Descarga cada imagen generada. Usa `remove.bg` para las que necesiten transparencia y luego reduce su tamaño a 64x64 píxeles (excepto los fondos).

**1. Nave del Jugador**

> `Single 2D pixel art spaceship sprite, top-down perspective, 8-bit arcade style. Symmetrical design, neon cyan and purple color palette. Completely solid black background. No shadows, crisp edges, isolated object.`

* 💾 *Guardar como:* `assets/images/player.png` (Quitar fondo negro).

**2. Enemigos (Alien/Nave hostil)**

> `A set of three distinct alien insect spaceships, 2D pixel art, top-down view, 8-bit retro arcade aesthetic. Vibrant red and toxic green colors. Flat solid black background, highly pixelated, symmetrical.`

* 💾 *Guardar como:* `assets/images/enemy.png` (Recortar uno y quitar fondo negro).

**3. Fondo Lejano (Capa 1: Lento)**

> `Seamless scrolling background, deep space full of tiny white distant stars, completely solid black background, 8-bit pixel art, low detail.`

* 💾 *Guardar como:* `assets/images/estrellas.png` (NO quitar el fondo).

**4. Fondo Frontal (Capa 2: Rápido - Efecto Parallax)**

> `Seamless scrolling overlay of a colorful space nebula and a few scattered small planets, solid black background, 8-bit pixel art.`

* 💾 *Guardar como:* `assets/images/nebulosa.png` (Quitar fondo negro obligatorio).

---

## FASE 2: Diseño Sonoro

**Herramientas recomendadas:** Suno AI (Música) y Bfxr (Efectos).

**5. Música de Fondo (Suno AI)**

> `Upbeat 8-bit chiptune track, 140 BPM, arpeggiated square waves, arcade space shooter level 1 theme, retro gaming synthesizer, driving bassline, no vocals, instrumental loop.`

* 💾 *Guardar como:* `assets/sounds/bgm.mp3`

**6. Efectos de Sonido (Bfxr.net)**

* *No requiere prompt.* Ingresa a la página, presiona los botones `Laser/Shoot` y `Explosion` hasta que te guste un sonido.
* 💾 *Guardar como:* `assets/sounds/laser.wav` y `assets/sounds/explosion.wav`

---

## FASE 3: Arquitectura Base (El Núcleo del Juego)

**Herramientas recomendadas:** ChatGPT, Claude, Gemini.
*Instrucción:* Abre tu editor de código, crea un archivo `main.py` y usa este prompt para generar la estructura inicial.

**7. El Prompt Estructural (El Esqueleto)**

> `Actúa como un programador experto en Python. Genera el código completo en Pygame para un shooter espacial vertical. La pantalla debe ser de 800x600. Incluye una clase para el Jugador que se mueva con las flechas, una clase para los Enemigos que caigan desde arriba, y una clase para los Disparos. Usa rectángulos de colisión (Hitboxes). No uses imágenes por ahora, usa cuadrados de colores sólidos (Fill) para representar las entidades.`

* 💡 *Nota del Ingeniero:* Pedirle a la IA que inicie con cuadrados de colores permite probar que la física y los inputs funcionan antes de complicarnos cargando archivos de imágenes.

---

## FASE 4: Lógica de Clases y Refinamiento

*Instrucción:* Una vez que el cuadrado se mueve, vamos a pedirle a la IA que mejore partes específicas del código.

**8. Generación de Lógica Aislada (Optimizando Memoria)**

> `Actúa como un Senior Python Developer. Revisa la clase 'Enemy' de mi código de Pygame. El enemigo debe inicializarse en la parte superior de la pantalla (y < 0) en una coordenada X aleatoria. Debe moverse hacia abajo en el eje Y a una velocidad aleatoria entre 2 y 5. Implementa el método update() y asegúrate de incluir self.kill() si el objeto sobrepasa el límite inferior de la pantalla (SCREEN_HEIGHT = 600) para liberar memoria y evitar fugas (memory leaks).`

---

## FASE 5: QA, Colisiones y Depuración

*Instrucción:* El código base de la IA rara vez maneja las colisiones perfectamente al primer intento. Usa esto para corregirlo.

**9. Resolución de Colisiones Exactas**

> `Tengo dos grupos de sprites en Pygame: 'bullets' y 'enemies'. Escribe la línea de código exacta usando 'pygame.sprite.groupcollide' para detectar impactos. Quiero que AMBOS objetos se eliminen al chocar. Además, proporciona un bucle 'for' para iterar sobre las colisiones resultantes, sumar 10 puntos a una variable global 'score', e instanciar la reproducción de mi archivo de sonido 'explosion.wav'.`

**10. Prompt de Rescate (Si algo sale mal)**

> `Estoy recibiendo el error 'pygame.error: video system not initialized' al intentar ejecutar mi archivo. Las constantes de pantalla están en un archivo separado. ¿Cuál es el error en el orden de ejecución de mis imports y la inicialización de pygame.init()? Explica la solución desde la perspectiva del ciclo de vida del software.`

---

## FASE 6: El "Juice" (Pulido y Game Feel)

*Instrucción:* Integraremos las imágenes transparentes y los efectos visuales para que deje de parecer un proyecto de consola y se vea profesional.

**11. Implementación del Parallax Scrolling**

> `Tengo dos imágenes para el fondo de mi juego en Pygame: 'estrellas.png' (fondo opaco) y 'nebulosa.png' (fondo transparente). Escribe el código necesario para implementarlas en mi Game Loop creando un efecto 'Parallax Vertical Infinito'. Las estrellas deben bajar a 1 píxel por frame, y la nebulosa a 3 píxeles por frame. Recuerda la lógica para reiniciar la coordenada Y cuando la imagen sale de la pantalla.`

**12. Implementación de "Screen Shake"**

> `Quiero añadir un efecto de 'Screen Shake' (temblor de pantalla) en Pygame cuando el jugador reciba daño de un enemigo. Mi superficie principal se llama 'screen'. Escribe una función 'screen_shake(duration, intensity)' que desplace temporalmente el renderizado general unos cuantos píxeles de forma aleatoria durante X frames sin modificar las coordenadas reales (Hitboxes) de los sprites.`
>
