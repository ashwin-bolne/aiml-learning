from typing import Dict 

import numpy as np 
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score,
)


def evaluate_regression(
        y_true,
        y_pred,
        n_features: int,
) -> Dict[str, float]:
    """
    Evaluate regression model performance using common regression metrics.

    Args:
        y_true (array-like): Actual target values.

        y_pred (array-like): Predicted target values from model.

        n_features (int): Number of input features used in the model.

    Returns
    Dict[str, float]: Dictionary containing regression evaluation metrics.
    """
    mse = mean_squared_error(y_true, y_pred)
    
    rmse = np.sqrt(mse)
    
    mae = mean_absolute_error(y_true, y_pred)
    
    r2 = r2_score(y_true, y_pred)
    
    n_samples = len(y_true)

    adjusted_r2 = 1 - (
        (1 - r2) * (n_samples - 1)
        / (n_samples - n_features - 1)
    )

    return {
        "mse": mse,
        "rmse": rmse,
        "mae": mae,
        "r2": r2,
        "adjusted_r2": adjusted_r2,
    }