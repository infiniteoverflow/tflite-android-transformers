import tensorflow as tf
from transformers import TFDistilBertForQuestionAnswering

model = TFDistilBertForQuestionAnswering.from_pretrained('distilbert-base-uncased-distilled-squad')

input_spec = tf.TensorSpec([1, 384], tf.int32)
model._set_inputs(input_spec, training=False)

print(model.inputs)
print(model.outputs)

converter = tf.lite.TFLiteConverter.from_keras_model(model)
converter.target_spec.supported_ops = [tf.lite.OpsSet.SELECT_TF_OPS]

tflite_model = converter.convert()

open("distilbert-squad-384.tflite", "wb").write(tflite_model)
