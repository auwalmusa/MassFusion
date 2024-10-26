# src/feature_extraction/formula_prediction.py
class FormulaPredictor:
    def __init__(self, features):
        """
        Initializes the FormulaPredictor with detected features.
        
        Parameters:
        - features (list): List of features with m/z values.
        """
        self.features = features

    def predict_formulas(self):
        """
        Predicts molecular formulas based on m/z values (simple approximation).
        
        Returns:
        - features_with_formulas (list): List of features with m/z, intensity, and formula.
        """
        for feature in self.features:
            # Simple approximation: Use m/z value to generate formula suggestion
            m_z = feature["m/z"]
            formula = f"C{int(m_z // 12)}H{int(m_z // 1.0079)}"  # Rough approximation
            feature["formula"] = formula
        return self.features
