import numpy as np
import cv2 #Importamos la libreria de OpenCV

# URL del archivo XML
face_cascade = cv2.CascadeClassifier('C:/**Sitio donde esta guardado el ->**/haarcascade_frontalface_alt.xml')
#Ligamos el cascade para que lo utilice en la detección de rostro: XML con algoritmos.

cap = cv2.VideoCapture(0) #Se consultan los modulos de la camara para que se active.

# Ciclo de deteccion de caras, toma de coordenadas para dibujar cuadrado de detección
while(True): #Ciclo infinito para que no se cancele o cierre la ventana
    ret, img = cap.read() #Variables capturadoras (leen)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #Variable donde se guarda una copia en escala de grises de la toma de la camara
    faces = face_cascade.detectMultiScale(gray, 1.3, 5) #Obtenemos una lista de todos los rostros encontrados en el frame.

    for (x,y,w,h) in faces: #Con el for se dibuja un rectángulo y se obtiene una copia del area donde se ha detectado un rostro, coordenadas establecidas
        cv2.rectangle(img,(x,y),(x+w,y+h),(123.255,0),2)

# Reemplazar imagen original por la actual con el cuadrado de detección en tiempo real
    cv2.imshow('Reconocimiento Facial',img)

    # Cierre de ventana mediante la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

