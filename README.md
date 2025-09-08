# Furniture Visualizer App

An AI-powered furniture visualization app that helps you see how furniture will look in your room before buying.

## Features

- Upload photos of your living room or any room
- Select furniture from a digital catalog (sofas, beds, lights, etc.)
- AI-powered furniture placement using Google's Nano Banana (Gemini 2.5 Flash Image Preview)
- Realistic visualization to help with purchasing decisions

## Setup

1. **Install dependencies:**

```bash
pip install -r requirements.txt
```

2. **Get your Gemini API key:**

   - Visit [Google AI Studio](https://aistudio.google.com/apikey)
   - Create an API key
   - Copy the key

3. **Set up environment variables:**

   - Create a `.env` file in this directory
   - Add your API key: `GEMINI_API_KEY=your_api_key_here`

4. **Run the app:**

```bash
streamlit run app.py
```

## How to Use

1. **Upload Room Photo**: Upload a clear photo of your room
2. **Select Furniture**: Choose furniture type and style from the menu
3. **Specify Placement**: Describe where you want the furniture placed
4. **Generate Visualization**: Click to see the furniture in your room
5. **Download Result**: Save the visualization for reference

## Technical Details

- Built with Streamlit for the web interface
- Uses Google Gemini 2.5 Flash Image Preview for AI image generation
- Supports multiple furniture categories and styles
- Generates photorealistic composite images

## Furniture Categories

- **Seating**: Sofas, chairs, recliners, ottomans
- **Tables**: Coffee tables, dining tables, side tables
- **Storage**: Bookshelves, wardrobes, cabinets
- **Lighting**: Floor lamps, table lamps, ceiling lights
- **Bedroom**: Beds, nightstands, dressers
- **Decor**: Plants, artwork, rugs, curtains
