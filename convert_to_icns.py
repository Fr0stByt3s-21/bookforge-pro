from icnsutil import IcnsFile
from PIL import Image
import os

# Paths
input_path = 'assets/icon.png'
output_path = 'assets/icon.icns'
temp_dir = 'assets/temp_icns'

# Create temp folder if not exists
os.makedirs(temp_dir, exist_ok=True)

# Sizes required by macOS ICNS
sizes = [16, 32, 64, 128, 256, 512, 1024]

# Load original image
img = Image.open(input_path)

# Create ICNS object
icns = IcnsFile()

# Generate resized images and add to ICNS
for size in sizes:
    temp_file = os.path.join(temp_dir, f'{size}.png')
    img.resize((size, size)).save(temp_file)
    icns.add_media(file=temp_file)

# Save ICNS file
icns.write(output_path)
print(f"✅ ICNS file created: {output_path}")
