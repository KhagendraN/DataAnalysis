import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

class PerformanceAnalysis:
    """
    Handles visualizations focused on efficiency and utilization (performance), 
    comparing planned budget vs. actual expenditure.
    """
    def __init__(self,
                 dataframe_budget: pd.DataFrame,
                 dataframe_expense: pd.DataFrame,
                 title: str="Budget Utilization - Performance Analysis",
                 bar_size: tuple=(10, 7),
                 bar_limit: int=7,
                 total_attributes_limit: int=21):
        
        self.dataframe_budget = dataframe_budget.copy()
        self.dataframe_expense = dataframe_expense.copy()
        self.title = title
        self.bar_limit = bar_limit
        self.bar_size = bar_size
        self.total_attribute_limit = total_attributes_limit

    def plot_utilization_bar(self):
        """
        Generates a bar chart showing the percentage utilization rate of the 
        Total Budget for a paginated list of local bodies.
        """
        feature_list = ["Recurrent", "Capital", "Financial", "Local Body", "Total"]
        columns_of_df_budget = self.dataframe_budget.columns
        columns_of_df_expn = self.dataframe_expense.columns
        missing_feature_budget = [feature for feature in feature_list if feature not in columns_of_df_budget]
        missing_feature_expn = [feature for feature in feature_list if feature not in columns_of_df_expn]
        
        # Check for missing features
        if missing_feature_budget or missing_feature_expn:
            raise ValueError(f"Missing columns in dataframe: {', '.join(missing_feature_expn, missing_feature_budget)}. Please ensure columns are named 'Total_Budget' and 'Total_Expenditure'.")
        
        # Check if total_attributes_limit > total local bodies
        if self.total_attribute_limit > len(self.dataframe_expense["Local Body"]):
            raise ValueError(f"Invalid : {self.total_attribute_limit} > {len(self.dataframe['Local Body'])}")

        #  Data Preparation
        self.dataframe_expense['Utilization_Rate'] = (self.dataframe_expense['Total'] / self.dataframe_budget['Total']) * 100
        self.dataframe_expense['Utilization_Rate'] = self.dataframe_expense['Utilization_Rate'].fillna(0).infer_objects(copy=False)
        
        # Slice and Sort Data
        df_sorted = self.dataframe_expense.sort_values(by='Utilization_Rate', ascending=False)
        df_slice = df_sorted.head(self.total_attribute_limit).copy()
        
        # Preparation of chunks
        chunks = [df_slice.iloc[i:i + self.bar_limit] for i in range(0, len(df_slice), self.bar_limit)]
        
        # Visualization

        for idx, chunk in enumerate(chunks):
            local_bodies = chunk["Local Body"]
            utilization_rates = chunk["Utilization_Rate"]
            
            fig, ax = plt.subplots(figsize=self.bar_size)
            
            # Define colors based on performance
            colors = ["#91e1a4" if rate <= 100 and rate >= 75 
                      else '#ffc107' if rate < 75 and rate >= 50 
                      else '#dc3545' 
                      for rate in utilization_rates]
            
            # Plotting Horizontal Bar Chart
            bars = ax.barh(local_bodies,
                           utilization_rates,
                           color=colors,
                           edgecolor='black')
            
            # Add labels to the bars
            for bar, rate in zip(bars, utilization_rates):
                ax.text(bar.get_width() + 1, 
                        bar.get_y() + bar.get_height()/2, 
                        f'{rate:.1f}%', 
                        va='center', 
                        ha='left', 
                        fontsize=10)

            # Set X-axis limit and labels
            ax.set_xlim(0, 250) 
            ax.set_xlabel("Budget Utilization Rate (%)")
            ax.set_ylabel("Local Bodies")
            ax.set_title(f"Performance Analysis - Utilization rate", fontsize=14)

            # Add a vertical line at the 100% mark as a target reference
            ax.axvline(100, color='red', linestyle='--', linewidth=1, alpha=0.7)
            
            # Show the plot for the current chunk
            plt.tight_layout()
            #plt.legend()
            plt.show()


class PieCharts:
    def __init__(self):
        pass