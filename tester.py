from src.data_import.import_manager import ImportManager
from src.data_import.metadata_extractor import MetadataExtractor

# Step 1: Import data
importer = ImportManager("data/raw/sample.json", file_format="json")
data = importer.load_data()

# Step 2: Extract metadata
if data:
    extractor = MetadataExtractor(data)
    metadata = extractor.extract_metadata()
    print("Extracted Metadata:", metadata)
