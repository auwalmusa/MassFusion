# src/data_import/import_manager.py

import pymzml  # For mzML file handling
import json    # For JSON file handling
import os      # For checking file paths

class ImportManager:
    def __init__(self, file_path, file_format="mzML"):
        """
        Initializes the ImportManager with a file path and format.
        
        Parameters:
        - file_path (str): Path to the file to load.
        - file_format (str): Format of the file (e.g., 'mzML', 'json').
        """
        self.file_path = file_path
        self.file_format = file_format
        self.data = None

    def load_data(self):
        """
        Loads the data based on the specified file format.
        
        Returns:
        - Loaded data if successful, otherwise raises an error.
        """
        # Check if the file exists
        if not os.path.exists(self.file_path):
            print(f"Error: File '{self.file_path}' does not exist.")
            return None

        # Load data based on file format
        try:
            if self.file_format.lower() == "mzml":
                self.data = pymzml.run.Reader(self.file_path)
            elif self.file_format.lower() == "json":
                with open(self.file_path, 'r') as file:
                    self.data = json.load(file)
            else:
                print(f"Error: Unsupported file format '{self.file_format}'.")
                return None
        except Exception as e:
            print(f"An error occurred while loading the data: {e}")
            return None

        print(f"Data loaded successfully from {self.file_path} in {self.file_format} format.")
        return self.data
