# 🏠 AI Furniture Visualizer - Complete Guide

## 🎯 What This App Does

The AI Furniture Visualizer is a powerful app that helps you visualize how furniture will look in your room before making a purchase. Simply upload a photo of your room, select furniture from our catalog, and see a realistic visualization of how it would look in your space.

## ✨ Key Features

- **Upload Room Photos**: Support for PNG, JPG, JPEG formats
- **Extensive Furniture Catalog**: 6 categories with multiple styles each
- **AI-Powered Visualization**: Uses Google's Nano Banana (Gemini 2.5 Flash Image Preview)
- **Customization Options**: Choose colors and materials
- **Realistic Results**: Proper scaling, lighting, and shadows
- **Download Results**: Save visualizations for reference
- **User Feedback**: Rate and save your favorites

## 📋 Furniture Catalog

### 🛋️ Seating

- Modern Sofa, Leather Recliner, Accent Chair
- Sectional Sofa, Bean Bag, Dining Chairs

### 🪑 Tables

- Coffee Table, Wooden Coffee Table, Dining Table
- Side Table, Console Table, End Table

### 📚 Storage

- Bookshelf, TV Unit, Wardrobe
- Storage Ottoman, Floating Shelves, Cabinet

### 💡 Lighting

- Floor Lamp, Table Lamp, Pendant Light
- Chandelier, LED Strip, Standing Light

### 🛏️ Bedroom

- Queen Bed, Nightstand, Dresser
- Bench, Armoire, Vanity

### 🎨 Decor

- Area Rug, Plant, Wall Art
- Curtains, Mirror, Throw Pillows

## 🚀 Quick Start Guide

### 1. Setup (One-time)

```powershell
# Navigate to the app directory
cd "d:\University_Academics\4th_yr\NanoBananaProject\furniture-visualizer-app"

# Run the setup script (installs packages)
setup.bat

# Or manually install:
pip install -r requirements.txt
```

### 2. Get API Key

1. Visit [Google AI Studio](https://aistudio.google.com/apikey)
2. Sign in with Google account
3. Click "Create API key"
4. Copy the generated key

### 3. Configure Environment

Edit the `.env` file and replace the placeholder:

```
GEMINI_API_KEY=your_actual_api_key_here
```

### 4. Run the App

```powershell
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## 🎮 How to Use

### Step 1: Upload Room Photo

- Click "Choose a room image..."
- Select a clear photo of your room
- Best results with good lighting and room perspective

### Step 2: Select Furniture

- Choose category from sidebar (Seating, Tables, etc.)
- Pick specific furniture item
- Customize color and material if desired

### Step 3: Specify Placement

- Describe where you want the furniture placed
- Be specific: "against the far wall, facing the TV"
- Consider room flow and accessibility

### Step 4: Generate Visualization

- Click "Generate Furniture Visualization"
- Wait for AI processing (30-60 seconds)
- View the result with furniture in your room

### Step 5: Evaluate & Download

- Rate the result (Love it, Not sure, Don't like it)
- Download the image for reference
- Try different furniture or placements

## 📸 Photo Tips for Best Results

### Room Photos

- **Lighting**: Use natural daylight when possible
- **Angle**: Take from a corner to show room perspective
- **Clarity**: Ensure photo is sharp and well-lit
- **Scale**: Include reference objects (doors, windows)
- **Preparation**: Keep room reasonably tidy

### Placement Instructions

- **Be Specific**: "Place sofa against the left wall"
- **Reference Points**: "Next to the window", "Facing the TV"
- **Consider Scale**: Think about proportions to room size
- **Traffic Flow**: Ensure placement allows easy movement

## 🛠️ Technical Details

### Architecture

- **Frontend**: Streamlit web interface
- **AI Engine**: Google Gemini 2.5 Flash Image Preview
- **Image Processing**: Pillow (PIL)
- **Configuration**: python-dotenv

### File Structure

```
furniture-visualizer-app/
├── app.py                 # Main Streamlit application
├── demo.py               # Command-line demo script
├── generate_samples.py   # Creates sample room images
├── test_setup.py         # Verifies installation
├── requirements.txt      # Python dependencies
├── .env                  # Environment variables (your API key)
├── setup.bat            # Windows setup script
└── README.md            # This documentation
```

### API Usage

The app uses Google's Gemini API for image generation:

- Model: `gemini-2.5-flash-image-preview`
- Input: Room image + furniture description + placement instructions
- Output: Photorealistic composite image

## 🧪 Testing & Troubleshooting

### Test Installation

```powershell
python test_setup.py
```

### Generate Sample Rooms

```powershell
python generate_samples.py
```

### Run Demo Script

```powershell
python demo.py
```

### Common Issues

**"API key not found"**

- Ensure `.env` file exists with correct API key
- Check that key is not quoted in the file

**"Failed to generate visualization"**

- Check internet connection
- Verify API key is valid
- Try with a simpler placement instruction

**"Package import errors"**

- Run `pip install -r requirements.txt` again
- Check Python version (3.8+ required)

## 💡 Usage Examples

### Example 1: Living Room Sofa

- **Upload**: Living room photo
- **Select**: Seating > Modern Sofa
- **Customize**: Gray color, Fabric material
- **Placement**: "Place against the far wall, facing the TV area"

### Example 2: Bedroom Furniture

- **Upload**: Empty bedroom photo
- **Select**: Bedroom > Queen Bed
- **Customize**: White color, Wood material
- **Placement**: "Center the bed against the back wall, with space for nightstands"

### Example 3: Dining Room Table

- **Upload**: Dining room photo
- **Select**: Tables > Dining Table
- **Customize**: Brown color, Wood material
- **Placement**: "Center in the room with chairs around it"

## 🔮 Future Enhancements

- Multiple furniture pieces in one generation
- Room style matching (modern, traditional, etc.)
- Price integration with furniture stores
- AR/VR preview capabilities
- Social sharing of visualizations
- Room layout optimization suggestions

## 📞 Support

If you encounter issues:

1. Check this documentation
2. Run `test_setup.py` to verify installation
3. Try the `demo.py` script for basic testing
4. Ensure your API key is valid and has credits

## 🏆 Use Cases

- **Home Buyers**: Visualize furniture in new homes
- **Interior Designers**: Present concepts to clients
- **Furniture Shoppers**: Try before you buy
- **Real Estate**: Stage empty properties virtually
- **Rental Furnishing**: Plan temporary setups

---

**Built with ❤️ using Google Gemini Nano Banana technology**
