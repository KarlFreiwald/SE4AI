# README

## Folder Structure

This project is organized into several directories, each serving a specific purpose. Below is an explanation of the structure and contents of each directory.

### Notebooks (.ipynb)

This folder contains Jupyter notebooks for various stages of the project:

1. **DataPreprocessing.ipynb**: 
   - Purpose: Preprocessing and storing data from the dataset available at [Kaggle Traffic Signs Classification](https://www.kaggle.com/code/valentynsichkar/traffic-signs-classification-with-cnn/).
   - Output: Data is saved in pickle files for easy loading in other notebooks.

2. **CNN.ipynb**:
   - Purpose: Training the original Convolutional Neural Network model.
   - Output: The trained model is saved as `model-3x3.keras`.

3. **Naïve_Trojan.ipynb**:
   - Purpose: Performing a naive trojan attack and checking its impact on the model.

4. **Neural_Trojan.ipynb**:
   - Purpose: Implementing a neural trojan attack and evaluating its impact on the model.

5. **MeanImageComputation.ipynb**: 
   - Purpose: (To be written) This notebook will compute the mean images for analysis purposes.

6. **SPC.ipynb**:
   - Purpose: Checking scale consistency on example images to assess if it might be a method for trojan detection.

### Models (.keras)

This folder stores the saved neural network models:

1. **model-3x3.keras**:
   - Description: The original trained CNN model.

2. **model_attack_1.keras**:
   - Description: Model after undergoing the first optimized attack.

3. **model_attack_2.keras**:
   - Description: Model after undergoing the second optimized attack.

### Dataset (.csv)

This folder contains the dataset files:

1. **Label_names.csv**:
   - Description: Stores the 43 class integer keys and their respective string labels.

### Helpers (.py)

This folder contains helper scripts to facilitate various operations:

1. **helpers.py**:
   - Description: Contains functions for loading and unloading data, constructing balanced datasets, and printing images.

2. **Import_notebook.ipynb**:
   - Description: Enables the import of code sections from another notebook for reuse.

### Images

This folder stores images generated during the project:

1. **images**:
   - Description: Stores images generated within the various notebooks.

2. **average_images**:
   - Description: (To be inserted) This folder will store average images computed in the `MeanImageComputation.ipynb` notebook for further analysis.

## Notes

- Ensure that the required libraries are installed before running the notebooks.
- Maintain the structure to avoid issues with file paths and imports.

This README provides an overview of the project structure and the purpose of each directory and file. If you have any questions or need further assistance, feel free to reach out.
