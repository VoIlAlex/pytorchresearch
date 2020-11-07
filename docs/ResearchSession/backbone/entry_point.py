import os
import sys

import pytorchresearch as ptr
from . import config as cfg

script_dir = os.path.dirname(os.path.abspath(__file__))
backbone_dir = os.path.dirname(script_dir)
project_dir = os.path.dirname(backbone_dir)
sys.path.insert(0, project_dir)

import importlib.util


def import_module(path: str):
    file_name = os.path.split(path)[-1]
    module_name, ext = os.path.splitext(file_name)
    spec = importlib.util.spec_from_file_location(module_name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def import_everything(path: str):
    config_paths = [file for file in os.listdir(path) if file.endswith('config.py')]
    config_paths = [os.path.join(
        cfg.RESEARCH_CONFIG_DIR,
        file
    ) for file in config_paths if os.path.isfile(
        os.path.join(
            cfg.RESEARCH_CONFIG_DIR,
            file
        )
    )]
    configs = []
    for config_path in config_paths:
        config = import_module(config_path)
        configs.append(config)
    return configs


def main():
    import pprint
    configs = import_everything(cfg.RESEARCH_CONFIG_DIR)
    pprint.pprint([getattr(config, 'RESEARCH_SESSION_CONFIG') for config in configs])
