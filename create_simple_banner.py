"""
Simple SVG banner creator - no dependencies needed!
Creates a professional banner in SVG format
"""

svg_content = '''<svg width="1200" height="400" xmlns="http://www.w3.org/2000/svg">
  <!-- Gradient Background -->
  <defs>
    <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#2c3e50;stop-opacity:1" />
      <stop offset="50%" style="stop-color:#3498db;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#8e44ad;stop-opacity:1" />
    </linearGradient>
    
    <filter id="shadow">
      <feDropShadow dx="0" dy="4" stdDeviation="4" flood-opacity="0.3"/>
    </filter>
  </defs>
  
  <!-- Background -->
  <rect width="1200" height="400" fill="url(#grad1)"/>
  
  <!-- Decorative circles -->
  <circle cx="1000" cy="100" r="50" fill="none" stroke="rgba(255,255,255,0.2)" stroke-width="3"/>
  <circle cx="1100" cy="300" r="50" fill="none" stroke="rgba(255,255,255,0.2)" stroke-width="3"/>
  <circle cx="150" cy="80" r="30" fill="rgba(255,255,255,0.1)"/>
  <circle cx="1050" cy="200" r="20" fill="rgba(255,255,255,0.1)"/>
  
  <!-- Checkmark icon background -->
  <rect x="80" y="120" width="140" height="140" rx="20" fill="rgba(255,255,255,0.15)"/>
  
  <!-- Checkmark icon -->
  <text x="110" y="220" font-family="Arial, sans-serif" font-size="100" fill="white">✓</text>
  
  <!-- Main Title -->
  <text x="280" y="180" font-family="Arial, sans-serif" font-size="72" font-weight="bold" 
        fill="white" filter="url(#shadow)">
    Task Manager Pro
  </text>
  
  <!-- Subtitle -->
  <text x="280" y="240" font-family="Arial, sans-serif" font-size="32" fill="#E8F4F8">
    Organize • Prioritize • Achieve
  </text>
  
  <!-- Feature badges -->
  <g transform="translate(280, 280)">
    <!-- Python badge -->
    <rect x="0" y="0" width="100" height="35" rx="17.5" fill="rgba(255,255,255,0.2)"/>
    <text x="50" y="23" font-family="Arial, sans-serif" font-size="16" fill="white" text-anchor="middle">
      Python
    </text>
    
    <!-- GUI badge -->
    <rect x="115" y="0" width="80" height="35" rx="17.5" fill="rgba(255,255,255,0.2)"/>
    <text x="155" y="23" font-family="Arial, sans-serif" font-size="16" fill="white" text-anchor="middle">
      GUI
    </text>
    
    <!-- CLI badge -->
    <rect x="210" y="0" width="70" height="35" rx="17.5" fill="rgba(255,255,255,0.2)"/>
    <text x="245" y="23" font-family="Arial, sans-serif" font-size="16" fill="white" text-anchor="middle">
      CLI
    </text>
    
    <!-- Free badge -->
    <rect x="295" y="0" width="75" height="35" rx="17.5" fill="rgba(39,174,96,0.8)"/>
    <text x="332.5" y="23" font-family="Arial, sans-serif" font-size="16" fill="white" text-anchor="middle">
      FREE
    </text>
  </g>
  
  <!-- Decorative lines -->
  <line x1="280" y1="260" x2="450" y2="260" stroke="rgba(255,255,255,0.3)" stroke-width="2"/>
</svg>'''

# Save SVG
with open('assets/banner.svg', 'w', encoding='utf-8') as f:
    f.write(svg_content)

print("✅ SVG banner created: assets/banner.svg")
print("📏 Size: 1200x400 pixels")
print("\n💡 To convert to PNG:")
print("   - Open in browser and take screenshot")
print("   - Use online converter: https://cloudconvert.com/svg-to-png")
print("   - Or use: https://www.svgviewer.dev/")
