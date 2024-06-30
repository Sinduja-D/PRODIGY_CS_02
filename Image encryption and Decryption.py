from PIL import Image

def encrypt_image(image):
    encrypted_image = image.copy()
    width, height = image.size

    for x in range(width):
        for y in range(height):
            pixel = image.getpixel((x, y))
            if image.mode == 'RGB':
                r, g, b = pixel
                # Swapping pixel values for RGB images
                g, b = b, g
                encrypted_image.putpixel((x, y), (r, g, b))
    return encrypted_image

def decrypt_image(image):
    decrypted_image = image.copy()
    width, height = image.size

    for x in range(width):
        for y in range(height):
            pixel = image.getpixel((x, y))
            if image.mode == 'RGB':
                r, g, b = pixel
                # Reversing the swapping of pixel values for RGB images
                g, b = b, g
                decrypted_image.putpixel((x, y), (r, g, b))
    return decrypted_image

def compare_images(image1, image2):
    width, height = image1.size
    for x in range(width):
        for y in range(height):
            pixel1 = image1.getpixel((x, y))
            pixel2 = image2.getpixel((x, y))
            if pixel1 != pixel2:
                return False
    return True

# Load the image
image_path = r"d:\Users\Sinduja\Documents\PYTHON Files\Python VS Code\Original Image.jpg"
image = Image.open(image_path)

# Encrypt the image
encrypted_image = encrypt_image(image)
encrypted_image.save("encrypted_image.jpg")
print("Encryption successful!")

# Decrypt the image
decrypted_image = decrypt_image(encrypted_image)

# Compare the decrypted image with the original image
if compare_images(image, decrypted_image):
    decrypted_image.save("decrypted_image.jpg")
    print("Decryption successful!")
