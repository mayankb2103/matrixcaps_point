import tensorflow as tf

flags = tf.app.flags

############################
#    hyper parameters      #
############################
flags.DEFINE_float('ac_lambda0', 0.01, '\lambda in the activation function a_c, iteration 0')
flags.DEFINE_float('ac_lambda_step', 0.01,
                   'It is described that \lambda increases at each iteration with a fixed schedule, however specific super parameters is absent.')

flags.DEFINE_integer('batch_size',2, 'batch size')
flags.DEFINE_integer('epoch', 3, 'epoch')
flags.DEFINE_integer('iter_routing', 2, 'number of iterations')
flags.DEFINE_float('m_schedule', 0.2, 'the m will get to 0.9 at current epoch')
flags.DEFINE_float('epsilon', 1e-9, 'epsilon')
flags.DEFINE_float('m_plus', 0.9, 'the parameter of m plus')
flags.DEFINE_float('m_minus', 0.1, 'the parameter of m minus')
flags.DEFINE_float('lambda_val', 0.5, 'down weight of the loss for absent digit classes')
flags.DEFINE_boolean('weight_reg', True, 'train with regularization of weights')
flags.DEFINE_string('norm', 'norm2', 'norm type')
################################
#    structure parameters      #
################################
flags.DEFINE_integer('A', 32, 'number of channels in output from ReLU Conv1')
flags.DEFINE_integer('B', 4, 'number of capsules in output from PrimaryCaps')
flags.DEFINE_integer('C', 4, 'number of channels in output from ConvCaps1')
flags.DEFINE_integer('D', 4, 'number of channels in output from ConvCaps2')

############################
#   environment setting    #
############################
flags.DEFINE_string('dataset', 'data/mnist', 'the path for dataset')
flags.DEFINE_string('dataset_fashion_mnist', 'data/fashion_mnist', 'the path for dataset')
flags.DEFINE_boolean('is_train', True, 'train or predict phase')
flags.DEFINE_integer('num_threads', 8, 'number of threads of enqueueing exampls')
flags.DEFINE_string('logdir', 'logdir', 'logs directory')
flags.DEFINE_string('test_logdir', 'test_logdir', 'test logs directory')

############################
#   modelnet40 setting    #
############################
flags.DEFINE_string('dataset_modelnet40', 'data/modelnet40', 'the path for dataset')
flags.DEFINE_integer('modelnet_num_point', 1024, 'number of 3D points in pointcloud of a shape ')
flags.DEFINE_boolean('is_64', False, 'Whether to include 64 transform layer in network or not')
flags.DEFINE_boolean('decoder', False, 'Whether to include decoder in network or not')



cfg = tf.app.flags.FLAGS

def get_coord_add(dataset_name: str):
    import numpy as np
    # TODO: get coord add for cifar10/100 datasets (32x32x3)
    options = {'mnist': ([[[8., 8.], [12., 8.], [16., 8.]],
                          [[8., 12.], [12., 12.], [16., 12.]],
                          [[8., 16.], [12., 16.], [16., 16.]]], 28.),
               'smallNORB': ([[[8., 8.], [12., 8.], [16., 8.], [24., 8.]],
                              [[8., 12.], [12., 12.], [16., 12.], [24., 12.]],
                              [[8., 16.], [12., 16.], [16., 16.], [24., 16.]],
                              [[8., 24.], [12., 24.], [16., 24.], [24., 24.]]], 32.),
               'modelnet40': ([[[8., 8.], [12., 8.], [16., 8.], [24., 8.]],
                              [[8., 12.], [12., 12.], [16., 12.], [24., 12.]],
                              [[8., 16.], [12., 16.], [16., 16.], [24., 16.]],
                              [[8., 24.], [12., 24.], [16., 24.], [24., 24.]]], 32.)
               #tempry coord addition for modelnet40, cloned of smallNORB
               }
    coord_add, scale = options[dataset_name]

    coord_add = np.array(coord_add, dtype=np.float32) / scale

    return coord_add

#no. of training samples, testing samples and classes in modelnet40: 9840, 2468 and 40
def get_dataset_size_train(dataset_name: str):
    options = {'mnist': 55000, 'fashion_mnist': 55000,
                'cifar10': 50000, 'cifar100': 50000,
               'smallNORB': 23400 * 2,'modelnet40': 9840
               }

    return options[dataset_name]


def get_dataset_size_test(dataset_name: str):
    options = {'mnist': 10000, 'fashion_mnist': 10000,
               'cifar10': 10000, 'cifar100': 10000,
               'smallNORB': 23400 * 2,'modelnet40':2468}
    return options[dataset_name]


def get_num_classes(dataset_name: str):
    options = {'mnist': 10,'fashion_mnist': 10,
                'cifar10': 10, 'cifar100': 100,
                'smallNORB': 5, 'modelnet40' : 40}
    return options[dataset_name]


from utils import create_inputs_mnist, create_inputs_norb, create_inputs_modelnet40

#calling create_inputs_modelnet40 from utils
def get_create_inputs(dataset_name: str, is_train: bool, epochs: int):
    options = {'mnist': lambda: create_inputs_mnist(is_train),
               'fashion_mnist': lambda: create_inputs_mnist(is_train),
               'smallNORB': lambda: create_inputs_norb(is_train, epochs),
               'modelnet40': lambda : create_inputs_modelnet40(is_train)}
    return options[dataset_name]
