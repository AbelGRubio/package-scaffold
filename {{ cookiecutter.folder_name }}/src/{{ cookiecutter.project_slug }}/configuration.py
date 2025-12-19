{% if cookiecutter.use_config_file.lower() == "yes" %}import configparser{% endif %}
import os

__version__ = {{ cookiecutter.version }}

{% if cookiecutter.use_config_file.lower() == "yes" %}
conf_file = os.getenv("CONF_FILE", "./conf/config.cfg")

config = configparser.ConfigParser()
config.read(conf_file)

basic_ = config.get("conf", "basic", fallback="")
{% endif %}
