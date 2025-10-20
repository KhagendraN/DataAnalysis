import matplotlib.pyplot as plt
import pandas as pd

class CompositionAnalysis:
    """To show the part-to-whole relationship for all financial figures:
      (Recurrent, Capital, Financial).
    """
    def __init__(self,
                 dataframe: pd.DataFrame,
                 title: str="Budget",
                 bar_size: tuple=(8,6),
                 bar_limit: int=7,
                 total_attributes_limit: int=21,
                 bar_colors: dict=None):
        self.dataframe = dataframe
        self.title = title
        self.bar_limit = bar_limit
        self.bar_size = bar_size
        self.total_attribute_limit = total_attributes_limit
        
        # Set default colors if not provided
        self.bar_colors = bar_colors if bar_colors else {
            'Recurrent': 'lightblue',
            'Capital': 'lightgreen',
            'Financial': 'salmon'
        }

    def plot_composition_bar(self):
        feature_list = ["Recurrent", "Capital", "Financial", "Local Body", "Total"]
        columns_of_df = self.dataframe.columns
        missing_feature = [feature for feature in feature_list if feature not in columns_of_df]
        
        # Check for missing features
        if missing_feature:
            raise ValueError(f"Missing columns in dataframe: {', '.join(missing_feature)}")
        
        # check if total_attributes_limit > total local bodies
        if self.total_attribute_limit > len(self.dataframe["Local Body"]):
            raise ValueError(f"Invalid : {self.total_attribute_limit} > {len(self.dataframe["Local Body"])}")
        
        # Fill NaN values in 'Total' column
        self.dataframe["Total"] = self.dataframe["Total"].fillna(0)
        
        # Slice data based on total_attributes_limit
        self.dataframe = self.dataframe.head(self.total_attribute_limit)
        
        # Calculate number of chunks
        chunks = [self.dataframe.iloc[i:i + self.bar_limit] for i in range(0, len(self.dataframe), self.bar_limit)]
        
        for idx, chunk in enumerate(chunks):
            # Extract data for current chunk
            Recurrent = chunk["Recurrent"]
            Capital = chunk["Capital"]
            Financial = chunk["Financial"]
            attributes = chunk["Local Body"]
            total_amount = chunk["Total"]
            
            # Create a new figure for each chunk
            fig, ax = plt.subplots(figsize=self.bar_size)
            
            ax.barh(attributes,
                    Recurrent,
                    color=self.bar_colors['Recurrent'],
                    label='Recurrent'
                    )
            ax.barh(attributes,
                    Capital,
                    left=Recurrent,
                    color=self.bar_colors['Capital'],
                    label='Capital'
                    )
            ax.barh(attributes,
                    Financial,
                    left=Recurrent + Capital,
                    color=self.bar_colors['Financial'],
                    label='Finance')
            
            # Add total amount labels
            for i, t in enumerate(total_amount):
                padding = max(2, t * 0.02) 
                ax.text(t + padding, i, str(t), va='center', ha='left', fontsize=10)

            # Set labels and title
            ax.set_xlabel("Total Amount")
            ax.set_ylabel("Local Bodies")
            ax.set_title(f"{self.title} In 10M - Part {idx + 1}")

            # Show legend
            ax.legend()
            
            # Show the plot for the current chunk
            plt.show()
