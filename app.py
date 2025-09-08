import streamlit as st
import os
from PIL import Image
import io
from google import genai
from google.genai import types
from dotenv import load_dotenv
import base64

# Load environment variables
load_dotenv()

# Furniture catalog with categories and styles
FURNITURE_CATALOG = {
    "Seating": {
        "Modern Sofa": "a modern minimalist sofa with clean lines and neutral fabric",
        "Leather Recliner": "a brown leather recliner chair with ottoman",
        "Accent Chair": "a colorful accent chair with geometric patterns",
        "Sectional Sofa": "a large L-shaped sectional sofa in gray fabric",
        "Bean Bag": "a large comfortable bean bag chair",
        "Dining Chairs": "a set of 4 modern dining chairs with wooden legs"
    },
    "Tables": {
        "Coffee Table": "a glass-top coffee table with metal legs",
        "Wooden Coffee Table": "a rustic wooden coffee table with storage",
        "Dining Table": "a modern dining table for 6 people with wooden top",
        "Side Table": "a small round side table with lamp",
        "Console Table": "a long console table against the wall",
        "End Table": "a wooden end table with drawer"
    },
    "Storage": {
        "Bookshelf": "a tall wooden bookshelf filled with books",
        "TV Unit": "a modern TV entertainment unit with storage",
        "Wardrobe": "a large wardrobe with sliding doors",
        "Storage Ottoman": "a fabric storage ottoman that doubles as seating",
        "Floating Shelves": "modern floating wall shelves",
        "Cabinet": "a wooden storage cabinet with doors"
    },
    "Lighting": {
        "Floor Lamp": "a modern arc floor lamp with fabric shade",
        "Table Lamp": "a contemporary table lamp with ceramic base",
        "Pendant Light": "a hanging pendant light over dining area",
        "Chandelier": "an elegant crystal chandelier",
        "LED Strip": "ambient LED strip lighting behind TV",
        "Standing Light": "a minimalist standing light fixture"
    },
    "Bedroom": {
        "Queen Bed": "a modern queen-size bed with upholstered headboard",
        "Nightstand": "a matching wooden nightstand with drawer",
        "Dresser": "a large dresser with mirror",
        "Bench": "a bedroom bench at the foot of the bed",
        "Armoire": "a traditional wooden armoire",
        "Vanity": "a modern vanity table with mirror and lights"
    },
    "Decor": {
        "Area Rug": "a large colorful area rug that defines the seating area",
        "Plant": "a large indoor plant in a decorative pot",
        "Wall Art": "modern abstract wall art in frames",
        "Curtains": "elegant floor-to-ceiling curtains",
        "Mirror": "a large decorative wall mirror",
        "Throw Pillows": "decorative throw pillows on the sofa"
    }
}

class FurnitureVisualizer:
    def __init__(self):
        self.api_key = os.getenv('GEMINI_API_KEY')
        if not self.api_key:
            st.error("Please set your GEMINI_API_KEY in the .env file")
            st.stop()
        
        self.client = genai.Client(api_key=self.api_key)
        self.model_id = "gemini-2.5-flash-image-preview"
    
    def generate_furniture_visualization(self, room_image, furniture_description, placement_instruction):
        """Generate a visualization of furniture placed in the room"""
        
        prompt = f"""
        Take this room image and add {furniture_description} to it. 
        
        Placement instruction: {placement_instruction}
        
        Requirements:
        - Make the furniture look realistic and properly scaled for the room
        - Ensure proper lighting and shadows that match the room's lighting
        - The furniture should blend naturally with the existing room decor
        - Maintain the original room's perspective and style
        - Make it look like a professional interior design visualization
        - Keep the original room elements intact, only add the new furniture
        
        Generate a photorealistic image showing how this furniture would look in the room.
        """
        
        try:
            response = self.client.models.generate_content(
                model=self.model_id,
                contents=[prompt, room_image],
                config=types.GenerateContentConfig(
                    response_modalities=['Image']
                )
            )
            
            # Extract image from response
            for part in response.parts:
                # Try inline_data first (most reliable)
                if hasattr(part, 'inline_data') and part.inline_data and hasattr(part.inline_data, 'data'):
                    try:
                        image_data = part.inline_data.data
                        pil_image = Image.open(io.BytesIO(image_data))
                        return pil_image
                    except Exception:
                        continue
                
                # Fallback to as_image method
                if hasattr(part, 'as_image'):
                    try:
                        genai_image = part.as_image()
                        if genai_image is not None:
                            # Try to get the image data directly
                            if hasattr(genai_image, 'data'):
                                pil_image = Image.open(io.BytesIO(genai_image.data))
                                return pil_image
                    except Exception:
                        continue
            
            return None
            
        except Exception as e:
            st.error(f"Error generating visualization: {str(e)}")
            return None
    
    def save_image(self, image, filename):
        """Save image to local storage"""
        if image:
            image.save(filename)
            return filename
        return None

