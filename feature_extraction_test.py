# feature_extraction_test.py
from src.feature_extraction.feature_detector import FeatureDetector
from src.feature_extraction.formula_prediction import FormulaPredictor
from src.feature_extraction.database_matching import DatabaseMatcher

# Updated sample data and detected peaks with m/z values closer to the database
data = [0, 0.1, 0.2, 0.4, 0.9, 1.2, 150.6, 200.3, 0.1, 0]  # Sample signal data
peaks = [6, 7]  # Sample peak indices where m/z values are 150.6 and 200.3

# Step 1: Feature Detection
detector = FeatureDetector(data, peaks)
features = detector.detect_features()
print("Detected Features:", features)

# Step 2: Formula Prediction
predictor = FormulaPredictor(features)
features_with_formulas = predictor.predict_formulas()
print("Features with Formulas:", features_with_formulas)

# Step 3: Database Matching
matcher = DatabaseMatcher(features_with_formulas)
matched_features = matcher.match_features()
print("Matched Features:", matched_features)
