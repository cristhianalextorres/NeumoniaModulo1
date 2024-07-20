
import tensorflow as tf #Se agrega
import tensorflow.keras.backend as K #Se instala por intuición
tf.compat.v1.disable_eager_execution()
tf.compat.v1.experimental.output_all_intermediates(True)

def model_fun():
    model = tf.keras.models.load_model('conv_MLP_84.h5')
    if not model.compiled_loss:
        loss = tf.keras.losses.CategoricalCrossentropy(reduction=tf.keras.losses.Reduction.SUM_OVER_BATCH_SIZE)
        model.compile(optimizer='adam', loss=loss)

    return model