"""
Classes ConfigurationAttributesLoader, ConfigurationAttributesManipulator, ConfigurationBuildingEngine, ConfigurationRegistry
define the subsystem.

The ConfigManager is the Facade to the subsystem which aims to simplify usage and access of clients.
"""

import yaml
import time

attributes_registry = {
    "Router-1": {
        "attributes": "cisco_config_example.yaml"
    }
}

def get_yaml_file_for_device(device):
    return attributes_registry[device]["attributes"]

CONFIG_FILE_PATH_POSTFIX = "cisco_device_config.cfg"

class ConfigurationAttributesLoader:
    def load_attributes(self, device):
        print(f"Loading configuration attributes for device {device}")
        yaml_file_path = get_yaml_file_for_device(device)
        # Load the YAML file
        with open(yaml_file_path, "r") as file:
            config = yaml.load(file, Loader=yaml.Loader)
        print(f"Loaded config for device\n{config}\n\n")
        return config

class ConfigurationAttributesUpdater:
    def add_interface(self, config, device):
        # Add new attributes to the configuration
        config["interfaces"].append(
            {
                "name": "GigabitEthernet0/2",
                "description": "Additional Interface",
                "ip_address": "192.168.3.1",
                "subnet_mask": "255.255.255.0",
                "status": "up"
            }
        )

        config["vlan"].append(
            {
                "id": 30,
                "name": "Guest",
                "ports": ["GigabitEthernet0/2"]
            }
        )

        yaml_file_path = get_yaml_file_for_device(device)
        # Save the updated configuration back to the YAML file
        with open(yaml_file_path, "w") as file:
            yaml.dump(config, file)

        # Print the updated configuration
        print(f"Updated Configuration:\n{config}\n\n")

class ConfigurationBuildingEngine:
    def generate(self, config, device):
        # Generate Cisco device configuration
        device_config = ""

        # Interface configuration
        device_config += "interface {}\n".format(config["interfaces"][0]["name"])
        device_config += " description {}\n".format(config["interfaces"][0]["description"])
        device_config += " ip address {} {}\n".format(config["interfaces"][0]["ip_address"], config["interfaces"][0]["subnet_mask"])
        device_config += " shutdown\n" if config["interfaces"][0]["status"] == "down" else " no shutdown\n"

        device_config += "\n"

        # VLAN configuration
        for vlan in config["vlan"]:
            device_config += "vlan {}\n".format(vlan["id"])
            device_config += " name {}\n".format(vlan["name"])
            device_config += "!\n"
            for port in vlan["ports"]:
                device_config += "interface {}\n".format(port)
                device_config += " switchport mode access\n"
                device_config += " switchport access vlan {}\n".format(vlan["id"])
                device_config += "!\n"
            device_config += "\n"

        # Routing configuration
        device_config += "ip route 0.0.0.0 0.0.0.0 {}\n".format(config["routing"][0]["next_hop"])
        device_config += "ip route {} {}\n".format(config["routing"][1]["network"], config["routing"][1]["next_hop"])
        device_config += "\n"

        # Print the generated Cisco device configuration
        print(f"Generated Cisco Device Configuration:\n{device_config}\n\n")

        device_config_file_name = f"{device}__{CONFIG_FILE_PATH_POSTFIX}"
        # Save the generated configuration to a local file
        with open(device_config_file_name, "w") as file:
            yaml.dump(device_config, file)

        # Print the generated Cisco device configuration
        print(f"Persisted configuration to local file {device_config_file_name}")
        return device_config_file_name

class ConfigurationRegistry:
    def upload_to_registry(self, generated_config):
        print(f"Uploading device configuration from {generated_config} to config registry...")
        time.sleep(1)
        print("Done!")

class ConfigManager:
    def start_config_gen_workflow(self, device):
        loader = ConfigurationAttributesLoader()
        config = loader.load_attributes(device)

        updater = ConfigurationAttributesUpdater()
        updater.add_interface(config, device)

        engine = ConfigurationBuildingEngine()
        generated_config = engine.generate(config, device)

        registry = ConfigurationRegistry()
        registry.upload_to_registry(generated_config)
        print("Configuration generation workflow has completed all its steps successfully")
