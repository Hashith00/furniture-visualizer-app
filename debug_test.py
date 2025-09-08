"""
Simple API test to verify Gemini image generation works
"""

import os
from google import genai
from google.genai import types
from dotenv import load_dotenv
from PIL import Image
import io

load_dotenv()

def test_image_generation():
    """Test basic image generation"""
    
    api_key = os.getenv('GEMINI_API_KEY')
    if not api_key:
        print("❌ No API key found")
        return
    
    print("🧪 Testing Gemini image generation...")
    
    try:
        client = genai.Client(api_key=api_key)
        
        # Simple test prompt
        response = client.models.generate_content(
            model="gemini-2.5-flash-image-preview",
            contents="Create a simple image of a red apple on a white background",
            config=types.GenerateContentConfig(
                response_modalities=['Image']
            )
        )
        
        print("📝 Response received, checking for images...")
        print(f"Response type: {type(response)}")
        print(f"Response has parts: {hasattr(response, 'parts')}")
        
        if hasattr(response, 'parts'):
            print(f"Number of parts: {len(response.parts)}")
            
            for i, part in enumerate(response.parts):
                print(f"Part {i}: {type(part)}")
                print(f"  Has text: {hasattr(part, 'text')}")
                print(f"  Has as_image: {hasattr(part, 'as_image')}")
                
                if hasattr(part, 'text') and part.text:
                    print(f"  Text content: {part.text[:100]}...")
                
                # Try different ways to get the image
                if hasattr(part, 'as_image'):
                    try:
                        genai_image = part.as_image()
                        if genai_image:
                            print(f"  ✅ Image extracted: {type(genai_image)}")
                            pil_image = genai_image.to_pil()
                            pil_image.save('test_apple.png')
                            print("  ✅ Saved as 'test_apple.png'")
                            return True
                    except Exception as e:
                        print(f"  ❌ Error with as_image(): {e}")
                
                # Check for inline_data
                if hasattr(part, 'inline_data'):
                    print(f"  Has inline_data: {part.inline_data is not None}")
                    if part.inline_data and hasattr(part.inline_data, 'data'):
                        try:
                            image_data = part.inline_data.data
                            image = Image.open(io.BytesIO(image_data))
                            image.save('test_apple_inline.png')
                            print("  ✅ Saved via inline_data as 'test_apple_inline.png'")
                            return True
                        except Exception as e:
                            print(f"  ❌ Error with inline_data: {e}")
        
        print("❌ No image found in response")
        return False
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

if __name__ == "__main__":
    test_image_generation()
