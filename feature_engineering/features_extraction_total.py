import pandas as pd

class FeatureExtractionTotal:
    """Extracts frame for total budget and total expenditure"""
    def __init__(self, budget_frame: pd.DataFrame, exp_frame: pd.DataFrame):
        self.budget_frame = budget_frame.copy()
        self.exp_frame = exp_frame.copy()

    def extract_index_for_total(self) -> list:
        """Extract index for total and return list"""
        index_names = ["Province 1 Total",
               "Madesh Province Total",
               "Bagmati Province Total",
               "Gandaki Province Total",
               "Lumbini Province Total",
               "Karnali Province Total",
               "Sudurpaschim Province Total"]
        indexes = []
        for province in index_names:
            index_value = self.budget_frame[self.budget_frame["SN"] == province].index[0]
            indexes.append(index_value)
        return indexes
    
    def extract_total(self):
        indexes = self.extract_index_for_total()
        print("Index extracted 😍")
        total_budget_df = self.budget_frame.iloc[indexes].copy()
        total_exp_df = self.exp_frame.iloc[indexes].copy()
        print("Frame for total extracted 😍")
        # rename SN to province 
        total_budget_df = total_budget_df.rename(columns={"SN": "Province"})
        total_exp_df = total_exp_df.rename(columns={"SN": "Province"})
        # Remove local body
        total_budget_df = total_budget_df.drop("Local Body", axis=1)
        total_exp_df = total_exp_df.drop("Local Body", axis=1)
        print("Successful 😍")

        return total_budget_df, total_exp_df