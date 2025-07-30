'use client'

import React, { useState, useEffect } from 'react'
import { Upload, ArrowRight, Home, HelpCircle, List, FileText } from 'lucide-react'

interface Invoice {
  id: string
  filename: string
  uploaded_at: string
  status: 'Pending' | 'Approved' | 'Rejected'
  data: any
}

export default function HomePage() {
  const [isUploading, setIsUploading] = useState(false)
  const [uploadedFile, setUploadedFile] = useState<File | null>(null)
  const [extractedInvoice, setExtractedInvoice] = useState<Invoice | null>(null)
  const [invoices, setInvoices] = useState<Invoice[]>([])
  const [activeTab, setActiveTab] = useState<'upload' | 'list'>('upload')

  // Fetch existing invoices on component mount
  useEffect(() => {
    fetchInvoices()
  }, [])

  const fetchInvoices = async () => {
    try {
      const response = await fetch('http://localhost:8000/invoices')
      if (response.ok) {
        const data = await response.json()
        setInvoices(data)
      }
    } catch (error) {
      console.error('Error fetching invoices:', error)
    }
  }

  const handleFileUpload = async (event: React.ChangeEvent<HTMLInputElement>) => {
    const file = event.target.files?.[0]
    if (!file) return

    setUploadedFile(file)
    setIsUploading(true)

    try {
      const formData = new FormData()
      formData.append('file', file)

      const response = await fetch('http://localhost:8000/extract-invoice', {
        method: 'POST',
        body: formData,
      })

      if (response.ok) {
        const result = await response.json()
        setExtractedInvoice(result)
        // Refresh the invoice list
        fetchInvoices()
      } else {
        console.error('Upload failed')
      }
    } catch (error) {
      console.error('Error uploading file:', error)
    } finally {
      setIsUploading(false)
    }
  }

  const getStatusColor = (status: string) => {
    switch (status) {
      case 'Approved':
        return 'bg-green-100 text-green-800'
      case 'Rejected':
        return 'bg-red-100 text-red-800'
      default:
        return 'bg-yellow-100 text-yellow-800'
    }
  }

  const getStatusDot = (status: string) => {
    switch (status) {
      case 'Approved':
        return 'bg-green-500'
      case 'Rejected':
        return 'bg-red-500'
      default:
        return 'bg-yellow-500'
    }
  }

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Header */}
      <header className="bg-white border-b border-gray-200">
        <div className="flex items-center justify-between px-6 py-4">
          <div className="flex items-center space-x-2">
            <div className="w-8 h-8 bg-blue-500 rounded-lg flex items-center justify-center">
              <Home className="w-5 h-5 text-white" />
            </div>
            <span className="text-xl font-semibold text-gray-900">Finvoice Guard</span>
          </div>
          
          <div className="flex items-center space-x-4">
            <HelpCircle className="w-5 h-5 text-gray-500" />
            <div className="flex items-center space-x-2">
              <div className="w-8 h-8 bg-green-500 rounded-lg flex items-center justify-center">
                <Home className="w-4 h-4 text-white" />
              </div>
              <span className="text-sm font-medium text-gray-700">TECMOLDDY</span>
            </div>
          </div>
        </div>

        {/* Tabs */}
        <div className="px-6">
          <div className="flex space-x-8">
            <button
              onClick={() => setActiveTab('upload')}
              className={`flex items-center space-x-2 py-3 px-1 border-b-2 font-medium text-sm ${
                activeTab === 'upload'
                  ? 'border-blue-500 text-blue-600'
                  : 'border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300'
              }`}
            >
              <Upload className="w-4 h-4" />
              <span>Upload Invoice</span>
            </button>
            <button
              onClick={() => setActiveTab('list')}
              className={`flex items-center space-x-2 py-3 px-1 border-b-2 font-medium text-sm ${
                activeTab === 'list'
                  ? 'border-blue-500 text-blue-600'
                  : 'border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300'
              }`}
            >
              <List className="w-4 h-4" />
              <span>Invoice List</span>
            </button>
          </div>
        </div>
      </header>

      {/* Main Content */}
      <main className="max-w-7xl mx-auto px-6 py-8">
        {activeTab === 'upload' ? (
          <div className="text-center">
            <h1 className="text-4xl font-bold text-gray-900 mb-6">
              Where insight begins.
            </h1>
            
            <p className="text-xl text-gray-600 mb-12 max-w-3xl mx-auto">
              An AI-powered application that helps organizations prevent financial leakage and fraud by transforming how vendor invoices are reviewed, analyzed, and approved.
            </p>

            {/* Upload Area */}
            <div className="max-w-2xl mx-auto">
              <div className="border-2 border-dashed border-gray-300 rounded-lg p-8 hover:border-blue-400 transition-colors bg-white">
                <div className="flex flex-col items-center space-y-4">
                  <Upload className="w-12 h-12 text-gray-400" />
                  <div className="text-center">
                    <p className="text-lg font-medium text-gray-900 mb-2">
                      Upload Invoice Image
                    </p>
                    <p className="text-gray-500 mb-4">
                      Drag and drop your invoice image here, or click to browse
                    </p>
                  </div>
                  
                  <label className="cursor-pointer">
                    <input
                      type="file"
                      accept="image/*"
                      onChange={handleFileUpload}
                      className="hidden"
                      disabled={isUploading}
                    />
                    <div className="flex items-center space-x-2 bg-blue-500 text-white px-6 py-3 rounded-lg hover:bg-blue-600 transition-colors">
                      <span>{isUploading ? 'Processing...' : 'Choose File'}</span>
                      <ArrowRight className="w-4 h-4" />
                    </div>
                  </label>
                </div>
              </div>
            </div>

            {/* Extracted Invoice Display */}
            {extractedInvoice && (
              <div className="mt-12 max-w-6xl mx-auto">
                <h2 className="text-2xl font-bold text-gray-900 mb-6">Extracted Invoice</h2>
                <div className="bg-white border border-gray-200 rounded-lg p-6 shadow-sm">
                  <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <div>
                      <h3 className="text-lg font-semibold mb-4 text-gray-900">Invoice Details</h3>
                      <div className="space-y-2">
                        <p className="text-gray-700"><span className="font-medium text-gray-900">Invoice Number:</span> {extractedInvoice.data.invoice_number}</p>
                        <p className="text-gray-700"><span className="font-medium text-gray-900">Issue Date:</span> {extractedInvoice.data.issue_date}</p>
                        <p className="text-gray-700"><span className="font-medium text-gray-900">Status:</span> 
                          <span className={`ml-2 px-2 py-1 rounded-full text-xs font-medium ${getStatusColor(extractedInvoice.status)}`}>
                            {extractedInvoice.status}
                          </span>
                        </p>
                      </div>
                    </div>
                    
                    <div>
                      <h3 className="text-lg font-semibold mb-4 text-gray-900">Vendor Information</h3>
                      <div className="space-y-2">
                        <p className="text-gray-700"><span className="font-medium text-gray-900">Name:</span> {extractedInvoice.data.seller.name}</p>
                        <p className="text-gray-700"><span className="font-medium text-gray-900">Address:</span> {extractedInvoice.data.seller.address}</p>
                        <p className="text-gray-700"><span className="font-medium text-gray-900">Tax ID:</span> {extractedInvoice.data.seller.tax_id}</p>
                      </div>
                    </div>
                  </div>

                  <div className="mt-6">
                    <h3 className="text-lg font-semibold mb-4 text-gray-900">Line Items</h3>
                    <div className="overflow-x-auto">
                      <table className="min-w-full divide-y divide-gray-200">
                        <thead className="bg-gray-50">
                          <tr>
                            <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Item</th>
                            <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Description</th>
                            <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Qty</th>
                            <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Unit Price</th>
                            <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Total</th>
                          </tr>
                        </thead>
                        <tbody className="bg-white divide-y divide-gray-200">
                          {extractedInvoice.data.items.map((item: any, index: number) => (
                            <tr key={index}>
                              <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-900">{item.item_number}</td>
                              <td className="px-6 py-4 text-sm text-gray-900">{item.description}</td>
                              <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-900">{item.quantity}</td>
                              <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-900">${item.net_price.toFixed(2)}</td>
                              <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-900">${item.net_worth.toFixed(2)}</td>
                            </tr>
                          ))}
                        </tbody>
                      </table>
                    </div>
                  </div>

                  <div className="mt-6 text-right">
                    <div className="text-lg font-semibold text-gray-900">
                      Total: ${extractedInvoice.data.summary.total_gross_worth.toFixed(2)}
                    </div>
                  </div>
                </div>
              </div>
            )}
          </div>
        ) : (
          <div>
            <div className="flex items-center justify-between mb-6">
              <h1 className="text-3xl font-bold text-gray-900">Invoice List</h1>
              <button
                onClick={() => setActiveTab('upload')}
                className="flex items-center space-x-2 bg-blue-500 text-white px-4 py-2 rounded-lg hover:bg-blue-600 transition-colors"
              >
                <Upload className="w-4 h-4" />
                <span>Upload New</span>
              </button>
            </div>

            {invoices.length === 0 ? (
              <div className="text-center py-12">
                <FileText className="w-12 h-12 text-gray-400 mx-auto mb-4" />
                <h3 className="text-lg font-medium text-gray-900 mb-2">No invoices yet</h3>
                <p className="text-gray-500 mb-4">Upload your first invoice to get started</p>
                <button
                  onClick={() => setActiveTab('upload')}
                  className="bg-blue-500 text-white px-4 py-2 rounded-lg hover:bg-blue-600 transition-colors"
                >
                  Upload Invoice
                </button>
              </div>
            ) : (
              <div className="bg-white shadow-sm rounded-lg overflow-hidden">
                <table className="min-w-full divide-y divide-gray-200">
                  <thead className="bg-gray-50">
                    <tr>
                      <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Invoice ID</th>
                      <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Vendor</th>
                      <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Amount</th>
                      <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Status</th>
                      <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Date</th>
                      <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Actions</th>
                    </tr>
                  </thead>
                  <tbody className="bg-white divide-y divide-gray-200">
                    {invoices.map((invoice) => (
                      <tr key={invoice.id} className="hover:bg-gray-50">
                        <td className="px-6 py-4 whitespace-nowrap">
                          <div className="flex items-center">
                            <div className={`w-2 h-2 rounded-full mr-3 ${getStatusDot(invoice.status)}`}></div>
                            <span className="text-sm font-medium text-gray-900">{invoice.id}</span>
                          </div>
                        </td>
                        <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
                          {invoice.data?.seller?.name || 'N/A'}
                        </td>
                        <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
                          ${invoice.data?.summary?.total_gross_worth?.toFixed(2) || '0.00'}
                        </td>
                        <td className="px-6 py-4 whitespace-nowrap">
                          <span className={`px-2 py-1 text-xs font-medium rounded-full ${getStatusColor(invoice.status)}`}>
                            {invoice.status}
                          </span>
                        </td>
                        <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
                          {invoice.uploaded_at}
                        </td>
                        <td className="px-6 py-4 whitespace-nowrap text-sm font-medium">
                          <button
                            onClick={() => {
                              setExtractedInvoice(invoice)
                              setActiveTab('upload')
                            }}
                            className="text-blue-600 hover:text-blue-900"
                          >
                            View
                          </button>
                        </td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            )}
          </div>
        )}
      </main>
    </div>
  )
} 