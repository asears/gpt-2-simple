# import os

# from unittest import TestCase, mock
# from unittest.mock import MagicMock
# from unittest.mock import patch

# import json

# import warnings

# warnings.filterwarnings('ignore', category=DeprecationWarning)
# warnings.filterwarnings('ignore', category=FutureWarning)

# # Disable tensorflow DeprecationWarning: the imp module is deprecated in favour of importlib; see the module's documentation for alternative uses
# os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 

# import tensorflow as tf

# from gpt_2_simple.src import memory_saving_gradients as msg

# class TestMemorySavingGradients(TestCase):
#     def test_gradients_speed(self):
#         tf.compat.v1.disable_eager_execution()
#         ys = [tf.Variable(1.)]
#         xs = ""
#         grad_ys = ""

#         result = msg.gradients_speed(ys, xs, grad_ys, test="123")
    
#     def test_gradients_memory(self):
#         tf.compat.v1.disable_eager_execution()
#         ys = [tf.Variable(1.)]
#         xs = ""
#         grad_ys = ""

#         result = msg.gradients_memory(ys, xs, grad_ys, test="123")

#     def test_gradients_collection(self):
#         tf.compat.v1.disable_eager_execution()
#         ys = [tf.Variable(1.)]
#         xs = ""
#         grad_ys = ""

#         result = msg.gradients_collection(ys, xs, grad_ys, test="123")

#     def test_gradients(self):
#         tf.compat.v1.disable_eager_execution()
#         ys = [tf.Variable(1.)]
#         xs = ""
#         grad_ys = ""

#         result = msg.gradients(ys, xs, grad_ys, checkpoints, test="123")

# # fixdims

#     def test_tf_toposort(self):
#         ts = ""
#         within_ops = ""

#         result = msg.tf_toposort(ts, within_ops)

#     def test_fast_backward_ops(self):
#         within_ops = ""
#         seed_ops = ""
#         stop_at_ts = ""

#         result = msg.fast_backward_ops(within_ops, seed_ops, stop_at_ts)

#     def test_capture_ops(self):
#         within_ops = ""
#         seed_ops = ""
#         stop_at_ts = ""

#         result = msg.capture_ops()

#     def test__to_op(self):
#         tensor_or_op = ""
#         result = msg._to_op(tensor_or_op)

#     def test__to_ops(self):
#         iterable = ""
#         result = msg._to_ops(iterable)

#     def test__is_iterable(self):
#         o = ""
#         result = msg._is_iterable(o)

#     def test_debug_print(self):
#         s = ""
#         result = msg.debug_print(s, "abc")

#     def test_format_ops(self):
#         ops = ""
#         sort_outputs = ""
#         result = msg.format_ops(ops, sort_outputs)

#     def test_my_add_control_inputs(self):
#         wait_to_do_ops=""
#         inputs_to_do_before=""
#         result = msg.my_add_control_inputs(wait_to_do_ops, inputs_to_do_before)