import tensorflow as tf
import tensorflow.keras as keras
import numpy as np
from collect import get_collect


#Описание модели
def cnn_model_fn(features, labels, mode):
    # Входной слой
    input_layer = tf.reshape(features["x"], [-1, 24, 24, 1])

    # Слой свёртки #1 с relu
    conv1 = tf.layers.conv2d(
        inputs=input_layer,
        filters=32,
        kernel_size=[3, 3],
        padding="same",
        activation=tf.nn.relu)

    # Слой макспулинга #1
    pool1 = tf.layers.max_pooling2d(inputs=conv1, pool_size=[2, 2], strides=2)

    # Слой свёртки #2 c сигмоидой
    conv2 = tf.layers.conv2d(
        inputs=pool1,
        filters=64,
        kernel_size=[5, 5],
        padding="same",
        activation=tf.nn.sigmoid)

    # Слой макспулинга #2
    pool2 = tf.layers.max_pooling2d(inputs=conv2, pool_size=[2, 2], strides=2)

    # Полносвязный слой
    pool2_flat = tf.reshape(pool2, [-1, 6 * 6 * 64])
    dense = tf.layers.dense(inputs=pool2_flat, units=1024, activation=tf.nn.relu)
    dropout = tf.layers.dropout(
        inputs=dense, rate=0.4, training=mode == tf.estimator.ModeKeys.TRAIN)

    logits = tf.layers.dense(inputs=dropout, units=5)

    # Генерация предиктов
    predictions = {
        "classes": tf.argmax(input=logits, axis=1),
        "probabilities": tf.nn.softmax(logits, name="softmax_tensor"),
    }

    # Анализ сэмпла
    if mode == tf.estimator.ModeKeys.PREDICT:
        return tf.estimator.EstimatorSpec(mode=mode, predictions=predictions)

    # Вычисление ошибки
    loss = tf.losses.sparse_softmax_cross_entropy(labels=labels, logits=logits)

    # Тренировка модели
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

#Использование модели
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
            #y=eval_labels,
            num_epochs=1,
            shuffle=False)

        return mnist_classifier.predict(input_fn=eval_input_fn)
