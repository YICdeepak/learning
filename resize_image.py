#!/usr/bin/env python3
"""
Image Resizer Script
This script resizes the ig.png image to decrease its file size
"""

from PIL import Image
import os

def resize_image(input_path, output_path, max_width=800, max_height=600):
    """
    Resize an image while maintaining aspect ratio
    
    Args:
        input_path: Path to input image
        output_path: Path to save resized image
        max_width: Maximum width in pixels
        max_height: Maximum height in pixels
    """
    try:
        # Open the original image
        with Image.open(input_path) as img:
            # Get original dimensions
            original_width, original_height = img.size
            
            # Calculate aspect ratio
            aspect_ratio = original_width / original_height
            
            # Calculate new dimensions while maintaining aspect ratio
            if original_width > original_height:
                new_width = min(max_width, original_width)
                new_height = int(new_width / aspect_ratio)
            else:
                new_height = min(max_height, original_height)
                new_width = int(new_height * aspect_ratio)
            
            # Ensure new dimensions don't exceed max values
            if new_width > max_width:
                new_width = max_width
                new_height = int(new_width / aspect_ratio)
            if new_height > max_height:
                new_height = max_height
                new_width = int(new_height * aspect_ratio)
            
            # Resize the image
            resized_img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
            
            # Save the resized image
            resized_img.save(output_path, optimize=True, quality=85)
            
            # Calculate size reduction
            original_size = os.path.getsize(input_path)
            new_size = os.path.getsize(output_path)
            reduction = ((original_size - new_size) / original_size) * 100
            
            print(f"✅ Image resized successfully!")
            print(f"Original dimensions: {original_width}x{original_height}")
            print(f"New dimensions: {new_width}x{new_height}")
            print(f"Original size: {original_size / 1024:.2f} KB")
            print(f"New size: {new_size / 1024:.2f} KB")
            print(f"Size reduction: {reduction:.1f}%")
            
            return True
            
    except Exception as e:
        print(f"❌ Error resizing image: {str(e)}")
        return False

def create_multiple_sizes():
    """Create multiple resized versions of the image"""
    input_file = "ig.png"
    
    if not os.path.exists(input_file):
        print(f"❌ {input_file} not found in current directory")
        return
    
    # Create different size versions
    sizes = {
        "small": (400, 300),
        "medium": (600, 450),
        "large": (800, 600)
    }
    
    for size_name, dimensions in sizes.items():
        output_file = f"ig_{size_name}.png"
        print(f"\n🔄 Creating {size_name} version...")
        resize_image(input_file, output_file, *dimensions)

if __name__ == "__main__":
    print("🖼️ Image Resizer Tool")
    print("=" * 30)
    
    # Check if PIL is available
    try:
        from PIL import Image
    except ImportError:
        print("❌ PIL/Pillow not found. Installing...")
        import subprocess
        subprocess.run(["pip", "install", "Pillow"])
        from PIL import Image
    
    # Create multiple resized versions
    create_multiple_sizes()
    
    print("\n✨ All resized images created successfully!")
    print("📁 Check your directory for the new image files:")
    print("   - ig_small.png (400x300)")
    print("   - ig_medium.png (600x450)")
    print("   - ig_large.png (800x600)")
