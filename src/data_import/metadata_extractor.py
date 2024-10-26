# src/data_import/metadata_extractor.py

class MetadataExtractor:
    def __init__(self, data):
        """
        Initializes the MetadataExtractor with data loaded by ImportManager.
        
        Parameters:
        - data: The data object loaded by ImportManager.
        """
        self.data = data
        self.metadata = {}

    def extract_metadata(self):
        """
        Extracts metadata from the loaded data.
        
        Returns:
        - metadata (dict): Dictionary containing extracted metadata.
        """
        # Check if the data has 'info' attribute directly (for mzML data) or as a dictionary key (for JSON data)
        if isinstance(self.data, dict) and 'info' in self.data:
            info = self.data['info']
            self.metadata['instrument'] = info.get('instrument', 'Unknown')
            self.metadata['run_start_time'] = info.get('start_time', 'Unknown')
            self.metadata['file_description'] = info.get('file_description', 'Unknown')
        elif hasattr(self.data, 'info'):
            # If data has an 'info' attribute (e.g., mzML data), access it directly
            self.metadata['instrument'] = self.data.info.get('instrument', 'Unknown')
            self.metadata['run_start_time'] = self.data.info.get('start_time', 'Unknown')
            self.metadata['file_description'] = self.data.info.get('file_description', 'Unknown')
        else:
            print("Warning: Metadata extraction not supported for this data format.")
        
        return self.metadata
