from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.immi5 import immi5


def test_immi5():
  """Test module immi5.py by downloading
   immi5.csv and testing shape of
   extracted data has 2485 rows and 5 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = immi5(test_path)
  try:
    assert x_train.shape == (2485, 5)
  except:
    shutil.rmtree(test_path)
    raise()
