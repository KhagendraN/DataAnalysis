import pandas as pd
import matplotlib.pyplot as plt

class PieCharts:
    """A class to generate pie charts for budget and expense data across different provinces and local bodies."""

    def __init__(self,
                 expense_frame: pd.DataFrame,
                 budget_frame : pd.DataFrame,
                 expense_total: pd.DataFrame,
                 budget_total: pd.DataFrame):
        """
        Initializes the PieCharts object with the provided data frames.
        
        Args:
            expense_frame (pd.DataFrame): Data frame containing the expense data.
            budget_frame (pd.DataFrame): Data frame containing the budget data.
            expense_total (pd.DataFrame): Data frame containing total expense data for each province.
            budget_total (pd.DataFrame): Data frame containing total budget data for each province.
        """
        self.expense_frame = expense_frame.copy()
        self.budget_frame = budget_frame.copy()
        self.expense_total = expense_total.copy()
        self.budget_total = budget_total.copy()

    @staticmethod
    def plot_total(dataframe: pd.DataFrame, title: str):
        """
        Plots a pie chart showing the total values for each province.

        Args:
            dataframe (pd.DataFrame): Data frame containing the total data to plot.
            title (str): The title of the pie chart (e.g., "Budget" or "Expense").
        """
        plt.pie(x=dataframe["Total"],
                labels=dataframe["Province"],
                autopct='%1.1f%%',
                startangle=140,
                shadow=False,
                normalize=True)
        
        plt.title(f"Total {title} for each province")
        plt.axis('equal')
        plt.show()

    def plot_for_total(self, type: str='budget'):
        """
        Plots a pie chart for the total budget or total expense by province.

        Args:
            type (str): Specifies whether to plot "budget" or "expense". Defaults to 'budget'.
        """
        if type == 'budget':
            sum_province = self.budget_total[["Province", "Total"]].copy()
            self.plot_total(dataframe=sum_province, title=type)
        else:
            sum_province = self.expense_total[["Province", "Total"]].copy()
            self.plot_total(dataframe=sum_province, title=type)

    @staticmethod
    def find_index(dataframe : pd.DataFrame, name: str):
        """
        Finds the index of a local body by its name.

        Args:
            dataframe (pd.DataFrame): Data frame containing the local body data.
            name (str): The name of the local body to search for.

        Returns:
            int: The index of the local body in the data frame.
        """
        idx = dataframe[dataframe["Local Body"] == name].index[0]
        return idx
    
    @staticmethod
    def plot_local_body(dataframe: pd.DataFrame, title: str, labels: list):
        """
        Plots a pie chart for a specific local body showing different categories (Recurrent, Capital, etc.).

        Args:
            dataframe (pd.DataFrame): Data frame containing data for a specific local body.
            title (str): The title of the pie chart (e.g., "Budget" or "Expense").
            labels (list): A list of category labels (e.g., ['Recurrent', 'Capital', 'Financial', 'Cash Balance']).
        """
        x = []
        for name in labels:
            value = dataframe[name]
            x.append(value)

        plt.pie(x=x,
                labels=labels,
                autopct='%1.1f%%',
                startangle=140,
                shadow=False,
                normalize=True)
        
        plt.title(f"{title} for Local body")
        plt.axis('equal')
        plt.show()

    def plot_for_local_body(self, local_body: str, type: str='budget'):
        """
        Plots a pie chart for a specific local body showing its budget or expense data.

        Args:
            local_body (str): The name of the local body to plot.
            type (str): Specifies whether to plot "budget" or "expense". Defaults to 'budget'.
        """
        labels = ['Recurrent', 'Capital', 'Financial', 'Cash Balance']
        if type == "budget":
            idx = self.find_index(dataframe=self.budget_frame, name=local_body)
            bud_for_lb = self.budget_frame.iloc[idx].copy()
            self.plot_local_body(dataframe=bud_for_lb, title=type, labels=labels)
        
        else:
            idx = self.find_index(dataframe=self.expense_frame, name=local_body)
            exp_for_lb = self.expense_frame.iloc[idx].copy()
            self.plot_local_body(dataframe=exp_for_lb, title=type, labels=labels)
