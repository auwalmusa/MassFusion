# src/feature_extraction/database_matching.py
class DatabaseMatcher:
    def __init__(self, features, database=None):
        """
        Initializes the DatabaseMatcher with features and an optional database.
        
        Parameters:
        - features (list): List of features with m/z values.
        - database (list of dict): List of known compounds with m/z and name.
        """
        self.features = features
        self.database = database if database else [
            {"name": "Compound_A", "m/z": 100.1},
            {"name": "Compound_B", "m/z": 150.5},
            {"name": "Compound_C", "m/z": 200.3}
        ]

    def match_features(self, tolerance=0.5):
        """
        Matches detected features to known compounds in the database.
        
        Parameters:
        - tolerance (float): Allowable difference in m/z for a match.
        
        Returns:
        - matched_features (list): List of features with matched compounds.
        """
        matched_features = []
        for feature in self.features:
            feature_mz = feature["m/z"]
            for compound in self.database:
                if abs(feature_mz - compound["m/z"]) <= tolerance:
                    matched_feature = feature.copy()
                    matched_feature["compound"] = compound["name"]
                    matched_features.append(matched_feature)
        return matched_features
