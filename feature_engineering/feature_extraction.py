import pandas as pd

class FeatureExtraction:
    """This extracts the relevant features from available data file."""
    def __init__(self, fname: str, province_name: str="Bagmati Province"):
        self.fname = fname
        self.province_name = province_name

    def open_file(self) -> pd.DataFrame:
        """Reads excel file and returns data frame"""
        df = pd.read_excel(self.fname, skiprows=3)
        return df
    
    def rename_label(self, dataframe: pd.DataFrame) -> pd.DataFrame:
        """This will rename the columns with meaningful names."""
        dataframe = dataframe.fillna('').copy()
        rename_dict = {
            "Province 1" : "SN",
            "Unnamed: 1" : "Local Body",
            "Unnamed: 2" : "Recurrent",
            "Unnamed: 3" : "Capital",
            "Unnamed: 4" : "Financial",
            "Unnamed: 5" : "Total",
            "Unnamed: 6" : "Recurrent",
            "Unnamed: 7" : "Capital",
            "Unnamed: 8" : "Financial",
            "Unnamed: 9" : "Total",
            "Unnamed: 10" : "Cash Balance",
        }
        dataframe = dataframe.rename(columns=rename_dict)
        return dataframe
    
    def extract_rows_for_province(self, dataframe: pd.DataFrame) -> pd.DataFrame:
        """Finds combined budget and expenditure for each province"""
        first_element_of_pro = self.province_name
        last_element_of_pro = f"{self.province_name} Total" 

        if self.province_name == "Province 1":
            start_idx = 0
        else:
            start_idx = dataframe[dataframe["SN"] == first_element_of_pro].index[0] + 1

        # Check if the last element exists in the dataframe
        last_row = dataframe[dataframe["SN"] == last_element_of_pro]

        if last_row.empty:
            raise ValueError(f"{last_element_of_pro} not found in the dataframe")

        # Get the index of the last element of the province
        end_idx = last_row.index[0]

        dataframe = dataframe.iloc[start_idx :end_idx + 1, :].copy()
        return dataframe


    def extract_budget_frame(self, dataframe: pd.DataFrame) -> pd.DataFrame:
        """Extracts data frame for budget part"""
        dataframe = dataframe.iloc[:, list(range(6)) + [10]].copy()
        return dataframe
    
    def extract_expenditure_frame(self, dataframe: pd.DataFrame) -> pd.DataFrame:
        """Extracts data frame for expenditure part"""
        dataframe = dataframe.iloc[:, list(range(2)) + list(range(6, 11))].copy()
        return dataframe
    
    def extract_individual(self):
        """Main implementation"""
        df = self.open_file()
        print("Original data extracted successfully☺️") 
        df_renamed = self.rename_label(df)
        print("DataFrame Renamed successfully☺️")  
        df_rows = self.extract_rows_for_province(df_renamed)
        df_budget = self.extract_budget_frame(df_rows)
        df_expenditure = self.extract_expenditure_frame(df_rows)
        print("ALL THE OPERSTIONS WERE SUCCESSFUL😊")
        return df_budget, df_expenditure
    


