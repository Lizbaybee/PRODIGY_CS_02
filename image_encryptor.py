from PIL import Image
import os

def encrypt_image(input_path, output_path, key):
    """Encrypt image by modifying pixel values and swapping them."""
    img = Image.open(input_path)
    pixels = img.load()

    width, height = img.size

    # Step 1: Add key to each RGB value
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            pixels[x, y] = ((r + key) % 256, (g + key) % 256, (b + key) % 256)

    # Step 2: Swap adjacent pixels in a consistent pattern
    for y in range(height):
        for x in range(0, width - 1, 2):  # step by 2 to avoid double swapping
            pixels[x, y], pixels[x + 1, y] = pixels[x + 1, y], pixels[x, y]

    img.save(output_path)
    print(f"Image encrypted and saved as: {output_path}")


def decrypt_image(input_path, output_path, key):
    """Decrypt image by reversing pixel swaps and subtracting the key."""
    img = Image.open(input_path)
    pixels = img.load()

    width, height = img.size

    # Step 1: Reverse pixel swapping
    for y in range(height):
        for x in range(0, width - 1, 2):  # reverse the same pattern
            pixels[x, y], pixels[x + 1, y] = pixels[x + 1, y], pixels[x, y]

    # Step 2: Subtract key from each RGB value
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            pixels[x, y] = ((r - key) % 256, (g - key) % 256, (b - key) % 256)

    img.save(output_path)
    print(f"Image decrypted and saved as: {output_path}")



if __name__ == "__main__":
    input_file = input("Enter the path to the image: ").strip()
    mode = input("Enter 'E' to encrypt or 'D' to decrypt: ").strip().upper()
    key = int(input("Enter numeric key (e.g., 50): "))

    if mode == 'E':
        output_file = "encrypted_" + os.path.basename(input_file)
        encrypt_image(input_file, output_file, key)
    elif mode == 'D':
        output_file = "decrypted_" + os.path.basename(input_file)
        decrypt_image(input_file, output_file, key)
    else:
        print("Invalid mode. Please enter 'E' or 'D'.")
