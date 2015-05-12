import logging
import logging.config
import os

from utils import load_yaml

home = os.path.dirname(os.path.abspath(__file__))
logger = logging.getLogger(__name__)


def load_config_data(env):

    c = {
        'env': env
    }

    config_loc = '{home}/config/{env}.yaml'.format(home=home, env=env)
    private_loc = '{home}/config/private.yaml'.format(home=home)

    c.update(load_yaml(config_loc) or {})
    c.update(load_yaml(private_loc) or {})

    return c, config_loc, private_loc


def setup_logging(logger_config):
    logging.config.dictConfig(logger_config)


# Reads in config based on env, sets up logging
# Then logs out the setup that just happened
def setup():

    env = os.environ.get('env', 'devel')

    conf, config_loc, private_loc = load_config_data(env)
    setup_logging(conf.get('logging', {}))

    logger.info('Server starting up...')
    logger.info('Environment set to %s', conf.get('env'))
    if not os.environ.get('env'):
        logger.warn('Environment set to %s by default - no "env" system property found!', env)
    logger.info('Loaded configs from %s', config_loc)
    logger.info('Loaded config from %s', private_loc)

    return conf


config = setup()
