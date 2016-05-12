#!/usr/bin/env python
import os
import argparse
import numpy as np
import scipy.misc
import deeppynon as dp
import threading

from web_neural.project.neuralArtistic.cpuver.matconvnetcpu import vgg_net
from web_neural.project.neuralArtistic.cpuver.style_networkcpu import StyleNetwork
from web_neural.project.models import Conversecpu
#from webNeuralArtistic.settings import MEDIA_ROOT

__NEURALDIR__ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def weight_tuple(s):
    try:
        conv_idx, weight = map(float, s.split(','))
        return conv_idx, weight
    except:
        raise argparse.ArgumentTypeError('weights must by "int,float"')

def float_range(x):
    x = float(x)
    if x < 0.0 or x > 1.0:
        raise argparse.ArgumentTypeError("%r not in range [0, 1]" % x)
    return x


def weight_array(weights):
    array = np.zeros(19)
    for idx, weight in weights:
        array[idx] = weight
    norm = np.sum(array)
    if norm > 0:
        array /= norm
    return array


def imread(path):
    return scipy.misc.imread(path).astype(dp.float_)


def imsave(path, img):
    img = np.clip(img, 0, 255).astype(np.uint8)
    scipy.misc.imsave(path, img)
    return path


def to_bc01(img):
    return np.transpose(img, (2, 0, 1))[np.newaxis, ...]


def to_rgb(img):
    return np.transpose(img[0], (1, 2, 0))


def run(args):

    if args.random_seed is not None:
        np.random.seed(args.random_seed)

    layers, pixel_mean = vgg_net(args.network, pool_method=args.pool_method)

    # Inputs
    style_img = imread(args.style) - pixel_mean
    subject_img = imread(args.subject) - pixel_mean
    if args.init is None:
        init_img = subject_img
    else:
        init_img = imread(args.init) - pixel_mean
    noise = np.random.normal(size=init_img.shape, scale=np.std(init_img)*1e-1)
    init_img = init_img * (1 - args.init_noise) + noise * args.init_noise

    # Setup network
    subject_weights = weight_array(args.subject_weights) * args.subject_ratio
    style_weights = weight_array(args.style_weights)
    net = StyleNetwork(layers, to_bc01(init_img), to_bc01(subject_img),
                       to_bc01(style_img), subject_weights, style_weights,
                       args.smoothness)

    # Repaint image
    def net_img():
        return to_rgb(net.image) + pixel_mean

    if not os.path.exists(args.animation):
        os.mkdir(args.animation)

    params = net.params
    learn_rule = dp.Adam(learn_rate=args.learn_rate)
    learn_rule_states = [learn_rule.init_state(p) for p in params]
    
    for i in range(args.iterations):
        file_path = imsave(os.path.join(args.animation, '%.4d.png' % i), net_img())
        condoc = Conversecpu(concpufile= '/' + file_path)
        condoc.save()
        
        cost = np.mean(net.update())
        for param, state in zip(params, learn_rule_states):
            learn_rule.step(param, state)
        print('Iteration: %i, cost: %.4f' % (i, cost))
    imsave(args.output, net_img())


class Runcpu(threading.Thread):
    #__REGISTERED_ = False
            
    def __init__(self):
        #if Run.__REGISTERED_:
        #    return
        threading.Thread.__init__(self)
        self.output = 'outcpu.png'
        self.init = None
        self.init_noise = 0
        self.random_seed = None
        self.animation = 'media/cpuanimation'
        self.iterations = 300
        self.learn_rate= 2.0
        self.smoothness=5e-8
        self.subject_weights=[(9,1)]
        self.style_weights=[(0,1), (2,1), (4,1), (8,1), (12,1)]
        self.subject_ratio=2e-2
        self.pool_method='avg'
        self.network= '/root/git/imagenet-vgg-verydeep-19.mat'
        #Run.__REGISTERED_ = True
        
    def setArg(self, subject, target):
        self.subject = '/root/git/web_neura/web_neural' + str(subject)
        self.style = '/root/git/web_neura/web_neural' + str(target)
          
    def run(self):
        print 'CPU Start background run'  
        run(self)
        print 'CPU Finished background run'  