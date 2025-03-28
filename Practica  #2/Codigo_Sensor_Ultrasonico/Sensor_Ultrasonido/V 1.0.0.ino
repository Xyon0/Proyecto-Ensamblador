// V 1.0.0
const int trigPin = 3; // Definimos el pin 3 como el pin de (trig) del sensor ultrasónico
const int echoPin = 4; // Definimos el pin 4 como el pin de (echo) del sensor ultrasónico

float duration, distance; // Declaramos variables para almacenar la duración del pulso y la distancia calculada

void setup() {
  pinMode(trigPin, OUTPUT);  // Configuramos el pin de disparo como salida
  pinMode(echoPin, INPUT);   // Configuramos el pin de eco como entrada
  Serial.begin(9600);        // Iniciamos la comunicación serie a 9600 baudios para enviar datos al monitor serie
}

void loop() {
  digitalWrite(trigPin, LOW);  // Aseguramos que el pin de disparo esté en LOW para iniciar la medición
  delayMicroseconds(2);         // Esperamos 2 microsegundos para estabilizar el pin
  digitalWrite(trigPin, HIGH); // Enviamos un pulso alto al pin de disparo
  delayMicroseconds(10);        // Mantenemos el pulso alto durante 10 microsegundos
  digitalWrite(trigPin, LOW);  // Apagamos el pulso en el pin de disparo

  duration = pulseIn(echoPin, HIGH); // Medimos la duración del pulso de eco que regresa al pin de eco
  distance = (duration * 0.0343) / 2; // Calculamos la distancia en centímetros (velocidad del sonido en cm/us, dividido por 2 para el viaje de ida y vuelta)
  Serial.print("Distance: "); // Imprimimos el texto "Distance: " en el monitor serie
  Serial.println(distance);    // Imprimimos la distancia calculada en el monitor serie
  delay(100);                 // Esperamos 100 milisegundos antes de repetir el ciclo
}
