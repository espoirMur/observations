from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.greene import greene


def test_greene():
  """Test module greene.py by downloading
   greene.csv and testing shape of
   extracted data has 384 rows and 7 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = greene(test_path)
  try:
    assert x_train.shape == (384, 7)
  except:
    shutil.rmtree(test_path)
    raise()
