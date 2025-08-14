# Invoice Processing App - Vibe Coding a Web App

This repository demonstrates how to "vibe code" a full-stack invoice processing application using Cursor/Claude Code from a simple starting file. This showcases building a complete Streamlit application with LlamaCloud's document extraction capabilities.

## 🎯 What This Repository Is Capable Of

This repository provides a complete end-to-end solution for building intelligent document processing applications:

1. **Vibe Coding Templates to Create Full Web Applications**: Provides comprehensive prompts that can be used alongside coding assistants like cursor to one-shot transform simple scripts into production web applications
2. **LlamaCloud Integration**: Automatically creates and configures LlamaExtract extraction agents using predefined Pydantic schemas for structured data extraction
7. **Sample scripts**: Sample scripts that can be used as context for coding assistants while generating new streamlit apps!

## 🚀 Quick Start - Vibe Coding Your Own App

This repository demonstrates **vibe coding** - rapidly building applications through iterative AI-assisted development. The goal is to transform a simple script into a full-featured application using Cursor/Claude Code.

### Prerequisites
- Python 3.11+
- LlamaCloud account and API key ([Get one here](https://cloud.llamaindex.ai/))

### Setup Process

#### 1. **Clone and Install**
```bash
git clone <your-repo-url>
cd invoice-extraction-vibe-coding
pip install -r requirements.txt
```

#### 2. **Set Up LlamaCloud**
1. Go to [LlamaCloud](https://cloud.llamaindex.ai/) and log in
2. Create a new project and note your `project_id` and `organization_id`
3. Get your API key from your account settings

#### 3. **Configure Environment**
Copy the template and add your credentials:
```bash
cp .env.template .env
```
Then edit `.env` with your LlamaCloud credentials:
```env
LLAMA_CLOUD_API_KEY=your_actual_api_key
LLAMA_CLOUD_PROJECT_ID=your_actual_project_id
LLAMA_CLOUD_ORGANIZATION_ID=your_actual_organization_id
LLAMA_CLOUD_AGENT_NAME=invoice_extraction_agent
```

#### 4. **Create Extraction Agent**
```bash
python create_agent.py
```
This automatically creates an extraction agent in LlamaCloud using the invoice schema from `sample_data/sample_schema.py`.

#### 5. **Test Your Setup**
```bash
python sample.py
```
This validates your configuration and runs extraction on the sample invoice. You should see structured JSON output.

#### 6. **Start Vibe Coding!**
Now comes the fun part - use the `cursor_prompt.md` template to transform `sample.py` into a full application:

1. Open your project in Cursor or Claude Code
2. Copy the prompt from `cursor_prompt.md`
3. Start iterating: "Transform this simple script into a professional Streamlit app with..."
4. Build features incrementally through natural language prompts

#### 7. **Compare Your Result**
When you're done vibe coding, compare your creation with our `app.py` to see different approaches!

## 📁 Project Structure

```
invoice-extraction-vibe-coding/
├── app.py                      # Full-featured Streamlit application (generated)
├── sample.py                   # Starting point - simple extraction script
├── create_agent.py            # Script to create LlamaCloud extraction agent
├── .env.template              # Environment variables template
├── requirements.txt           # Python dependencies
├── cursor_prompt.md           # Cursor prompt template for vibe coding
└── sample_data/               # Sample invoice data
    ├── batch1-0274.jpg       # Sample invoice image
    └── sample_schema.py      # Pydantic models for data structure
```

## 🎯 What This Demonstrates

### From Simple Script to Full App
- **Starting Point**: `sample.py` - A basic 20-line script that calls LlamaCloud extraction
- **End Result**: `app.py` - A fully-featured Streamlit application with:
  - Professional UI with custom CSS
  - File upload functionality
  - Real-time data extraction
  - Structured data display
  - Invoice history tracking
  - Status indicators and metrics

### LlamaCloud Integration
- Document parsing and extraction using LlamaExtract
- Structured data output using predefined schemas
- Integration with kaggle_invoice_agent

## 🛠 Vibe Coding with the Prompt Template

This project demonstrates **vibe coding** - rapidly building applications through conversational AI development.

### Start with `cursor_prompt.md`
The `cursor_prompt.md` file contains a comprehensive prompt template that can potentially **one-shot** the entire application transformation:

1. **Copy the main prompt** from `cursor_prompt.md`
2. **Paste it into Cursor/Claude Code** with your `sample.py` file open
3. **Watch the magic happen** - the AI may build the entire Streamlit app in one go!

### The Vibe Coding Process:
- **Start Simple**: `sample.py` - a working 20-line script
- **Use Natural Language**: Describe what you want, not how to build it
- **Iterate if Needed**: Add features through follow-up prompts
- **Build Incrementally**: Test and refine each addition

### Why the Template Works:
- **Comprehensive Scope**: Covers UI, functionality, and user experience
- **Clear Context**: References your actual files and sample data
- **Specific Examples**: Shows exactly what features to build
- **Production-Ready**: Asks for professional-quality output

Try the full prompt first - you might be surprised how much gets built in a single interaction!

## 🔧 Features

### Current Application (`app.py`)
- 📄 **Multi-format Support**: JPG, JPEG, PNG, BMP, TIFF
- 🎨 **Professional UI**: Custom CSS styling and responsive design
- 📊 **Data Visualization**: Structured invoice data display
- 📈 **Analytics**: Processing metrics and status tracking
- 🔄 **Real-time Processing**: Live extraction with progress indicators
- 💾 **Session Storage**: Invoice history within session

### Data Schema
The application extracts structured invoice data including:
- Invoice metadata (number, date)
- Seller and client information
- Line items with pricing details
- VAT calculations and summaries
- Total amounts

See `sample_data/sample_schema.py` for the complete Pydantic model definitions.

## 📝 Usage

1. **Upload Invoice**: Drag and drop or select an invoice image
2. **Extract Data**: Click the extraction button to process with LlamaCloud
3. **View Results**: See structured data in formatted tables and JSON
4. **Track History**: View processed invoices in the history tab

## 🔑 Configuration

Update these values in your application for your own LlamaCloud setup:
```python
project_id = "your-project-id"
organization_id = "your-organization-id"
agent_name = "your-agent-name"
```

## 🐛 Troubleshooting

### Common Issues
- **API Key**: Ensure your LlamaCloud API key is valid and in `.env`
- **Dependencies**: Run `pip install -r requirements.txt`
- **File Formats**: Only image formats are supported
- **File Size**: Keep images under 10MB for best performance

## 🤝 Contributing

This is an educational example demonstrating the vibe coding approach. Feel free to:
- Fork and modify for your use case
- Share improvements and variations
- Use as a starting point for your own projects

## 📄 License

Open source - use freely for learning and development.

---

**Built with ❤️ using LlamaIndex, LlamaCloud, and the power of vibe coding with Cursor/Claude Code!** 