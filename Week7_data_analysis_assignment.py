import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
from typing import Tuple, Dict, Any

class DataAnalyzer:
    def __init__(self):
        self.data = None
        self.X = None
        self.y = None
        self.feature_names = None
        self.target_names = None
    
    def load_iris_dataset(self) -> None:
        """Load the Iris dataset from scikit-learn."""
        try:
            iris = load_iris()
            self.X = pd.DataFrame(iris.data, columns=iris.feature_names)
            self.y = pd.Series(iris.target, name='target')
            self.target_names = iris.target_names
            self.feature_names = iris.feature_names
            self.data = pd.concat([self.X, self.y], axis=1)
            print("Iris dataset loaded successfully!")
            print(f"Dataset shape: {self.data.shape}")
        except Exception as e:
            print(f"Error loading Iris dataset: {e}")
    
    def explore_data(self) -> None:
        """Explore the dataset by displaying basic information."""
        if self.data is None:
            print("No data loaded. Please load the dataset first.")
            return
        
        print("\n=== First 5 rows ===")
        print(self.data.head())
        
        print("\n=== Dataset Info ===")
        print(self.data.info())
        
        print("\n=== Missing Values ===")
        print(self.data.isnull().sum())
        
        print("\n=== Basic Statistics ===")
        print(self.data.describe())
    
    def analyze_by_species(self) -> pd.DataFrame:
        """Group data by species and calculate mean values."""
        if self.data is None:
            print("No data loaded. Please load the dataset first.")
            return None
        
        # Map target values to species names
        self.data['species'] = self.data['target'].map(
            {i: name for i, name in enumerate(self.target_names)}
        )
        
        # Group by species and calculate mean
        species_means = self.data.groupby('species').mean(numeric_only=True)
        return species_means
    
    def create_visualizations(self) -> None:
        """Create and display various visualizations."""
        if self.data is None:
            print("No data loaded. Please load the dataset first.")
            return
        
        # Set style
        sns.set_style("whitegrid")
        
        # 1. Line Chart - Feature means by species
        plt.figure(figsize=(12, 6))
        species_means = self.analyze_by_species()
        species_means.T.plot(kind='line', marker='o')
        plt.title('Mean Feature Values by Iris Species')
        plt.ylabel('Mean Value')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
        
        # 2. Bar Chart - Compare sepal length by species
        plt.figure(figsize=(10, 6))
        sns.barplot(x='species', y='sepal length (cm)', data=self.data, 
                   order=self.target_names, ci=None)
        plt.title('Average Sepal Length by Species')
        plt.xlabel('Species')
        plt.ylabel('Sepal Length (cm)')
        plt.tight_layout()
        plt.show()
        
        # 3. Histogram - Distribution of sepal width
        plt.figure(figsize=(10, 6))
        sns.histplot(data=self.data, x='sepal width (cm)', hue='species', 
                    element='step', kde=True, bins=15)
        plt.title('Distribution of Sepal Width by Species')
        plt.xlabel('Sepal Width (cm)')
        plt.ylabel('Count')
        plt.tight_layout()
        plt.show()
        
        # 4. Scatter Plot - Sepal length vs Petal length
        plt.figure(figsize=(10, 6))
        sns.scatterplot(data=self.data, x='sepal length (cm)', 
                       y='petal length (cm)', hue='species', 
                       style='species', s=100)
        plt.title('Sepal Length vs Petal Length by Species')
        plt.xlabel('Sepal Length (cm)')
        plt.ylabel('Petal Length (cm)')
        plt.legend(title='Species')
        plt.tight_layout()
        plt.show()

def main():
    # Initialize the analyzer
    analyzer = DataAnalyzer()
    
    # Load and explore the dataset
    analyzer.load_iris_dataset()
    analyzer.explore_data()
    
    # Perform analysis by species
    print("\n=== Analysis by Species ===")
    species_analysis = analyzer.analyze_by_species()
    if species_analysis is not None:
        print(species_analysis)
    
    # Create visualizations
    print("\nCreating visualizations...")
    analyzer.create_visualizations()
    
    print("\n=== Analysis Complete ===")
    print("Key Findings:")
    print("1. Setosa has the smallest petal dimensions but the widest sepals.")
    print("2. Virginica has the largest petals and longer sepals.")
    print("3. There's a clear separation between species in the scatter plot, "
          "especially between Setosa and the other two species.")
    print("4. The distribution of sepal width shows some overlap between "
          "Versicolor and Virginica, but Setosa is distinct.")

if __name__ == "__main__":
    main()
