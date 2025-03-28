// V 1.0.0
// Definimos el pin para el sensor de ultrasonido (trig) y el pin para la lectura (echo)
const int trigPin = 3;  // Pin de disparo del sensor
const int echoPin = 4;  // Pin de eco del sensor

float duration, distance; // Variables para almacenar la duración del pulso y la distancia medida

void setup() {
  // Configuramos el pin de disparo como salida y el pin de eco como entrada
  pinMode(trigPin, OUTPUT);  
  pinMode(echoPin, INPUT);  
  // Iniciamos la comunicación serie a 9600 baudios para enviar datos al monitor serie
  Serial.begin(9600);  
}

void loop() {
  // Aseguramos que el pin de disparo esté en LOW antes de iniciar la medición
  digitalWrite(trigPin, LOW);  
  delayMicroseconds(2);  // Esperamos 2 microsegundos
  // Enviamos un pulso de 10 microsegundos al pin de disparo
  digitalWrite(trigPin, HIGH);  
  delayMicroseconds(10);  
  digitalWrite(trigPin, LOW);  

  // Medimos la duración del pulso que regresa al pin de eco
  duration = pulseIn(echoPin, HIGH);  
  // Calculamos la distancia en centímetros (la velocidad del sonido es aproximadamente 343 m/s)
  distance = (duration * 0.0343) / 2;  
  // Enviamos la distancia medida al monitor serie
  Serial.print("Distance: ");  
  Serial.println(distance);  
  // Esperamos 100 milisegundos antes de realizar la siguiente medición
  delay(100);  
