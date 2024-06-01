import pickle
import os
from tensorflow.keras.utils import to_categorical
import numpy as np
import matplotlib.pyplot as plt

# Replace with your own database download directory
# base_path = 'E:/input'
base_path = r'C:\Users\kfrei\OneDrive - Ostbayerische Technische Hochschule Regensburg\Desktop\input'

# Opening file for reading in binary mode
file_path = os.path.join(base_path, 'data2.pickle')
with open(file_path, 'rb') as f:
    data = pickle.load(f, encoding='latin1')  # dictionary type

data['y_train'] = to_categorical(data['y_train'], num_classes=43)
data['y_validation'] = to_categorical(data['y_validation'], num_classes=43)
data['x_train'] = data['x_train'].transpose(0, 2, 3, 1)
data['x_validation'] = data['x_validation'].transpose(0, 2, 3, 1)
data['x_test'] = data['x_test'].transpose(0, 2, 3, 1)

print(f"{data['x_train'].shape=}")
print(f"{data['x_validation'].shape=}")
print(f"{data['x_test'].shape=}")

# Compute the average images
avg_image_train = np.mean(data['x_train'], axis=0)
avg_image_validation = np.mean(data['x_validation'], axis=0)
avg_image_test = np.mean(data['x_test'], axis=0)

# Plot all average images in one figure
fig, axs = plt.subplots(1, 3, figsize=(15, 5))

axs[0].imshow(avg_image_train.astype('uint8'))
axs[0].set_title('Average Image of x_train')
axs[0].axis('off')

axs[1].imshow(avg_image_validation.astype('uint8'))
axs[1].set_title('Average Image of x_validation')
axs[1].axis('off')

axs[2].imshow(avg_image_test.astype('uint8'))
axs[2].set_title('Average Image of x_test')
axs[2].axis('off')

plt.tight_layout()
plt.show()