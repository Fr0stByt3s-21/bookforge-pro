from icnsutil import IcnsFile
from PIL import Image
import os
import shutil

input_path = 'assets/icon.png'
output_path = 'assets/icon.icns'
temp_dir = 'assets/temp_icns'

os.makedirs(temp_dir, exist_ok=True)

sizes = [16, 32, 64, 128, 256, 512, 1024]

try:
    img = Image.open(input_path).convert('RGBA')
    icns = IcnsFile()
    for size in sizes:
        temp_file = os.path.join(temp_dir, f'{size}.png')
        img.resize((size, size), Image.LANCZOS).save(temp_file)
        icns.add_media(file=temp_file)
    icns.write(output_path)
    print(f"✅ ICNS file created: {output_path}")
except Exception as e:
    print(f"❌ Error: {e}")
finally:
    shutil.rmtree(temp_dir, ignore_errors=True)
