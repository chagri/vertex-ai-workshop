

# Copyright 2021 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#            http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and

import tensorflow as tf
from tensorflow import keras

from absl import app
from absl import flags
from absl import logging

FEATURE_NAMES = [
    "trip_month",
    "trip_day",
    "trip_day_of_week",
    "trip_hour",
    "trip_seconds",
    "trip_miles",
    "payment_type",
    "pickup_grid",
    "dropoff_grid",
    "euclidean",
    "loc_cross",
]

TARGET_FEATURE_NAME = "tip_bin"

TARGET_LABELS = ["tip<20%", "tip>=20%"]

NUMERICAL_FEATURE_NAMES = [
    "trip_seconds",
    "trip_miles",
    "euclidean",
]

EMBEDDING_CATEGORICAL_FEATURES = {
    "trip_month": 2,
    "trip_day": 4,
    "trip_hour": 3,
    "pickup_grid": 3,
    "dropoff_grid": 3,
    "loc_cross": 10,
}

ONEHOT_CATEGORICAL_FEATURE_NAMES = ["payment_type", "trip_day_of_week"]

def create_model_inputs():
    inputs = {}
    for name in NUMERICAL_FEATURE_NAMES:
        inputs[name] = keras.layers.Input(name=name, shape=[], dtype=tf.float32)
    for name in list(EMBEDDING_CATEGORICAL_FEATURES.keys()) + ONEHOT_CATEGORICAL_FEATURE_NAMES:
        inputs[name] = keras.layers.Input(name=name, shape=[], dtype=tf.int64)
    return inputs


def main(argv):
    del argv
    
    inputs = create_model_inputs()
    print(inputs)

if __name__ == '__main__':
    logging.set_verbosity(logging.INFO)
    app.run(main)
