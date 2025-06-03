# Importación de bibliotecas necesarias
import cv2  # OpenCV para procesamiento de imágenes y video
import mediapipe as mp  # MediaPipe para detección de manos
import pickle   # Para serializar/deserializar los modelos
import os   # Para operaciones con el sistema de archivos

# Configuración inicial del directorio para guardar modelos
carpeta_modelos = "modelos_señas"   # Nombre de la carpeta para almacenar modelos
os.makedirs(carpeta_modelos, exist_ok=True) # Crea la carpeta si no existe

# Configuración de MediaPipe Hands para detección de manos
mp_hands = mp.solutions.hands   # Módulo de detección de manos de MediaPipe

# Configuración del detector de manos:
hands = mp_hands.Hands(
        static_image_mode=False, # Modo video (mejor rendimiento para secuencias)
        max_num_hands=1,    # Máximo 1 mano a detectar
        min_detection_confidence=0.7    # Umbral mínimo de confianza para detección
                       )
mp_drawing = mp.solutions.drawing_utils # Utilidades para dibujar las marcas de manos

#  Inicialización de captura de video
cap = cv2.VideoCapture(0)   # Abre la cámara predeterminada 

# Instrucciones para el usuario
print("Presioná 'ESPACIO' para capturar una letra. Presioná 'ESC' para salir.")

# Bucle principal de captura de video
while True:
    # Captura de frame de la cámara
    ret, frame = cap.read() # Lee un frame de la cámara
    if not ret: # Si falla la captura
        print("No se pudo acceder a la cámara.")    # Mensaje de error
        break   #   Rompe el bucle

    # Preprocesamiento del frame
    frame = cv2.flip(frame, 1)  # Voltear horizontalmente para efecto espejo
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)    # Convertir a RGB (requerido por MediaPipe)

    # Detección de manos en el frame
    resultado = hands.process(rgb)  # Procesa el frame para detectar manos

    # Dibujar landmarks si se detectan manos
    if resultado.multi_hand_landmarks:  # Si se detectaron manos
        for mano in resultado.multi_hand_landmarks:# Para cada mano detectada

            # Dibuja los landmarks y conexiones en la imagen
            mp_drawing.draw_landmarks(frame, mano, mp_hands.HAND_CONNECTIONS)

    # Mostrar instrucciones en pantalla
    cv2.putText(frame, "Presioná ESPACIO para capturar modelo", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

    # Mostrar el frame procesado
    cv2.imshow("Captura de modelos", frame)

    # Captura de teclas presionadas
    tecla = cv2.waitKey(1) & 0xFF   # Espera 1ms por entrada de teclado

    # Manejo de teclas especiales
    if tecla == 27: # Tecla ESC
        break   #   Rompe el bucle
    elif tecla == 32:   # Tecla ESPACIO
        if resultado.multi_hand_landmarks:  # Si hay manos detectadas
            for mano in resultado.multi_hand_landmarks: # Para cada mano
                keypoints = []  # Lista para almacenar puntos clave
                alto, ancho, _ = frame.shape    # Dimensiones del frame

                # Convertir landmarks a coordenadas de píxeles
                for lm in mano.landmark:    # Para cada punto de referencia
                    x = int(lm.x * ancho)   # Coordenada X normalizada a píxeles
                    y = int(lm.y * alto)    # Coordenada Y normalizada a píxeles
                    keypoints.append((x, y))    # Agrega punto a la lista

                # Interacción con el usuario para obtener la letra
                letra = input("Ingresá la letra que estás mostrando (A-Z): ").upper()

                # Validación de la entrada del usuario
                if len(letra) != 1 or not letra.isalpha():  # Si no es una sola letra
                    print("Entrada inválida. Se esperaba una letra.")
                    continue    # Vuelve al inicio del bucle

                # Configuración de ruta para guardar el modelo
                ruta = os.path.join(carpeta_modelos, f"modelo_{letra}.pkl")

                # Manejo de modelos existentes
                if os.path.exists(ruta):    # Si ya existe un modelo para esta letra
                    resp = input(f"Ya existe un modelo para '{letra}'. ¿Sobrescribir? (s/n): ").lower()
                    if resp != 's': # Si no quiere sobrescribir
                        print("Modelo no guardado.")
                        continue    # Vuelve al inicio del bucle

                # Creación del diccionario del modelo
                modelo = {
                    "letra": letra, # Letra asociada
                    "keypoints": keypoints  # Puntos clave de la mano
                }

                # Guardado del modelo serializado
                with open(ruta, "wb") as f: # Abre archivo en modo escritura binaria
                    pickle.dump(modelo, f)  # Serializa y guarda el modelo

                print(f"Modelo para la letra '{letra}' guardado exitosamente.")
        else:   # Si no se detectaron manos al presionar ESPACIO
            print("No se detectó una mano. Asegurate de que esté bien visible.")

# Liberación de recursos al terminar
cap.release()   # Libera la cámara
cv2.destroyAllWindows() # Cierra todas las ventanas abiertas

