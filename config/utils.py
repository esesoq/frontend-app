import os
import logging
from typing import List, Tuple

# Set up logging configuration
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

def get_current_directory() -> str:
    """Returns the current working directory."""
    return os.getcwd()

def get_current_script_path() -> str:
    """Returns the path of the current script."""
    return os.path.abspath(__file__)

def get_script_directory() -> str:
    """Returns the directory of the current script."""
    return os.path.dirname(get_current_script_path())

def get_project_root() -> str:
    """Returns the root directory of the project."""
    return os.path.dirname(get_script_directory())

def get_asset_path(asset_name: str) -> str:
    """Returns the path to a static asset."""
    return os.path.join(get_project_root(), 'static', asset_name)

def get_template_path(template_name: str) -> str:
    """Returns the path to a template file."""
    return os.path.join(get_project_root(), 'templates', template_name)

def get_config_path(config_name: str) -> str:
    """Returns the path to a configuration file."""
    return os.path.join(get_project_root(), 'config', config_name)

def get_environment_variable(var_name: str) -> str:
    """Returns the value of an environment variable."""
    return os.environ.get(var_name)

def get_user_home() -> str:
    """Returns the user's home directory."""
    return os.path.expanduser('~')