from image_extractor import ImageExtractor
import json
imageExt = ImageExtractor()
# print(imageExt.get_response("You are a Banking and mortgage expert. What is the approved loan amount?","images"))
print(imageExt.get_response("You are a Banking and mortgage expert. Who are the witnesses to this deed and when it was signed, give the name and date ?","images"))
#output = imageExt.get_response("You are a Banking and mortgage expert. Extract all the information from the mortgage and loan document as json file, do not make up any information","images")

# try:
#     with open("loan_info.json", "w") as json_file:
#         json.dump(output, json_file, indent=4) # indent=4 for pretty-printing
#     print("Data successfully written to product_info.json")
# except IOError as e:
#     print(f"Error writing to file: {e}")