def main():
    st.set_page_config(
        page_title="Furniture Visualizer",
        page_icon="🏠",
        layout="wide"
    )
    
    st.title("🏠 AI Furniture Visualizer")
    st.subheader("See how furniture will look in your room before you buy!")
    
    # Initialize the visualizer
    if 'visualizer' not in st.session_state:
        st.session_state.visualizer = FurnitureVisualizer()
    
    # Sidebar for furniture selection
    with st.sidebar:
        st.header("🛋️ Furniture Selection")
        
        # Category selection
        category = st.selectbox(
            "Select Furniture Category:",
            list(FURNITURE_CATALOG.keys())
        )
        
        # Furniture item selection
        furniture_item = st.selectbox(
            "Select Furniture:",
            list(FURNITURE_CATALOG[category].keys())
        )
        
        # Get furniture description
        furniture_description = FURNITURE_CATALOG[category][furniture_item]
        
        st.write(f"**Selected:** {furniture_item}")
        st.write(f"*{furniture_description}*")
        
        # Placement instruction
        placement = st.text_area(
            "Placement Instructions:",
            placeholder="e.g., Place the sofa against the far wall, facing the TV area...",
            help="Describe where you want the furniture placed in your room"
        )
        
        # Custom modifications
        st.subheader("🎨 Customize")
        color_preference = st.selectbox(
            "Preferred Color:",
            ["Keep original", "Black", "White", "Brown", "Gray", "Navy", "Beige", "Custom"]
        )
        
        if color_preference == "Custom":
            custom_color = st.text_input("Enter custom color:")
            if custom_color:
                color_preference = custom_color
        
        material_preference = st.selectbox(
            "Preferred Material:",
            ["Keep original", "Leather", "Fabric", "Wood", "Metal", "Glass", "Plastic"]
        )
    
    # Main content area
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.header("📸 Upload Your Room")
        
        uploaded_file = st.file_uploader(
            "Choose a room image...",
            type=['png', 'jpg', 'jpeg'],
            help="Upload a clear photo of your room where you want to place furniture"
        )
        
        if uploaded_file is not None:
            # Display uploaded image
            room_image = Image.open(uploaded_file)
            st.image(room_image, caption="Your Room", width="stretch")
            
            # Store in session state
            st.session_state.room_image = room_image
    
    with col2:
        st.header("🎯 Generated Visualization")
        
        if st.button("🚀 Generate Furniture Visualization", type="primary"):
            if 'room_image' not in st.session_state:
                st.error("Please upload a room image first!")
            elif not placement:
                st.error("Please provide placement instructions!")
            else:
                with st.spinner("Generating your furniture visualization..."):
                    # Modify furniture description based on preferences
                    modified_description = furniture_description
                    
                    if color_preference != "Keep original":
                        modified_description += f" in {color_preference} color"
                    
                    if material_preference != "Keep original":
                        modified_description += f" made of {material_preference.lower()}"
                    
                    # Generate visualization
                    result_image = st.session_state.visualizer.generate_furniture_visualization(
                        st.session_state.room_image,
                        modified_description,
                        placement
                    )
                    
                    if result_image:
                        st.image(result_image, caption="Furniture Visualization", width="stretch")
                        
                        # Save to session state
                        st.session_state.result_image = result_image
                        
                        # Download button
                        img_buffer = io.BytesIO()
                        result_image.save(img_buffer, format='PNG')
                        img_buffer.seek(0)
                        
                        st.download_button(
                            label="📥 Download Visualization",
                            data=img_buffer.getvalue(),
                            file_name=f"furniture_visualization_{furniture_item.lower().replace(' ', '_')}.png",
                            mime="image/png"
                        )
                        
                        # Success message
                        st.success("✅ Visualization generated successfully!")
                        
                        # Feedback section
                        st.subheader("💭 How does it look?")
                        col_a, col_b, col_c = st.columns(3)
                        
                        with col_a:
                            if st.button("😍 Love it!"):
                                st.balloons()
                                st.write("Great choice! This furniture suits your room well.")
                        
                        with col_b:
                            if st.button("🤔 Not sure"):
                                st.write("Try adjusting the placement or choosing a different style.")
                        
                        with col_c:
                            if st.button("❌ Don't like it"):
                                st.write("No problem! Try a different furniture piece or color.")
                    
                    else:
                        st.error("Failed to generate visualization. Please try again.")
        
        # Show previous result if available
        if 'result_image' in st.session_state and not st.button:
            st.image(st.session_state.result_image, caption="Previous Visualization", width="stretch")
    
    # Tips section
    st.markdown("---")
    st.header("💡 Tips for Better Results")
    
    tips_col1, tips_col2 = st.columns(2)
    
    with tips_col1:
        st.markdown("""
        **📸 Room Photo Tips:**
        - Use good lighting (natural light is best)
        - Take photo from a corner to show room perspective
        - Keep the room reasonably tidy
        - Include reference objects for scale
        """)
    
    with tips_col2:
        st.markdown("""
        **🎯 Placement Tips:**
        - Be specific about location ("against the left wall")
        - Mention nearby objects ("next to the window")
        - Consider room flow and accessibility
        - Think about scale and proportions
        """)
    
    # Footer
    st.markdown("---")
    st.markdown(
        "🤖 Powered by Google Gemini 2.5 Flash Image Preview (Nano Banana) | "
        "Built with ❤️ for furniture shopping visualization"
    )

if __name__ == "__main__":
    main()
