from dotenv import load_dotenv
from llama_cloud_services import LlamaExtract
from llama_cloud.core.api_error import ApiError


project_id = "2fef999e-1073-40e6-aeb3-1f3c0e64d99b"
organization_id = "43b88c8f-e488-46f6-9013-698e3d2e374a"

# Optionally, add your project id/organization id
extract = LlamaExtract(
    show_progress=False, 
    check_interval=5,
    project_id=project_id,
    organization_id=organization_id
)


agent = extract.get_agent(name="kaggle_invoice_agent")

result = agent.extract("batch1-0274.jpg")
result.data # outputs json of the extracted output according to the schema defined in the agent

