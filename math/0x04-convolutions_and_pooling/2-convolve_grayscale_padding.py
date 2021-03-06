#!/usr/bin/env python3
"""Padding"""

import numpy as np


def convolve_grayscale_padding(images, kernel, padding):
    """Padding"""

    m, h, w = images.shape
    kh, kw = kernel.shape
    ph, pw = padding

    padded_img = np.pad(images, ((0, 0), (ph, ph), (pw, pw)), 'constant')

    ch = h + 2 * ph - kh + 1
    cw = w + 2 * pw - kw + 1

    convolved = np.zeros((m, ch, cw))

    for j in range(ch):
        for k in range(cw):
            images_slide = padded_img[:, j:j + kh, k:k + kw]
            elem_mul = np.multiply(images_slide, kernel)
            convolved[:, j, k] = elem_mul.sum(axis=1).sum(axis=1)

    return convolved
