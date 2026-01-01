import os
import sys
from pathlib import Path
from PIL import Image
from pillow_heif import register_heif_opener

register_heif_opener()


def convert_heic_to_png(input_dir: str = "image/20260101", output_dir: str = "image/converted"):
    input_path = Path(input_dir)
    output_path = Path(output_dir)
    
    if not input_path.exists():
        print(f"Error: Input directory '{input_dir}' does not exist")
        return
    
    output_path.mkdir(parents=True, exist_ok=True)
    
    heic_files = list(input_path.glob("*.heic")) + list(input_path.glob("*.HEIC"))
    
    if not heic_files:
        print(f"No HEIC files found in '{input_dir}'")
        return
    
    print(f"Found {len(heic_files)} HEIC files to convert")
    
    for heic_file in heic_files:
        try:
            with Image.open(heic_file) as img:
                png_filename = heic_file.stem + ".png"
                png_path = output_path / png_filename
                
                img.save(png_path, "PNG")
                print(f"Converted: {heic_file.name} → {png_filename}")
                
        except Exception as e:
            print(f"Error converting {heic_file.name}: {e}")
    
    print(f"Conversion complete! Files saved to '{output_dir}'")


def main():
    if len(sys.argv) > 1:
        input_dir = sys.argv[1]
        output_dir = sys.argv[2] if len(sys.argv) > 2 else "image/converted"
        convert_heic_to_png(input_dir, output_dir)
    else:
        convert_heic_to_png()


if __name__ == "__main__":
    main()
