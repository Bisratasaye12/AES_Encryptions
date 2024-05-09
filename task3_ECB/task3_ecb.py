from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad
from PIL import Image

def encrypt_ecb(image_path, key):
    # Open the image
    img = Image.open(image_path)
    
    # Convert the image to bytes
    img_bytes = img.tobytes()
    
    # Pad the bytes to be a multiple of AES block size
    padded_img_bytes = pad(img_bytes, AES.block_size)
    
    # Create AES cipher object with ECB mode
    cipher = AES.new(key, AES.MODE_ECB)
    
    # Encrypt the padded bytes
    encrypted_data = cipher.encrypt(padded_img_bytes)
    
    # Return the encrypted data
    return encrypted_data

def save_encrypted_image(encrypted_data, output_path):
    # Write the encrypted data to a file
    with open(output_path, 'wb') as f:
        f.write(encrypted_data)

# Example usage
if __name__ == "__main__":
    # Path to the image
    image_path = "./pic_original.bmp"
    
    # Generate a random 128-bit (16 bytes) key
    key = get_random_bytes(16)
    
    # Encrypt the image
    encrypted_data = encrypt_ecb(image_path, key)
    
    # Save the encrypted image
    output_path = "encrypted_image.bmp"
    save_encrypted_image(encrypted_data, output_path)
