"""
Quick test to verify the app components work
"""

import sys
import importlib

def test_imports():
    """Test if all required packages can be imported"""
    required_packages = [
        'streamlit',
        'PIL',
        'google.genai',
        'dotenv'
    ]
    
    print("🔍 Testing package imports...")
    
    for package in required_packages:
        try:
            if package == 'PIL':
                import PIL
                print(f"✅ {package} - OK (version: {PIL.__version__})")
            elif package == 'google.genai':
                import google.genai as genai
                print(f"✅ {package} - OK")
            elif package == 'streamlit':
                import streamlit as st
                print(f"✅ {package} - OK (version: {st.__version__})")
            elif package == 'dotenv':
                import dotenv
                print(f"✅ {package} - OK")
        except ImportError as e:
            print(f"❌ {package} - FAILED: {e}")
            return False
    
    print("\n🎉 All packages imported successfully!")
    return True

def check_env_file():
    """Check if .env file exists and has the right structure"""
    import os
    
    if os.path.exists('.env'):
        print("✅ .env file found")
        with open('.env', 'r') as f:
            content = f.read()
            if 'GEMINI_API_KEY' in content:
                print("✅ GEMINI_API_KEY placeholder found in .env")
                if 'your_actual_api_key_here' in content:
                    print("⚠️  Please replace 'your_actual_api_key_here' with your actual API key")
                else:
                    print("✅ API key appears to be set")
            else:
                print("❌ GEMINI_API_KEY not found in .env file")
    else:
        print("❌ .env file not found")

if __name__ == "__main__":
    print("🧪 Furniture Visualizer App - Quick Test")
    print("=" * 50)
    
    success = test_imports()
    if success:
        print("\n📁 Checking configuration...")
        check_env_file()
        
        print("\n🚀 Ready to run!")
        print("\nNext steps:")
        print("1. Add your Gemini API key to the .env file")
        print("2. Run: streamlit run app.py")
    else:
        print("\n❌ Some packages failed to import. Please check the installation.")
