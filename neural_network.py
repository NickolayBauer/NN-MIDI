import tensorflow as tf
import tensorflow.keras as keras
import numpy as np
from collect import get_collect
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 

########################################################################
#
# Используемые функции:
# cnn_model_fn – описание модели нейронной сети;
# lets_go – использование модели нейронной сети.
#
########################################################################

########################################################################
#
# cnn_model_fn – описание модели нейронной сети.
#
########################################################################
#
# Используемые переменные:
# features - создание свойств для метки;
# labels - метки обучения;
# mode - режим использования;
# сonv1 - первый свёрточный слой;
# input_layer - входной слой;
# pool1 - первый слой макспулинга;
# conv2 - второй свёрточный слой;
# pool2 - второй слой макспулинга;
# pool2_flat - сглаженная матрица;
# dense - полносвязный слой;
# dropout - слой дропаута;
# logits - логистический слой;
# predictions - хранит сформированный прогнозы;
# loss - накопленная ошибка;
# optimizer - оптмизация обучения;
# learning_rate - коэфициент обучения;
# train_op - содержит процесс тренировки;
# global_step - шаг обучения;
# eval_metric_ops - сформированные метрики;
# inputs - входы в слой;
# filters - фильтры слоя;
# kernel_size - окно свёртки;
# padding - способ свёртки;
# activations - функция активации;
# pool_size - окно макспулинга;
# strides - коэфициент уменьшения данных;
# unints - количество нейронов;
# rate - процент выборки нейронов;
# training - содержит режим работы;
# axis - оси метрики;
# name - имя метрики.
#
########################################################################

def cnn_model_fn(features, labels, mode):
    input_layer = tf.reshape(features["x"], [-1, 24, 24, 1])

    conv1 = tf.layers.conv2d(
        inputs=input_layer,
        filters=32,
        kernel_size=[3, 3],
        padding="same",
        activation=tf.nn.relu)

    pool1 = tf.layers.max_pooling2d(inputs=conv1, pool_size=[2, 2], strides=2)

    conv2 = tf.layers.conv2d(
        inputs=pool1,
        filters=64,
        kernel_size=[5, 5],
        padding="same",
        activation=tf.nn.sigmoid)

    pool2 = tf.layers.max_pooling2d(inputs=conv2, pool_size=[2, 2], strides=2)

    pool2_flat = tf.reshape(pool2, [-1, 6 * 6 * 64])
    dense = tf.layers.dense(inputs=pool2_flat, units=1024, activation=tf.nn.relu)
    dropout = tf.layers.dropout(
        inputs=dense, rate=0.4, training=mode == tf.estimator.ModeKeys.TRAIN)

    logits = tf.layers.dense(inputs=dropout, units=5)

    predictions = {
        "classes": tf.argmax(input=logits, axis=1),
        "probabilities": tf.nn.softmax(logits, name="softmax_tensor"),
    }

    if mode == tf.estimator.ModeKeys.PREDICT:
        return tf.estimator.EstimatorSpec(mode=mode, predictions=predictions)

    loss = tf.losses.sparse_softmax_cross_entropy(labels=labels, logits=logits)

    if mode == tf.estimator.ModeKeys.TRAIN:
        optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.001)
        train_op = optimizer.minimize(
            loss=loss,
            global_step=tf.train.get_global_step())
        return tf.estimator.EstimatorSpec(mode=mode, loss=loss, train_op=train_op)

    eval_metric_ops = {
        "accuracy": tf.metrics.accuracy(
            labels=labels, predictions=predictions["classes"])
    }

    return tf.estimator.EstimatorSpec(
        mode=mode, loss=loss, eval_metric_ops=eval_metric_ops)

########################################################################
#
# lets_go – использование модели нейронной сети.
#
########################################################################
# 
# Используемые переменные:
# init - инициализация модели;
# data_edu - данные для обучения;
# label_edu - метки для обучения;
# data_word - данные для работы;
# mnist_classifier - использование модели;
# tensors_to_log - логи метрик;
# logging_hook - оформление метрик;
# train_input_fn - входной слой тренировки;
# eval_input_fn - входной слой работы;
# result - данные о результатах;
# batch_size - размер тренировочной партии;
# x - данные;
# y - метки;
# shuffle - нужно ли перетасовать выборку;
# input_fn - входной слой;
# steps - количество шагов.
#
########################################################################

def lets_go(mode):
    init = tf.global_variables_initializer()

    data_edu, label_edu, data_work = get_collect()

    data_edu = data_edu/np.float32(255)
    data_work = data_work/np.float32(255)
    label_edu = label_edu.astype(np.int32)
    
    mnist_classifier = tf.estimator.Estimator(
        model_fn=cnn_model_fn, model_dir="results")

    tensors_to_log = {"probabilities": "softmax_tensor"}

    logging_hook = tf.train.LoggingTensorHook(
        tensors=tensors_to_log, every_n_iter=50)

    if mode == "train":
        train_input_fn = tf.estimator.inputs.numpy_input_fn(
            x={"x": data_edu},
            y=label_edu,
            batch_size=100,
            num_epochs=None,
            shuffle=True)

        mnist_classifier.train(
           input_fn=train_input_fn,
           steps=1,
           hooks=[logging_hook])

        mnist_classifier.train(input_fn=train_input_fn, steps=1000)

    if mode == "work":
        eval_input_fn = tf.estimator.inputs.numpy_input_fn(
            x={"x": data_work},
            num_epochs=1,
            shuffle=False)
        result = mnist_classifier.predict(input_fn=eval_input_fn)
        return result
