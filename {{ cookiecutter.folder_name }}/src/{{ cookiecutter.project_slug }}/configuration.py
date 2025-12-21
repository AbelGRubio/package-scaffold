{% if cookiecutter.use_config_file.lower() == "yes" %}import configparser{% endif %}
import os
from typing import List
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


__version__ = "{{ cookiecutter.version }}"



class Settings(BaseSettings):
    """
    Configuración global de la aplicación.
    Prioridad: 1. Variables de entorno → 2. Archivo .cfg → 3. Valores por defecto
    """
    model_config = SettingsConfigDict(
        env_file=".env",             
        env_file_encoding="utf-8",
        env_prefix="",             
        env_ignore_empty=True,
        case_sensitive=False,
        extra="ignore",
    )

    debug: bool = False

    basic: str = ''

    {% if cookiecutter.use_config_file.lower() == "yes" %}
    # Ruta al archivo de configuración
    conf_file: str = Field(default='./conf/config.cfg', validation_alias='CONF_FILE')

    def __init__(self, **data):
        super().__init__()

        # Leer el archivo .cfg solo si existe
        if os.path.exists(self.conf_file):
            parser = configparser.ConfigParser()
            parser.read(self.conf_file)

            # Actualizar valores desde el .cfg (si no fueron sobreescritos por env)
            self._update_from_ini(parser)

    def _update_from_ini(self, parser: configparser.ConfigParser):
        """Actualiza los atributos desde el archivo .cfg si no fueron seteados por entorno."""
        section = "conf"

        # CORS_ORIGINS
        if "cors_origins" in parser[section]:
            cors_str = parser[section]["cors_origins"].strip()
            if cors_str:
                self.cors_origins = [
                    origin.strip() for origin in cors_str.split(",") if origin.strip()
                ]

        # Puedes añadir más campos aquí según necesites
        if "basic" in parser[section]:
            self.basic = parser[section]["basic"]


    @property
    def cors_origins_clean(self) -> List[str]:
        return [o.strip() for o in self.cors_origins if o.strip()]

    {% endif %}


SETTINGS = Settings()