import os
import yaml

class Configuration:
    def __init__(self):
        self.config = None
        self.load_config()

    def load_config(self):
        config_dir = '/home/jovyan/work/week12/homework8/config'
        config_file = os.path.join(config_dir, 'config.yml')
        with open(config_file, 'r') as f:
            self.config = yaml.safe_load(f)

    def get_config(self, key):
        return self.config[key] if key in self.config else None