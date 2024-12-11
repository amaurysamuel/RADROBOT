import RPi.GPIO as GPIO
import time

# Configuration du mode des pins
GPIO.setmode(GPIO.BCM)

# Définir le GPIO4 comme une entrée
GPIO.setup(4, GPIO.IN)

try:
    while True:
        # Lire l'état du capteur (HIGH ou LOW)
        sensor_value = GPIO.input(4)
        
        if sensor_value == GPIO.HIGH:
            print("Capteur activé!")
        else:
            print("Capteur désactivé!")
        
        # Attendre un peu avant la prochaine lecture
        time.sleep(1)

except KeyboardInterrupt:
    print("Arrêt du programme.")

finally:
    # Nettoyer les configurations des GPIO
    GPIO.cleanup()
