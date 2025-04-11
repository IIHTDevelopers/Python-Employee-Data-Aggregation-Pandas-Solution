import pandas as pd

class EmployeeDataAnalysis:
    def __init__(self, file_path):
        """Load CSV data into a Pandas DataFrame."""
        self.df = pd.read_csv(file_path)

    def display_head(self):
        """Return the first 5 rows of the DataFrame."""
        return self.df.head()

    def dataframe_info(self):
        """Return DataFrame column names and data types."""
        return self.df.info()

    def group_by_department(self):
        """Group the employee data by department and compute aggregate statistics."""
        return self.df.groupby('Department').agg(
            Age_Mean=('Age', 'mean'),
            Salary_Mean=('Salary', 'mean'),
            Age_Median=('Age', 'median'),
            Salary_Median=('Salary', 'median'),
            Employee_Count=('Employee ID', 'count')
        )

    def export_aggregated_data(self, output_file="department_statistics.csv"):
        """Save the aggregated statistics to a new CSV file."""
        aggregated_data = self.group_by_department()
        aggregated_data.to_csv(output_file)
        return aggregated_data
