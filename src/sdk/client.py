import sys
import platform
from core import *
from secrets_api import Secrets

SDK_LANGUAGE = "Python"
SDK_VERSION = "0010001"  # v0.1.0
DEFAULT_INTEGRATION_NAME = "Unknown"
DEFAULT_INTEGRATION_VERSION = "Unknown"
DEFAULT_REQUEST_LIBRARY = "net/http"
DEFAULT_OS_VERSION = "0.0.0"


class Client:
    def __init__(self, auth, integration_name, integration_version):
        self.config = NewDefaultConfig(auth=auth, integration_name=integration_name, integration_version=integration_version),
        self.secrets = Secrets(client_id=InitClient(self.config)),


def NewDefaultConfig(auth, integration_name, integration_version):
    client_config_dict = {
        "SAToken": auth,
        "Language": SDK_LANGUAGE,
        "SDKVersion": SDK_VERSION,
        "IntegrationName": integration_name,
        "IntegrationVersion": integration_version,
        "RequestLibraryName": DEFAULT_REQUEST_LIBRARY,
        "RequestLibraryVersion": sys.version_info[0] + "." + sys.version_info[1] + "." + sys.version_info[2],
        "SystemOS": platform.system(),
        "SystemOSVersion": platform.architecture()[0],
        "SystemArch": DEFAULT_OS_VERSION,
    }
    return client_config_dict
