import numpy as np
import matplotlib.pyplot as plt
import pickle
import os


def convert_to_grid(x_input):
    """
    Preparing function for ploting set of examples
    As input it will take 4D tensor and convert it to the grid
    Values will be scaled to the range [0, 255]
    """

    N, H, W, C = x_input.shape
    grid_size = int(np.ceil(np.sqrt(N)))
    grid_height = H * grid_size + 1 * (grid_size - 1)
    grid_width = W * grid_size + 1 * (grid_size - 1)
    grid = np.zeros((grid_height, grid_width, C)) + 255
    next_idx = 0
    y0, y1 = 0, H
    for y in range(grid_size):
        x0, x1 = 0, W
        for x in range(grid_size):
            if next_idx < N:
                img = x_input[next_idx]
                low, high = np.min(img), np.max(img)
                grid[y0:y1, x0:x1] = 255.0 * (img - low) / (high - low)
                next_idx += 1
            x0 += W + 1
            x1 += W + 1
        y0 += H + 1
        y1 += H + 1

    return grid


def save_data_pickle(data, file_path):
    with open(file_path, 'wb') as f:
        pickle.dump(data, f)

def load_pickle(file_path):
    with open(file_path, 'rb') as f:
        return pickle.load(f)
    
def load_data_from_pickle(index):
    # Define the file paths based on provided names
    train_data_path = '../SE4AI_data/x_train'+str(index)+'.pickle'
    validation_data_path = '../SE4AI_data/x_val'+str(index)+'.pickle'
    test_data_path = '../SE4AI_data/x_test'+str(index)+'.pickle'

    train_label_path = '../SE4AI_data/y_train'+str(index)+'.pickle'
    validation_label_path = '../SE4AI_data/y_val'+str(index)+'.pickle'
    test_label_path = '../SE4AI_data/y_test'+str(index)+'.pickle'

    # Load datasets
    x_train = load_pickle(train_data_path)
    x_val = load_pickle(validation_data_path)
    x_test = load_pickle(test_data_path)

    # Load labels
    y_train = load_pickle(train_label_path)
    y_val = load_pickle(validation_label_path)
    y_test = load_pickle(test_label_path)

    return x_train, y_train, x_val, y_val, x_test, y_test
