# Finvoice Guard

An AI-powered invoice management application that helps organizations prevent financial leakage and fraud by transforming how vendor invoices are reviewed, analyzed, and approved.

## Features

- Upload invoice images for AI-powered extraction
- View extracted invoice data in a clean, organized format
- Real-time invoice processing with Llama Cloud Services
- Modern, responsive UI built with Next.js and Tailwind CSS

## Project Structure

```
nextjs_app/
├── api/                    # FastAPI backend
│   ├── main.py            # FastAPI server with extraction endpoints
│   └── requirements.txt   # Python dependencies
├── app/                   # Next.js frontend
│   ├── globals.css        # Global styles
│   ├── layout.tsx         # Root layout
│   └── page.tsx           # Main page component
├── package.json           # Node.js dependencies
├── tailwind.config.js     # Tailwind CSS configuration
├── tsconfig.json          # TypeScript configuration
└── README.md             # This file
```

## Setup Instructions

### Prerequisites

- Python 3.8+
- Node.js 18+
- npm, yarn, or pnpm

### Backend Setup (FastAPI)

1. Navigate to the API directory:
   ```bash
   cd nextjs_app/api
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up your environment variables (create a `.env` file):
   ```
   # Add your Llama Cloud API credentials here
   LLAMA_CLOUD_API_KEY=your_api_key_here
   ```

5. Start the FastAPI server:
   ```bash
   python main.py
   ```

The API will be available at `http://localhost:8000`

### Frontend Setup (Next.js)

1. Navigate to the Next.js app directory:
   ```bash
   cd nextjs_app
   ```

2. Install Node.js dependencies (choose your preferred package manager):
   ```bash
   # Using npm
   npm install
   
   # Using yarn
   yarn install
   
   # Using pnpm
   pnpm install
   ```

3. Start the development server:
   ```bash
   # Using npm
   npm run dev
   
   # Using yarn
   yarn dev
   
   # Using pnpm
   pnpm dev
   ```

The application will be available at `http://localhost:3000`

### Quick Start (Both Services)

You can also use the provided startup script which automatically detects your package manager:

```bash
cd nextjs_app
chmod +x start.sh
./start.sh
```

This will start both the FastAPI backend and Next.js frontend simultaneously.

## Usage

1. Open your browser and navigate to `http://localhost:3000`
2. You'll see the Finvoice Guard landing page with the upload interface
3. Click "Choose File" to select an invoice image
4. The image will be processed by the AI extraction service
5. View the extracted invoice data displayed in a clean, organized format

## API Endpoints

- `POST /extract-invoice` - Upload and extract invoice data from an image
- `GET /invoices` - Get all extracted invoices
- `GET /invoices/{invoice_id}` - Get a specific invoice by ID
- `PUT /invoices/{invoice_id}/status` - Update invoice status

## Invoice Schema

The application extracts the following data from invoice images:

- Invoice number and issue date
- Seller information (name, address, tax ID, IBAN)
- Client information (name, address, tax ID)
- Line items with quantities, prices, and VAT details
- Summary totals (net worth, VAT, gross worth)

## Technologies Used

- **Backend**: FastAPI, Python, Llama Cloud Services
- **Frontend**: Next.js 14, React, TypeScript, Tailwind CSS
- **Icons**: Lucide React
- **Styling**: Tailwind CSS

## Development

- The backend uses in-memory storage for simplicity. In production, consider using a database.
- The frontend is built with Next.js App Router for modern React development.
- Tailwind CSS provides utility-first styling for rapid UI development. 