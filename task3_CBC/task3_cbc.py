from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad
from PIL import Image

def encrypt_cbc(image_path, key):
 
    img = Image.open(image_path)
    
  
    img_bytes = img.tobytes()
    
    padded_img_bytes = pad(img_bytes, AES.block_size)

    iv = get_random_bytes(AES.block_size)
   
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    
    # Encrypt the padded bytes
    encrypted_data = cipher.encrypt(padded_img_bytes)
    
    # Return the IV and encrypted data
    return iv, encrypted_data

def save_encrypted_image(iv, encrypted_data, output_path):
    
    with open(output_path, 'wb') as f:
        f.write(iv)
        f.write(encrypted_data)

# Example usage
if __name__ == "__main__":
    # Path to the image
    image_path = "./pic_original.bmp"
    
    # Generate a random 128-bit (16 bytes) key
    key = get_random_bytes(16)
    
    # Encrypt the image
    iv, encrypted_data = encrypt_cbc(image_path, key)
    
    # Save the encrypted image
    output_path = "CBC_encrypted_image_cbc.bmp"
    save_encrypted_image(iv, encrypted_data, output_path)
