"""
Sample room generator for testing the furniture visualizer
This creates sample room images you can use to test the app
"""

import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

def generate_sample_rooms():
    """Generate sample room images for testing"""
    
    api_key = os.getenv('GEMINI_API_KEY')
    if not api_key or api_key == 'your_actual_api_key_here':
        print("❌ Please set your actual GEMINI_API_KEY in the .env file first")
        return
    
    client = genai.Client(api_key=api_key)
    model_id = "gemini-2.5-flash-image-preview"
    
    sample_rooms = {
        "living_room": """
        Create a photorealistic empty living room with:
        - Hardwood floors
        - White walls with one accent wall in light gray
        - Large windows with natural daylight
        - High ceilings
        - Modern architectural style
        - Empty space ready for furniture
        - Neutral color palette
        """,
        
        "bedroom": """
        Create a photorealistic empty bedroom with:
        - Carpet flooring in beige
        - Soft white walls
        - One large window with sheer curtains
        - Built-in closet with sliding doors
        - Modern contemporary style
        - Empty space suitable for bedroom furniture
        """,
        
        "dining_room": """
        Create a photorealistic empty dining room with:
        - Tile flooring in warm gray
        - White walls with wainscoting
        - Chandelier hanging from ceiling
        - Large window overlooking garden
        - Traditional style with modern elements
        - Open space perfect for dining furniture
        """
    }
    
    print("🏠 Generating sample rooms for testing...")
    
    for room_name, description in sample_rooms.items():
        print(f"\n🎯 Generating {room_name}...")
        
        try:
            response = client.models.generate_content(
                model=model_id,
                contents=description,
                config=types.GenerateContentConfig(
                    response_modalities=['Image']
                )
            )
            
            # Save the room image
            for part in response.parts:
                if hasattr(part, 'as_image'):
                    room_image = part.as_image()
                    filename = f"sample_{room_name}.png"
                    room_image.save(filename)
                    print(f"✅ Saved {filename}")
                    break
                    
        except Exception as e:
            print(f"❌ Error generating {room_name}: {str(e)}")
    
    print("\n🎉 Sample rooms generated! You can now use these to test the furniture visualizer.")
    print("Upload any of the generated images in the app to try different furniture.")

if __name__ == "__main__":
    generate_sample_rooms()
