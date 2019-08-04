from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

import logging

from rasa_core.agent import Agent   # train the model
from rasa_core.policies.keras_policy import KerasPolicy     # model used to train the model
from rasa_core.policies.memoization import MemoizationPolicy    # model used to train the model

if __name__ == '__main__':
    logging.basicConfig(level='INFO')

    training_data_file = './data/stories.md'    # Take data for training
    model_path = './models/dialogue'    # Save the model after it is trained

    agent = Agent('insurance_domain.yml', policies=[MemoizationPolicy(), KerasPolicy()])

    agent.train(
        training_data_file,
        augmentation_factor=50,   # No of stories to be created
        max_history=2,  # No of states the model should remember
        epochs=500,     # No of forward and backward passes of training data in the training process
        batch_size=10,  # No of training samples to be parsed in each pass.
        validation_split=0.2)   # percentage of data which should be used to validate the model

    agent.persist(model_path)   # Save the model
