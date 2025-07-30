from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import os
import tempfile
from typing import List, Dict, Any
import json
from dotenv import load_dotenv
from llama_cloud_services import LlamaExtract
from llama_cloud.core.api_error import ApiError

# Load environment variables
load_dotenv()

app = FastAPI(title="Finvoice Guard API", version="1.0.0")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Next.js app
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize the extraction agent
project_id = "2fef999e-1073-40e6-aeb3-1f3c0e64d99b"
organization_id = "43b88c8f-e488-46f6-9013-698e3d2e374a"

extract = LlamaExtract(
    show_progress=False, 
    check_interval=5,
    project_id=project_id,
    organization_id=organization_id
)

agent = extract.get_agent(name="kaggle_invoice_agent")

# In-memory storage for extracted invoices (in production, use a database)
extracted_invoices: List[Dict[str, Any]] = []

@app.get("/")
async def root():
    return {"message": "Finvoice Guard API is running"}

@app.post("/extract-invoice")
async def extract_invoice(file: UploadFile = File(...)):
    """
    Extract invoice data from uploaded image
    """
    try:
        # Validate file type
        if not file.content_type.startswith('image/'):
            raise HTTPException(status_code=400, detail="File must be an image")
        
        # Save uploaded file temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix='.jpg') as temp_file:
            content = await file.read()
            temp_file.write(content)
            temp_file_path = temp_file.name
        
        try:
            # Extract invoice data
            result = agent.extract(temp_file_path)
            extracted_data = result.data
            
            # Add metadata
            invoice_with_metadata = {
                "id": f"INV-{len(extracted_invoices) + 1:03d}",
                "filename": file.filename,
                "uploaded_at": "2024-01-15",  # In production, use actual timestamp
                "status": "Pending",
                "data": extracted_data
            }
            
            # Store in memory
            extracted_invoices.append(invoice_with_metadata)
            
            return JSONResponse(content=invoice_with_metadata)
            
        finally:
            # Clean up temporary file
            os.unlink(temp_file_path)
            
    except ApiError as e:
        raise HTTPException(status_code=500, detail=f"Extraction failed: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Server error: {str(e)}")

@app.get("/invoices")
async def get_invoices():
    """
    Get all extracted invoices
    """
    return extracted_invoices

@app.get("/invoices/{invoice_id}")
async def get_invoice(invoice_id: str):
    """
    Get a specific invoice by ID
    """
    for invoice in extracted_invoices:
        if invoice["id"] == invoice_id:
            return invoice
    raise HTTPException(status_code=404, detail="Invoice not found")

@app.put("/invoices/{invoice_id}/status")
async def update_invoice_status(invoice_id: str, status: str):
    """
    Update invoice status (Approved, Rejected, Pending)
    """
    for invoice in extracted_invoices:
        if invoice["id"] == invoice_id:
            invoice["status"] = status
            return invoice
    raise HTTPException(status_code=404, detail="Invoice not found")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 