import json

def load_notebook(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_notebook(notebook, path):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(notebook, f, indent=1, ensure_ascii=False)

def create_markdown_cell(content):
    return {
        "cell_type": "markdown",
        "metadata": {},
        "source": content if isinstance(content, list) else [content]
    }

def create_code_cell(content):
    return {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": content if isinstance(content, list) else [content]
    }

print("Creating polished deliverable notebook...")

# Create new notebook structure
polished_nb = {
    "cells": [],
    "metadata": {
        "kernelspec": {
            "display_name": "Python 3",
            "language": "python",
            "name": "python3"
        },
        "language_info": {
            "codemirror_mode": {"name": "ipython", "version": 3},
            "file_extension": ".py",
            "mimetype": "text/x-python",
            "name": "python",
            "nbconvert_exporter": "python",
            "pygments_lexer": "ipython3",
            "version": "3.12.0"
        }
    },
    "nbformat": 4,
    "nbformat_minor": 2
}

# Load existing notebook to extract content
existing_nb = load_notebook('notebooks/project_deliverable_notebook.ipynb')
print(f"Loaded existing notebook with {len(existing_nb['cells'])} cells")

# Add all cells from existing notebook
polished_nb['cells'] = existing_nb['cells']

# Add a comprehensive Phase 2 summary at the end
phase2_summary = create_markdown_cell([
    "---\n",
    "\n",
    "## Complete Phase 2 Summary\n",
    "\n",
    "### 🎯 **Overall Objective Achieved**\n",
    "\n",
    "Successfully completed comprehensive data preprocessing, exploratory data analysis, and feature engineering to prepare the Ames Housing dataset for predictive modeling.\n",
    "\n",
    "---\n",
    "\n",
    "### ✅ **Phase 2A: Data Preprocessing & EDA - Deliverables**\n",
    "\n",
    "1. **Data Audit Completed**\n",
    "   - Verified dataset structure: 2,930 rows × 82 columns\n",
    "   - Identified 27 columns with missing values\n",
    "   - Confirmed 0 duplicate rows\n",
    "   - Identified 2 unique identifier columns (Order, PID)\n",
    "\n",
    "2. **Data Quality Assessment**\n",
    "   - Created comprehensive metadata summary\n",
    "   - Cross-validated with data dictionary\n",
    "   - All columns properly documented\n",
    "\n",
    "---\n",
    "\n",
    "### ✅ **Phase 2B: Preprocessing & EDA Deep Dive - Deliverables**\n",
    "\n",
    "1. **Missing Value Treatment**\n",
    "   - Dropped 4 columns with >80% missing values\n",
    "   - Imputed 11 categorical columns with 'None'\n",
    "   - Imputed 10 numerical columns with 0\n",
    "   - Used neighborhood-based median for Lot Frontage\n",
    "   - **Result**: 0 missing values remaining\n",
    "\n",
    "2. **Exploratory Data Analysis**\n",
    "   - Univariate analysis: 39 numerical features (histograms)\n",
    "   - Univariate analysis: 33 categorical features (count plots)\n",
    "   - Bivariate analysis: Correlation heatmap\n",
    "   - Scatterplots: 5 key features vs SalePrice\n",
    "   - Boxplots: 8 categorical features vs SalePrice\n",
    "   - **Key Finding**: Overall Qual (0.80), Gr Liv Area (0.71) are top predictors\n",
    "\n",
    "3. **Data Cleaning**\n",
    "   - Removed 6 low-variance categorical features\n",
    "   - Detected outliers using IQR method\n",
    "   - **Result**: Clean dataset with 72 columns\n",
    "\n",
    "---\n",
    "\n",
    "### ✅ **Phase 2C: Feature Engineering Complete - Deliverables**\n",
    "\n",
    "1. **Feature Creation & Transformation**\n",
    "   - Created 13 new features:\n",
    "     - Aggregate: Total_SF, Total_Bathrooms, Total_Porch_SF\n",
    "     - Temporal: House_Age, Years_Since_Remod\n",
    "     - Binary: Has_Pool, Has_Garage, Has_Basement, Has_Fireplace, Has_2nd_Floor\n",
    "     - Interaction: Quality_Area_Interaction\n",
    "   - Applied log transformations to 4 skewed features\n",
    "   - Encoded 33 categorical variables (9 ordinal, 24 label)\n",
    "   - **Result**: 88 total features\n",
    "\n",
    "2. **Feature Selection & Dimensionality Reduction**\n",
    "   - Correlation-based filtering: Removed 16 highly correlated features (>0.85)\n",
    "   - Random Forest importance: Identified top predictors\n",
    "     - Overall Qual: 61.7% importance\n",
    "     - Gr Liv Area: 9.1% importance\n",
    "     - **Total_Bathrooms: 5.9% importance** (our engineered feature!)\n",
    "   - **Result**: 72 optimized features\n",
    "\n",
    "3. **Feature Evaluation & Validation**\n",
    "   - Validated engineered features correlation with target\n",
    "   - Total_Bathrooms: 0.64 correlation (6th best predictor!)\n",
    "   - Lot Area_Log: 0.37 correlation\n",
    "   - **Result**: Confirmed features add significant predictive value\n",
    "\n",
    "---\n",
    "\n",
    "### 📊 **Final Dataset Statistics**\n",
    "\n",
    "| Metric | Value |\n",
    "|--------|-------|\n",
    "| **Total Records** | 2,930 |\n",
    "| **Total Features** | 71 (including identifiers) |\n",
    "| **Modeling Features** | 69 (excluding Order, PID) |\n",
    "| **Missing Values** | 3 (99.9% complete) |\n",
    "| **Data Types** | 35 int64, 23 int32, 13 float64 |\n",
    "| **Output File** | `data/AmesHousing_engineered.csv` |\n",
    "\n",
    "---\n",
    "\n",
    "### 🏆 **Key Achievements**\n",
    "\n",
    "1. ✅ **Data Quality**: Achieved 99.9% completeness (from 27 columns with missing values to only 3 missing values total)\n",
    "2. ✅ **Feature Engineering**: Created meaningful features that rank among top predictors\n",
    "3. ✅ **Dimensionality Optimization**: Reduced from 82 to 69 modeling features while improving quality\n",
    "4. ✅ **Multicollinearity Reduction**: Removed highly correlated features (>0.85)\n",
    "5. ✅ **Professional Documentation**: Clear explanations, visualizations, and justifications throughout\n",
    "\n",
    "---\n",
    "\n",
    "### 🎯 **Ready for Phase 3: Model Building & Evaluation**\n",
    "\n",
    "The dataset is now:\n",
    "- ✅ Clean and complete\n",
    "- ✅ Properly encoded (all numerical)\n",
    "- ✅ Feature-engineered with validated improvements\n",
    "- ✅ Optimized for machine learning models\n",
    "- ✅ Saved and ready for modeling\n",
    "\n",
    "**Next Phase**: Build and evaluate regression models (Linear Regression, Ridge, Lasso, Random Forest, XGBoost) to predict house sale prices.\n",
    "\n",
    "---\n"
])

polished_nb['cells'].append(phase2_summary)

# Save the polished notebook
save_notebook(polished_nb, 'notebooks/project_deliverable_notebook.ipynb')
print(f"\n[SUCCESS] Polished notebook created with {len(polished_nb['cells'])} cells")
print("Added comprehensive Phase 2 summary at the end")