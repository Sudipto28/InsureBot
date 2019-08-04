from rasa_nlu.converters import load_data
from rasa_nlu.config import RasaNLUConfig
from rasa_nlu.model import Trainer, Metadata,Interpreter


def train_nlu(data, config, model_dir):
    training_data = load_data(data)
    trainer = Trainer(RasaNLUConfig(config))
    trainer.train(training_data)
    trainer.persist(model_dir, fixed_model_name='insurancenlu')


def run_nlu():
    interpreter = Interpreter.load('./models/nlu/default/insurancenlu', RasaNLUConfig('config.json'))
    print(interpreter.parse(u"I wonder what are the insurance plans available in India"))


if __name__ == '__main__':
    train_nlu('./data/data.json', 'config.json', './models/nlu')
    run_nlu()
