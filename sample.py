"""
Simple invoice extraction script using LlamaCloud.

This is the starting point for vibe coding a full Streamlit application.
Configure your LlamaCloud credentials and run this script to test extraction
before building the full web application.
"""

import os
import json
from dotenv import load_dotenv
from llama_cloud_services import LlamaExtract
from llama_cloud.core.api_error import ApiError

# Load environment variables
load_dotenv()

# Configuration - Update these with your LlamaCloud details
PROJECT_ID = os.getenv("LLAMA_CLOUD_PROJECT_ID", "your-project-id-here")
ORGANIZATION_ID = os.getenv("LLAMA_CLOUD_ORGANIZATION_ID", "your-organization-id-here")
AGENT_NAME = os.getenv("LLAMA_CLOUD_AGENT_NAME", "your-agent-name-here")

# Sample image path
SAMPLE_IMAGE = "sample_data/batch1-0274.jpg"

def main():
    """Run invoice extraction on sample image."""
    
    # Validate configuration
    if PROJECT_ID == "your-project-id-here" or ORGANIZATION_ID == "your-organization-id-here":
        print("❌ Please configure your LlamaCloud credentials!")
        print("Update your .env file with:")
        print("LLAMA_CLOUD_PROJECT_ID=your-actual-project-id")
        print("LLAMA_CLOUD_ORGANIZATION_ID=your-actual-organization-id")
        print("LLAMA_CLOUD_AGENT_NAME=your-actual-agent-name")
        return
    
    try:
        print("🚀 Initializing LlamaCloud extraction agent...")
        
        # Initialize the extraction service
        extract = LlamaExtract(
            show_progress=True,  # Show progress for better UX
            check_interval=5,
            project_id=PROJECT_ID,
            organization_id=ORGANIZATION_ID
        )
        
        # Get the configured agent
        agent = extract.get_agent(name=AGENT_NAME)
        print(f"✅ Successfully connected to agent: {AGENT_NAME}")
        
        # Run extraction on sample image
        print(f"📄 Processing sample invoice: {SAMPLE_IMAGE}")
        result = agent.extract(SAMPLE_IMAGE)
        
        # Display results
        print("✅ Extraction completed successfully!")
        print("\n📊 Extracted Data:")
        print("=" * 50)
        print(json.dumps(result.data, indent=2))
        
        # Save results for reference
        output_file = "sample_output.json"
        with open(output_file, "w") as f:
            json.dump(result.data, f, indent=2)
        print(f"\n💾 Results saved to: {output_file}")
        
        print("\n🎉 Success! You're ready to start vibe coding the Streamlit app!")
        print("Use cursor_prompt.md to transform this script into a full application.")
        
    except ApiError as e:
        print(f"❌ API Error: {e}")
        print("Check your API key and agent configuration.")
    except FileNotFoundError:
        print(f"❌ Sample image not found: {SAMPLE_IMAGE}")
        print("Make sure the sample_data directory exists with the sample image.")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

if __name__ == "__main__":
    main()

