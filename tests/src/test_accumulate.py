# import os
# from unittest import TestCase, mock
# from unittest.mock import patch

# # Tensorflow warings will kill test discovery and throw spurious errors with py.test, suppress them
# # This shows up as error Error: 2020-03-01 15:43:56.145370: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library cudart64_101.dll
# # Disable tensorflow DeprecationWarning: the imp module is deprecated in favour of importlib; see the module's documentation for alternative uses

# import warnings

# warnings.filterwarnings('ignore', category=DeprecationWarning)
# warnings.filterwarnings('ignore', category=FutureWarning)
# os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

# #tf.logging.set_verbosity(tf.logging.ERROR)
# #tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)

# from gpt_2_simple.src import accumulate

# # TODO Mock tensorflow, external dependencies
# import tensorflow as tf

# #os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 


# class TestAccumulate(TestCase):
#     #@patch('accumulate.AccumulatingOptimizer.__init__', return_value=9)
#     def test_init(self):
#         # TODO This currently has 2 options, enable tests for both or mock out
#         #if optimizer == 'adam':
#         #    opt = tf.compat.v1.train.AdamOptimizer(learning_rate=learning_rate)
#         #elif optimizer == 'sgd':
#         #    opt = tf.compat.v1.train.GradientDescentOptimizer(learning_rate=learning_rate)
#         opt = ""
#         var_list = ""
#         ac = accumulate.AccumulatingOptimizer(opt, var_list)

#     def test_reset(self):
#         opt = ""
#         var_list = ""
#         ac = accumulate.AccumulatingOptimizer(opt, var_list)
#         ac.reset()

#     def test_compute_gradients(self):
#         # TODO Currently complaining about RuntimeError: tf.placeholder() is not compatible with eager execution.
#         tf.compat.v1.disable_eager_execution()

#         learning_rate = ""
#         opt = tf.compat.v1.train.AdamOptimizer(learning_rate=learning_rate)
#         var_list = ""
#         batch_size = None
#         context = tf.compat.v1.placeholder(tf.int32, [batch_size, None])
#         output = ""

#         loss = tf.reduce_mean(
#         input_tensor=tf.nn.sparse_softmax_cross_entropy_with_logits(
#             labels=context[:, 1:], logits=output['logits'][:, :-1]))
        
#         ac = accumulate.AccumulatingOptimizer(opt, var_list)

        
#         ac.compute_gradients(loss)

#     def test_apply_gradients(self):        
#         opt = ""
#         var_list = ""
#         ac = accumulate.AccumulatingOptimizer(opt, var_list)
#         ac.apply_gradients(ac)
