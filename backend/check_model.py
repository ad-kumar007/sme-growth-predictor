"""
Debug script to check model file location
"""
import os
from pathlib import Path

print("=" * 80)
print("MODEL FILE DEBUG INFO")
print("=" * 80)

# Current working directory
cwd = Path.cwd()
print(f"\n1. Current Working Directory: {cwd}")

# List files in cwd
print(f"\n2. Files in CWD (first 20):")
try:
    files = list(cwd.iterdir())[:20]
    for f in files:
        print(f"   - {f.name} ({'dir' if f.is_dir() else f'file, {f.stat().st_size} bytes'})")
except Exception as e:
    print(f"   Error: {e}")

# Check ml_model directory
ml_model_paths = [
    cwd / "ml_model",
    cwd / "backend" / "ml_model",
    Path("/opt/render/project/src/ml_model"),
    Path(__file__).parent.parent / "ml_model",
]

print(f"\n3. Checking ml_model directories:")
for path in ml_model_paths:
    exists = path.exists()
    print(f"   - {path}: {'EXISTS' if exists else 'NOT FOUND'}")
    if exists and path.is_dir():
        try:
            files = list(path.iterdir())
            print(f"     Files: {[f.name for f in files]}")
        except Exception as e:
            print(f"     Error listing: {e}")

# Check environment variable
print(f"\n4. Environment Variables:")
print(f"   - MODEL_PATH: {os.getenv('MODEL_PATH', 'NOT SET')}")
print(f"   - PORT: {os.getenv('PORT', 'NOT SET')}")

# Check if model file exists at expected location
model_file = cwd / "ml_model" / "sme_digitalization_model_final.pkl"
print(f"\n5. Expected model file: {model_file}")
print(f"   Exists: {model_file.exists()}")
if model_file.exists():
    print(f"   Size: {model_file.stat().st_size} bytes")

print("\n" + "=" * 80)
