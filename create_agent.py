"""
Create LlamaCloud extraction agent for invoice processing.

Run this script to automatically create an extraction agent with the invoice schema
before testing with sample.py or building your Streamlit app.
"""

import os
import sys
from dotenv import load_dotenv
from llama_cloud_services import LlamaExtract
from llama_cloud.core.api_error import ApiError
from sample_data.sample_schema import Invoice

# Load environment variables
load_dotenv()

def create_invoice_agent():
    """Create or update the invoice extraction agent."""
    
    # Get configuration
    project_id = os.getenv("LLAMA_CLOUD_PROJECT_ID")
    organization_id = os.getenv("LLAMA_CLOUD_ORGANIZATION_ID")
    agent_name = os.getenv("LLAMA_CLOUD_AGENT_NAME", "invoice_extraction_agent")
    
    # Validate configuration
    if not project_id or project_id == "your-project-id-here":
        print("❌ Error: LLAMA_CLOUD_PROJECT_ID not configured!")
        print("Please set your project ID in the .env file")
        return False
        
    if not organization_id or organization_id == "your-organization-id-here":
        print("❌ Error: LLAMA_CLOUD_ORGANIZATION_ID not configured!")
        print("Please set your organization ID in the .env file")
        return False
    
    try:
        print("🚀 Initializing LlamaCloud extraction service...")
        
        # Initialize LlamaExtract
        extract = LlamaExtract(
            show_progress=True,
            check_interval=5,
            project_id=project_id,
            organization_id=organization_id
        )
        
        print(f"✅ Connected to LlamaCloud")
        print(f"📋 Project ID: {project_id}")
        print(f"🏢 Organization ID: {organization_id}")
        print(f"🤖 Agent name: {agent_name}")
        
        # Check if agent already exists
        try:
            existing_agent = extract.get_agent(name=agent_name)
            if existing_agent:
                print(f"✅ Agent '{agent_name}' already exists!")
                print(f"🤖 Agent ID: {existing_agent.id}")
                print("📝 You can use this existing agent for extraction.")
                return True
        except ApiError as e:
            if e.status_code == 404:
                print(f"📝 Agent '{agent_name}' does not exist, creating new one...")
            else:
                raise
        
        # Create new agent with invoice schema
        print("🔧 Creating new extraction agent...")
        print("📊 Using invoice schema from sample_data/sample_schema.py")
        
        agent = extract.create_agent(
            name=agent_name, 
            data_schema=Invoice
        )
        
        print("🎉 Success! Extraction agent created successfully!")
        print(f"🤖 Agent ID: {agent.id}")
        print(f"📝 Agent Name: {agent.name}")
        
        print("\n📋 Schema Summary:")
        print("  • Invoice metadata (number, date)")
        print("  • Seller and client information")
        print("  • Line items with pricing details")
        print("  • VAT calculations and summaries")
        print("  • Total amounts")
        
        print(f"\n✅ Setup complete! Your agent '{agent_name}' is ready to use.")
        print("\n🚀 Next steps:")
        print("1. Run 'python sample.py' to test extraction")
        print("2. Use 'cursor_prompt.md' to build your Streamlit app")
        
        return True
        
    except Exception as e:
        print(f"❌ Error creating agent: {e}")
        print("\n🔧 Troubleshooting:")
        print("1. Check your .env file has correct credentials")
        print("2. Verify your LlamaCloud account has necessary permissions")
        print("3. Ensure you have a valid project and organization setup")
        return False

def main():
    """Main function."""
    print("🔨 LlamaCloud Invoice Extraction Agent Setup")
    print("=" * 50)
    
    # Check if .env file exists
    if not os.path.exists(".env"):
        print("❌ No .env file found!")
        print("\nPlease create a .env file with:")
        print("LLAMA_CLOUD_API_KEY=your_api_key_here")
        print("LLAMA_CLOUD_PROJECT_ID=your_project_id_here")
        print("LLAMA_CLOUD_ORGANIZATION_ID=your_organization_id_here")
        print("LLAMA_CLOUD_AGENT_NAME=invoice_extraction_agent")
        sys.exit(1)
    
    # Create agent
    success = create_invoice_agent()
    
    if success:
        sys.exit(0)
    else:
        sys.exit(1)

if __name__ == "__main__":
    main()