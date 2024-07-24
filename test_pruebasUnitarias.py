import pytest
import numpy as np
import cv2
from preprocess_img import preprocess

def test_preprocess_normalization():
    input_array = np.random.randint(0, 256, (256, 256, 3), dtype=np.uint8)
    output_array = preprocess(input_array)
    assert np.all(output_array >= 0) and np.all(output_array <= 1)