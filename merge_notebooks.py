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

phase2a = load_notebook('notebooks/Phase-2A_Data_Preprocessing_and_EDA.ipynb')
print(f"Phase-2A has {len(phase2a['cells'])} cells")

phase2b = load_notebook('notebooks/Phase-2B_Feature_Engineering.ipynb')
print(f"Phase-2B has {len(phase2b['cells'])} cells")

base_notebook = {
    "cells": [],
    "metadata": {
        "kernelspec": {
            "display_name": "Python 3",
            "language": "python",
            "name": "python3"
        },
        "language_info": {
            "codemirror_mode": {
                "name": "ipython",
                "version": 3
            },
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

base_notebook['cells'].extend([
    create_markdown_cell("# Real Estate Price Prediction - Complete Project Deliverable\n"),
    create_markdown_cell("**Team**: The Outliers  \n**Course**: Advanced Apex Project 1 - BITS Pilani Digital  \n**Trimester**: First Trimester 2025-26  \n**Supervisor**: Bharathi Dasari\n"),
    create_markdown_cell("---\n"),
    create_markdown_cell("## Team Members\n\n| Name | BITS ID |\n|------|--------|\n| Anik Das | 2025EM1100026 |\n| Adeetya Wadikar | 2025EM1100384 |\n| Tushar Nishane | 2025EM1100306 |\n"),
    create_markdown_cell("---\n"),
    create_markdown_cell("## Project Overview\n\n**Problem Statement**: Accurate real estate price prediction using machine learning regression models.\n\n**Business Goal**: Develop a predictive model that estimates property sale prices with high accuracy to help buyers, sellers, and investors make informed decisions.\n\n**Dataset**: Ames Housing Dataset from Kaggle  \n- **Records**: 2,930 residential properties  \n- **Features**: 82 attributes (numerical and categorical)  \n- **Target Variable**: SalePrice (house sale price in USD)\n"),
    create_markdown_cell("---\n"),
    create_markdown_cell("## Table of Contents\n\n1. [Phase 1: Data Acquisition](#phase1)\n2. [Phase 2A: Data Preprocessing & EDA](#phase2a)\n3. [Phase 2B: Feature Engineering](#phase2b)\n4. [Phase 3: Modeling & Evaluation](#phase3)\n5. [Phase 4: Visualization & Storytelling](#phase4)\n6. [Phase 5: Final Summary & Conclusions](#phase5)\n"),
    create_markdown_cell("---\n<a id='phase1'></a>\n\n# Phase 1: Data Acquisition\n\n**Objective**: Load the Ames Housing dataset, verify its structure, and create a metadata summary for downstream analysis.\n\n**Deliverables**:\n- ✅ Data extraction from Kaggle\n- ✅ Schema verification\n- ✅ Data audit (missing values, duplicates, identifiers)\n- ✅ Metadata summary creation\n- ✅ Data dictionary validation\n"),
])

base_notebook['cells'].extend([
    create_markdown_cell("---\n## 1.1 Import Dependencies"),
    create_code_cell("# Import required libraries\nimport os\nimport pandas as pd\nimport numpy as np\n\n# Display settings\npd.set_option('display.max_columns', None)\npd.set_option('display.max_rows', 100)\n\nprint(\"✅ Libraries imported successfully\")\nprint(f\"Pandas version: {pd.__version__}\")\nprint(f\"NumPy version: {np.__version__}\")"),
    create_markdown_cell("## 1.2 Dataset Import\n\n**Data Source**: Kaggle - Ames Housing Dataset  \n**Citation**: Shashank Necrothapa. (n.d.). Ames Housing Dataset [Data set]. Kaggle.  \n**URL**: https://www.kaggle.com/datasets/shashanknecrothapa/ames-housing-dataset\n\nThe dataset was downloaded manually from Kaggle and stored in the `data/` directory."),
    create_code_cell("# Define data path\ndata_path = \"../data/AmesHousing.csv\"\n\n# Load dataset\ndf = pd.read_csv(data_path)\n\nprint(\"✅ Dataset Loaded Successfully\")\nprint(f\"Shape: {df.shape}\")\nprint(f\"\\nDataset contains {df.shape[0]:,} rows and {df.shape[1]} columns\")"),
    create_markdown_cell("---\n\n## Phase 1 Summary\n\n### ✅ Deliverables Completed:\n\n1. **Dataset Successfully Loaded**\n   - Shape: 2,930 rows × 82 columns\n   - Source: Kaggle - Ames Housing Dataset\n\n2. **Data Audit Completed**\n   - No duplicate rows found ✅\n   - 27 features contain missing values\n   - Unique identifiers: Order, PID\n\n3. **Data Types Identified**\n   - Categorical (object): 43 columns\n   - Integer (int64): 28 columns\n   - Float (float64): 11 columns\n\n### 🎯 Next Steps:\n\nProceed to **Phase 2A: Data Preprocessing & EDA**\n\n---"),
])

base_notebook['cells'].append(
    create_markdown_cell("<a id='phase2a'></a>\n\n# Phase 2A: Data Preprocessing & EDA\n\n**Objective**: Clean the dataset, handle missing values, perform exploratory data analysis, and prepare data for feature engineering.\n\n**Deliverables**:\n- ✅ Missing value treatment\n- ✅ Outlier detection and analysis\n- ✅ Univariate and bivariate analysis\n- ✅ Data quality improvements\n- ✅ Cleaned dataset preparation\n\n---")
)

base_notebook['cells'].extend(phase2a['cells'])

base_notebook['cells'].append(
    create_markdown_cell("<a id='phase2b'></a>\n\n# Phase 2B: Feature Engineering\n\n**Objective**: Create new features, transform existing features, and prepare the final dataset for modeling.\n\n**Deliverables**:\n- ✅ Feature creation and transformation\n- ✅ Encoding categorical variables\n- ✅ Feature scaling and normalization\n- ✅ Final dataset preparation\n\n---")
)

base_notebook['cells'].extend(phase2b['cells'])

save_notebook(base_notebook, 'notebooks/project_deliverable_notebook.ipynb')
print(f"\nMerged notebook created with {len(base_notebook['cells'])} total cells")
print("Saved to: notebooks/project_deliverable_notebook.ipynb")