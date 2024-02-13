from PIL import Image

def zoom_image(image_path, scale):
    try:
        # Charger l'image
        image = Image.open(image_path)
        
        # Afficher les informations sur l'image
        print("The size in pixel on both X and Y axis:", image.size)
        print("The number of channel:", len(image.getbands()))
        print("Pixel content of the image:")
        print(list(image.getdata()))
        
        # Effectuer le zoom en réduisant la taille de l'image
        new_width = int(image.width * scale)
        new_height = int(image.height * scale)
        resized_image = image.resize((new_width, new_height))
        
        # Afficher l'échelle sur les axes x et y
        print("New size after resizing:", resized_image.size)
        
        # Afficher l'image zoomée
        resized_image.show()
        
    except Exception as e:
        print("Une erreur s'est produite:", e)

if __name__ == "__main__":
    # Chemin d'accès à l'image
    image_path = "animal.jpeg"
    
    # Facteur d'échelle pour le zoom
    scale = 0.5
    
    # Appeler la fonction pour zoomer l'image
    zoom_image("animal.jpeg", 10)
