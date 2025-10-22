import pandas as pd

class FeatureExtractionUrban:
    """Extract data for urban areas only"""
    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()

    def extract_urban_features(self):
        df_filtered = self.df[self.df["Local Body"].str.contains(r'(?:Sub-Metropolitan|Metropolitan)$', case=False, na=False)]
        df_sorted = df_filtered.sort_values(by="Total", ascending=False)
        return df_sorted