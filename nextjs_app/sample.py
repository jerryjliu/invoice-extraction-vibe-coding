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



#### NOTE: HERE IS THE SCHEMA DEFINITION
# {
#   "additionalProperties": false,
#   "properties": {
#     "invoice_number": {
#       "description": "The unique identifier for the invoice.",
#       "type": "string"
#     },
#     "issue_date": {
#       "description": "The date the invoice was issued, formatted as MM/DD/YYYY.",
#       "type": "string"
#     },
#     "seller": {
#       "additionalProperties": false,
#       "description": "Information about the seller.",
#       "properties": {
#         "name": {
#           "description": "The name of the seller.",
#           "type": "string"
#         },
#         "address": {
#           "description": "The address of the seller.",
#           "type": "string"
#         },
#         "tax_id": {
#           "description": "The tax identification number of the seller.",
#           "type": "string"
#         },
#         "iban": {
#           "description": "The International Bank Account Number of the seller.",
#           "type": "string"
#         }
#       },
#       "required": [
#         "name",
#         "address",
#         "tax_id",
#         "iban"
#       ],
#       "type": "object"
#     },
#     "client": {
#       "additionalProperties": false,
#       "description": "Information about the client.",
#       "properties": {
#         "name": {
#           "description": "The name of the client.",
#           "type": "string"
#         },
#         "address": {
#           "description": "The address of the client.",
#           "type": "string"
#         },
#         "tax_id": {
#           "description": "The tax identification number of the client.",
#           "type": "string"
#         }
#       },
#       "required": [
#         "name",
#         "address",
#         "tax_id"
#       ],
#       "type": "object"
#     },
#     "items": {
#       "description": "A list of items included in the invoice.",
#       "items": {
#         "additionalProperties": false,
#         "properties": {
#           "item_number": {
#             "description": "The item number or identifier.",
#             "type": "string"
#           },
#           "description": {
#             "description": "A description of the item.",
#             "type": "string"
#           },
#           "quantity": {
#             "description": "The quantity of the item.",
#             "type": "number"
#           },
#           "unit_of_measure": {
#             "description": "The unit of measure for the item (e.g., each, kg, liter).",
#             "type": "string"
#           },
#           "net_price": {
#             "description": "The net price of the item.",
#             "type": "number"
#           },
#           "net_worth": {
#             "description": "The net worth of the item (quantity * net_price).",
#             "type": "number"
#           },
#           "vat_percentage": {
#             "description": "The VAT percentage applied to the item.",
#             "type": "string"
#           },
#           "gross_worth": {
#             "description": "The gross worth of the item (including VAT).",
#             "type": "number"
#           }
#         },
#         "required": [
#           "item_number",
#           "description",
#           "quantity",
#           "unit_of_measure",
#           "net_price",
#           "net_worth",
#           "vat_percentage",
#           "gross_worth"
#         ],
#         "type": "object"
#       },
#       "type": "array"
#     },
#     "summary": {
#       "additionalProperties": false,
#       "description": "Summary of the invoice amounts.",
#       "properties": {
#         "vat_summary": {
#           "description": "Summary of VAT amounts for different VAT percentages.",
#           "items": {
#             "additionalProperties": false,
#             "properties": {
#               "vat_percentage": {
#                 "description": "The VAT percentage.",
#                 "type": "string"
#               },
#               "net_worth": {
#                 "description": "The total net worth for this VAT percentage.",
#                 "type": "number"
#               },
#               "vat": {
#                 "description": "The total VAT amount for this VAT percentage.",
#                 "type": "number"
#               },
#               "gross_worth": {
#                 "description": "The total gross worth for this VAT percentage.",
#                 "type": "number"
#               }
#             },
#             "required": [
#               "vat_percentage",
#               "net_worth",
#               "vat",
#               "gross_worth"
#             ],
#             "type": "object"
#           },
#           "type": "array"
#         },
#         "total_net_worth": {
#           "description": "The total net worth of the invoice.",
#           "type": "number"
#         },
#         "total_vat": {
#           "description": "The total VAT amount for the invoice.",
#           "type": "number"
#         },
#         "total_gross_worth": {
#           "description": "The total gross worth of the invoice.",
#           "type": "number"
#         }
#       },
#       "required": [
#         "vat_summary",
#         "total_net_worth",
#         "total_vat",
#         "total_gross_worth"
#       ],
#       "type": "object"
#     }
#   },
#   "required": [
#     "invoice_number",
#     "issue_date",
#     "seller",
#     "client",
#     "items",
#     "summary"
#   ],
#   "type": "object"
# }