#!/usr/bin/env python3
"""Game Assets Manager - Simple tool for managing game assets"""

import json
from pathlib import Path
from asset_manager import AssetManager

def main():
    print("🎮 Game Assets Manager v1.0")
    
    # Load configuration
    with open('config.json', 'r') as f:
        config = json.load(f)
    
    # Initialize asset manager
    manager = AssetManager(config['assets_path'])
    
    # Scan for assets
    assets = manager.scan_assets()
    print(f"Found {len(assets)} assets:")
    
    for asset in assets:
        print(f"  📁 {asset['name']} ({asset['type']})")
    
    # Generate asset index
    manager.generate_index(assets)
    print("✅ Asset index generated!")

if __name__ == "__main__":
    main()