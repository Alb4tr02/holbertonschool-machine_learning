#!/usr/bin/env python3
"""Grayscale"""

import numpy as np


def convolve_grayscale(images, kernel, padding='same', stride=(1, 1)):
    """Grayscale"""

    m, h, w = images.shape
    kh, kw = kernel.shape
    sh, sw = stride

    ph = 0
    pw = 0

    if padding == 'same':
        ph = int(((h - 1) * sh + kh - h) / 2) + 1
        pw = int(((w - 1) * sw + kw - w) / 2) + 1

    if type(padding) == tuple:
        ph, pw = padding

    padded_img = np.pad(images, ((0, 0), (ph, ph), (pw, pw)), 'constant')

    ch = int(((h + 2 * ph - kh) / sh) + 1)
    cw = int(((w + 2 * pw - kw) / sw) + 1)

    convolved = np.zeros((m, ch, cw))

    for j in range(ch):
        for k in range(cw):
            images_slide = padded_img[:,
                                      j * sh:j * sh + kh,
                                      k * sw:k * sw + kw]

            elem_mul = np.multiply(images_slide, kernel)
            convolved[:, j, k] = elem_mul.sum(axis=1).sum(axis=1)

    return convolved
