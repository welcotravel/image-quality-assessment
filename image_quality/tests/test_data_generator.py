
import os
import unittest
import numpy as np
from image_quality.handlers.data_generator import TrainDataGenerator, TestDataGenerator


IMG_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'test_images')
N_CLASSES = 10
BATCH_SIZE = 2
BASENET_PREPROCESS = lambda x: x
TEST_SAMPLES = [
  {
    'image_id': '42039.jpg',
    'label': [0, 5, 10, 28, 54, 31, 12, 3, 3, 2]
  },
  {
    'image_id': '42040.jpg',
    'label': [0, 5, 10, 28, 54, 31, 12, 3, 3, 2]
  },
  {
    'image_id': '42041.jpg',
    'label': [0, 5, 10, 28, 54, 31, 12, 3, 3, 2]
  },
  {
    'image_id': '42042.jpg',
    'label': [0, 5, 10, 28, 54, 31, 12, 3, 3, 2]
  },
  {
    'image_id': '42044.jpg',
    'label': [0, 5, 10, 28, 54, 31, 12, 3, 3, 2]
  },
]


class TestTrainDataGenerator(unittest.TestCase):

  def test_train_data_generator(self):
    dg = TrainDataGenerator(TEST_SAMPLES, IMG_DIR, BATCH_SIZE, N_CLASSES, BASENET_PREPROCESS,
                shuffle=False)
    X, y = dg.__getitem__(0)

    # test image dimensions
    expected = (BATCH_SIZE, 224, 224, 3)
    self.assertEqual(X.shape, expected)

    # test label dimensions
    expected = (BATCH_SIZE, 10)
    self.assertEqual(y.shape, expected)

    # test that label is probability distribution
    expected = np.array([1, 1])
    np.testing.assert_array_almost_equal(np.sum(y, axis=1), expected)

    # test that last batch has 1 sample only
    X, y = dg.__getitem__(2)
    expected = 1
    self.assertEqual(X.shape[0], expected)

    # test number of batches
    expected = 3
    self.assertEqual(dg.__len__(), expected)

  def test_test_data_generator(self):
    dg = TestDataGenerator(TEST_SAMPLES, IMG_DIR, BATCH_SIZE, N_CLASSES, BASENET_PREPROCESS)
    X, y = dg.__getitem__(0)

    # test image dimensions
    expected = (BATCH_SIZE, 224, 224, 3)
    self.assertEqual(X.shape, expected)

    # test label dimensions
    expected = (BATCH_SIZE, 10)
    self.assertEqual(y.shape, expected)

    # test that label is probability distribution
    expected = np.array([1, 1])
    np.testing.assert_array_almost_equal(np.sum(y, axis=1), expected)

    # test that last batch has 1 sample only
    X, y = dg.__getitem__(2)
    expected = 1
    self.assertEqual(X.shape[0], expected)

    # test number of batches
    expected = 3
    self.assertEqual(dg.__len__(), expected)
