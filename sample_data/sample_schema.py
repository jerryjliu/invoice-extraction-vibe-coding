from pydantic import BaseModel
from typing import List
from datetime import datetime


class Seller(BaseModel):
    """Information about the seller."""
    name: str
    address: str
    tax_id: str
    iban: str


class Client(BaseModel):
    """Information about the client."""
    name: str
    address: str
    tax_id: str


class Item(BaseModel):
    """Individual item in the invoice."""
    item_number: str
    description: str
    quantity: float
    unit_of_measure: str
    net_price: float
    net_worth: float
    vat_percentage: str
    gross_worth: float


class VatSummaryEntry(BaseModel):
    """VAT summary for a specific VAT percentage."""
    vat_percentage: str
    net_worth: float
    vat: float
    gross_worth: float


class Summary(BaseModel):
    """Summary of the invoice amounts."""
    vat_summary: List[VatSummaryEntry]
    total_net_worth: float
    total_vat: float
    total_gross_worth: float


class Invoice(BaseModel):
    """Complete invoice model."""
    invoice_number: str
    issue_date: str  # Formatted as MM/DD/YYYY
    seller: Seller
    client: Client
    items: List[Item]
    summary: Summary