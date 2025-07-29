# Invoice Extraction Streamlit App

A simple Streamlit application that allows users to upload invoice images and extract structured data using LlamaCloud's extraction agent.

## Features

- 📄 Upload invoice images (JPG, JPEG, PNG, BMP, TIFF)
- 🔍 Automatic data extraction using LlamaCloud's kaggle_invoice_agent
- 📊 Display extracted data in both JSON and formatted views
- 🎨 Clean, modern UI with progress indicators

## Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up environment variables:**
   Create a `.env` file in the project root with your LlamaCloud API credentials:
   ```
   LLAMA_CLOUD_API_KEY=your_api_key_here
   ```

3. **Run the app:**
   ```bash
   streamlit run app.py
   ```

4. **Open your browser:**
   The app will be available at `http://localhost:8501`

## Usage

1. Upload an invoice image using the file uploader
2. Click "Extract Data" to run the extraction
3. View the extracted data in both JSON and formatted formats
4. The sidebar shows configuration details and app information

## Configuration

The app uses the following configuration (from `sample.py`):
- **Project ID:** `2fef999e-1073-40e6-aeb3-1f3c0e64d99b`
- **Organization ID:** `43b88c8f-e488-46f6-9013-698e3d2e374a`
- **Agent:** `kaggle_invoice_agent`

## File Structure

```
jerry_invoice_streamlit/
├── app.py              # Main Streamlit application
├── sample.py           # Original sample code
├── requirements.txt    # Python dependencies
├── README.md          # This file
└── .env               # Environment variables (create this)
```

## Troubleshooting

- **API Key Issues:** Make sure your `.env` file contains the correct `LLAMA_CLOUD_API_KEY`
- **Import Errors:** Ensure all dependencies are installed with `pip install -r requirements.txt`
- **File Upload Issues:** Check that your image file is in a supported format 