"""
Demo script for Furniture Visualizer
This script demonstrates the core functionality without the web interface
"""

import os
from PIL import Image
from google import genai
from google.genai import types
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def demo_furniture_visualization():
    """Demo function to test furniture visualization"""
    
    # Initialize client
    api_key = os.getenv('GEMINI_API_KEY')
    if not api_key:
        print("❌ Error: GEMINI_API_KEY not found in .env file")
        print("Please add your API key to the .env file")
        return
    
    client = genai.Client(api_key=api_key)
    model_id = "gemini-2.5-flash-image-preview"
    
    print("🏠 Furniture Visualizer Demo")
    print("=" * 40)
    
    # For demo, we'll create a room description instead of uploading
    # In the real app, this would be an uploaded image
    room_description = """
    Create a photorealistic living room with:
    - Hardwood floors
    - White walls  
    - A large window with natural light
    - Empty space suitable for furniture placement
    - Modern interior design style
    """
    
    print("🎯 Generating base room...")
    try:
        # First, generate a base room
        room_response = client.models.generate_content(
            model=model_id,
            contents=room_description,
            config=types.GenerateContentConfig(
                response_modalities=['Image']
            )
        )
        
        # Save the base room
        base_room = None
        for part in room_response.parts:
            # Try inline_data first
            if hasattr(part, 'inline_data') and part.inline_data and hasattr(part.inline_data, 'data'):
                try:
                    from PIL import Image
                    import io
                    image_data = part.inline_data.data
                    base_room = Image.open(io.BytesIO(image_data))
                    base_room.save('demo_room.png')
                    print("✅ Base room saved as 'demo_room.png'")
                    break
                except Exception as e:
                    print(f"Error with inline_data: {e}")
                    continue
        
        if base_room is None:
            print("❌ No image generated for base room")
            return
        
        # Now add furniture to the room
        furniture_prompt = """
        Take this room image and add a modern gray sectional sofa to it.
        
        Placement: Place the sofa against the far wall, facing toward the center of the room.
        
        Requirements:
        - Make the sofa look realistic and properly scaled for the room
        - Ensure proper lighting and shadows that match the room's lighting  
        - The sofa should blend naturally with the existing room decor
        - Maintain the original room's perspective and style
        - Make it look like a professional interior design visualization
        
        Generate a photorealistic image showing how this sofa would look in the room.
        """
        
        print("🛋️ Adding furniture to room...")
        
        furniture_response = client.models.generate_content(
            model=model_id,
            contents=[furniture_prompt, base_room],
            config=types.GenerateContentConfig(
                response_modalities=['Image']
            )
        )
        
        # Save the furnished room
        for part in furniture_response.parts:
            if hasattr(part, 'inline_data') and part.inline_data and hasattr(part.inline_data, 'data'):
                try:
                    from PIL import Image
                    import io
                    image_data = part.inline_data.data
                    furnished_room = Image.open(io.BytesIO(image_data))
                    furnished_room.save('demo_furnished_room.png')
                    print("✅ Furnished room saved as 'demo_furnished_room.png'")
                    print("🎉 Demo complete! Check the generated images.")
                    return
                except Exception as e:
                    print(f"Error with inline_data: {e}")
                    continue
        
        print("❌ No image generated for furnished room")
                
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        print("Make sure your API key is valid and you have internet connection")

def test_api_connection():
    """Test if the API key works"""
    api_key = os.getenv('GEMINI_API_KEY')
    if not api_key:
        print("❌ No API key found")
        return False
    
    try:
        client = genai.Client(api_key=api_key)
        # Simple test call
        response = client.models.generate_content(
            model="gemini-2.5-flash-image-preview",
            contents="Create a simple image of a red apple on a white background",
            config=types.GenerateContentConfig(
                response_modalities=['Image']
            )
        )
        print("✅ API connection successful!")
        return True
    except Exception as e:
        print(f"❌ API connection failed: {str(e)}")
        return False

if __name__ == "__main__":
    print("Testing API connection...")
    if test_api_connection():
        print("\nRunning furniture visualization demo...")
        demo_furniture_visualization()
    else:
        print("\nPlease check your API key and try again.")
