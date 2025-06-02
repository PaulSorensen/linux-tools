import yaml
from collections import OrderedDict

class YamlHelper:
    """Helper for customizing YAML serialization and formatting."""

    @staticmethod
    def setup_represent_ordereddict():
        """Configure YAML to respect OrderedDict order."""
        def represent_ordereddict(dumper, data):
            return dumper.represent_mapping('tag:yaml.org,2002:map', data.items())
        
        yaml.add_representer(OrderedDict, represent_ordereddict)