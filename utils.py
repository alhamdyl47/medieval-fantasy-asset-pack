"""Utility functions for asset management"""

import os
from pathlib import Path

def create_asset_structure(base_path):
    """Create basic asset directory structure"""
    folders = ['textures', 'models', 'sounds', 'levels']
    
    base = Path(base_path)
    base.mkdir(exist_ok=True)
    
    for folder in folders:
        (base / folder).mkdir(exist_ok=True)
    
    print(f"Created asset structure in {base_path}")

def get_file_info(file_path):
    """Get basic file information"""
    path = Path(file_path)
    
    if not path.exists():
        return None
    
    return {
        'name': path.name,
        'size': path.stat().st_size,
        'extension': path.suffix,
        'modified': path.stat().st_mtime
    }

def format_file_size(size_bytes):
    """Format file size in human readable format"""
    if size_bytes < 1024:
        return f"{size_bytes} B"
    elif size_bytes < 1024**2:
        return f"{size_bytes/1024:.1f} KB"
    else:
        return f"{size_bytes/(1024**2):.1f} MB"