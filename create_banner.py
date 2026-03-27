"""
Script to create a professional banner image for Task Manager Pro
Run this to generate the banner.png file
"""

try:
    from PIL import Image, ImageDraw, ImageFont
    import os
    
    # Create banner
    width, height = 1200, 400
    
    # Create gradient background
    img = Image.new('RGB', (width, height), color='white')
    draw = ImageDraw.Draw(img)
    
    # Draw gradient background (blue to purple)
    for y in range(height):
        r = int(44 + (142 - 44) * y / height)
        g = int(62 + (68 - 62) * y / height)
        b = int(80 + (173 - 80) * y / height)
        draw.rectangle([(0, y), (width, y + 1)], fill=(r, g, b))
    
    # Try to use a nice font, fallback to default
    try:
        title_font = ImageFont.truetype("arial.ttf", 80)
        subtitle_font = ImageFont.truetype("arial.ttf", 35)
        emoji_font = ImageFont.truetype("seguiemj.ttf", 100)
    except:
        title_font = ImageFont.load_default()
        subtitle_font = ImageFont.load_default()
        emoji_font = ImageFont.load_default()
    
    # Draw emoji/icon
    draw.text((100, 150), "📋", font=emoji_font, fill='white')
    
    # Draw title
    draw.text((280, 120), "Task Manager Pro", font=title_font, fill='white')
    
    # Draw subtitle
    draw.text((280, 220), "Organize • Prioritize • Achieve", font=subtitle_font, fill='#E8F4F8')
    
    # Draw decorative elements
    draw.ellipse([950, 50, 1050, 150], outline='white', width=3)
    draw.ellipse([1050, 250, 1150, 350], outline='white', width=3)
    
    # Save
    output_path = os.path.join('assets', 'banner.png')
    img.save(output_path, 'PNG', quality=95)
    print(f"✅ Banner created successfully: {output_path}")
    print("📏 Size: 1200x400 pixels")
    
except ImportError:
    print("⚠️  Pillow library not found!")
    print("📦 Install it with: pip install Pillow")
    print("🎨 Or create your banner manually using:")
    print("   - Canva (https://www.canva.com)")
    print("   - Figma (https://www.figma.com)")
    print("   - Photoshop or GIMP")
    print("\n💡 Recommended banner size: 1200x400 pixels")
