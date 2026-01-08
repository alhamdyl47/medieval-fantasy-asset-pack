import os
import json
from pathlib import Path

class AssetManager:
    """Manages game assets: textures, models, sounds, levels"""
    
    ASSET_TYPES = {
        '.png': 'texture',
        '.jpg': 'texture', 
        '.obj': 'model',
        '.fbx': 'model',
        '.wav': 'sound',
        '.mp3': 'sound',
        '.json': 'level'
    }
    
    def __init__(self, assets_path):
        self.assets_path = Path(assets_path)
        
    def scan_assets(self):
        """Scan directory for game assets"""
        assets = []
        
        for file_path in self.assets_path.rglob('*'):
            if file_path.is_file():
                ext = file_path.suffix.lower()
                if ext in self.ASSET_TYPES:
                    assets.append({
                        'name': file_path.name,
                        'path': str(file_path),
                        'type': self.ASSET_TYPES[ext],
                        'size': file_path.stat().st_size
                    })
        
        return assets
    
    def generate_index(self, assets):
        """Generate asset index file"""
        index = {'assets': assets, 'count': len(assets)}
        
        with open('assets_index.json', 'w') as f:
            json.dump(index, f, indent=2)
        
        return index