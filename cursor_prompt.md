# Cursor Prompt for Invoice Processing App

Use this prompt to transform the simple `sample.py` script into a full-featured Streamlit invoice processing application.

## Main Prompt

```
I have a simple piece of sample code (sample.py) that initializes a LlamaCloud extraction agent and runs extraction over a sample invoice image. I want to transform this into a professional Streamlit web application.

Here's what I'm starting with:
- sample.py: Basic extraction script using LlamaExtract with kaggle_invoice_agent
- sample_data/batch1-0274.jpg: Sample invoice image for testing
- sample_data/sample_schema.py: Pydantic models defining the expected invoice data structure

Transform this into a comprehensive Streamlit app with:

## Core Features
1. **File Upload Interface**
   - Support multiple image formats (JPG, JPEG, PNG, BMP, TIFF)
   - Drag-and-drop functionality
   - Image preview before processing
   - File validation and size limits

2. **Data Extraction & Display**
   - Use the same LlamaExtract agent from sample.py
   - Process uploaded invoices in real-time
   - Display extracted data using the schema structure from sample_schema.py
   - Show both formatted view and raw JSON

3. **Professional UI Design**
   - Modern, clean interface with custom CSS
   - Responsive layout with proper spacing
   - Professional color scheme and typography
   - Loading states and progress indicators

## Data Presentation
Based on the sample_schema.py structure, display:
- Invoice overview (number, date, status)
- Seller and client information in organized cards
- Line items in a structured table
- VAT summary with calculations
- Total amounts prominently displayed

## Additional Features
- Session-based invoice history
- Processing status and metrics in sidebar
- Error handling with user-friendly messages
- System status indicators
- Usage statistics and tips

## Technical Requirements
- Use the same project_id and organization_id from sample.py
- Maintain the kaggle_invoice_agent configuration
- Include proper environment variable handling for API keys
- Add comprehensive error handling for API failures

Make it production-ready with clean code structure, proper documentation, and professional presentation. The app should feel like a commercial invoice processing tool while maintaining the simplicity of the original extraction logic.

Test with the provided sample_data/batch1-0274.jpg to ensure everything works correctly.
```

## Follow-up Enhancement Prompts

### UI Polish
```
Enhance the visual design with:
- Custom CSS for a more professional look
- Better color scheme (consider invoice/business themes)
- Improved typography and spacing
- Status badges and progress indicators
- Responsive design for different screen sizes
```

### Feature Expansion
```
Add these capabilities:
- Export results to JSON/CSV
- Batch processing of multiple invoices
- Invoice data validation against schema
- Search and filter processed invoices
- Comparison between different invoices
```

### User Experience
```
Improve the user experience with:
- Better error messages and recovery options
- Helpful tooltips and guidance
- Keyboard shortcuts and accessibility
- Auto-save of processing results
- Undo/redo functionality where applicable
```

## Key Context Files

When using this prompt, make sure to include:
- `sample.py` - The starting extraction script
- `sample_data/sample_schema.py` - Pydantic models for data structure
- `sample_data/batch1-0274.jpg` - Test invoice image
- Current `requirements.txt` - Dependencies list

## Expected Transformation

**From:** 20-line extraction script
**To:** Full-featured web application with professional UI, comprehensive functionality, file handling, data visualization, and production-ready code quality.

The result should demonstrate the power of "vibe coding" - rapidly building complex applications through iterative AI-assisted development.