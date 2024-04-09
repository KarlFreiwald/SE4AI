import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, accuracy_score


def plot_confusion_matrices(y_train, y_pred_train, y_test, y_pred_test):

    conf_matrix_train = confusion_matrix(y_train, y_pred_train)
    conf_matrix_test = confusion_matrix(y_test, y_pred_test)

    accuracy_train = accuracy_score(y_train, y_pred_train)
    accuracy_test = accuracy_score(y_test, y_pred_test)

    # Set up the matplotlib figure
    plt.figure(figsize=(8, 4))

    # Plot confusion matrix for the training set
    plt.subplot(1, 2, 1)
    sns.heatmap(conf_matrix_train, annot=True, fmt='g', cmap='Blues', cbar=False)
    plt.xlabel('Predicted labels')
    plt.ylabel('True labels')
    plt.title(f'Training Set Accuracy: {accuracy_train:.2f}')

    # Plot confusion matrix for the test set
    plt.subplot(1, 2, 2)
    sns.heatmap(conf_matrix_test, annot=True, fmt='g', cmap='Blues', cbar=False)
    plt.xlabel('Predicted labels')
    plt.ylabel('True labels')
    plt.title(f'Test Set Accuracy: {accuracy_test:.2f}')

    plt.tight_layout()
    plt.show()
