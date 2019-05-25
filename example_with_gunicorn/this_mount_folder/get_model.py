import os, sys
PROJECT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(PROJECT_PATH)

from keras.models import load_model
import numpy as np
import keras.backend as K
import tensorflow as tf


# Объявляем метрики, которые нам вдальнейшем понадобятся:
def dice_coef_np(y_true, y_pred, smooth=1):
    intersection = (y_true.flatten() * y_pred.flatten()).sum()
    return -(2. * intersection + smooth) / (y_true.sum() + y_pred.sum() + smooth)


def dice_coef_batch(y_true_in, y_pred_in):
    y_pred_in = (y_pred_in > 0.5).astype(np.float32)  # added by sgx 20180728
    batch_size = y_true_in.shape[0]
    metric = []
    for batch in range(batch_size):
        value = dice_coef_np(y_true_in[batch], y_pred_in[batch])
        metric.append(value)
    return np.mean(metric)


def my_dice_metric(label, pred):
    metric_value = tf.py_func(dice_coef_batch, [label, pred], tf.float64)
    return metric_value


def dice_coef_K(y_true, y_pred, smooth=1):
    y_true_f = K.flatten(y_true)
    y_pred_f = K.flatten(y_pred)
    intersection = K.sum(y_true_f * y_pred_f)
    return (2. * intersection + smooth) / (K.sum(y_true_f) + K.sum(y_pred_f) + smooth)


def get_model(model_name):
    model = load_model(os.path.join(PROJECT_PATH, 'models', model_name), custom_objects={'dice_coef_K': dice_coef_K, 'my_dice_metric': my_dice_metric})
    model._make_predict_function()
    graph = tf.get_default_graph()
    print('Model read!')
    return model, graph
