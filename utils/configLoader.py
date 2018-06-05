import configparser


class ConfigLoader:

    @staticmethod
    def __loadConfigFile():
        config = configparser.ConfigParser()
        config.read("config.cfg")
        return config

    @staticmethod
    def getBlockChainAddress():
        config = ConfigLoader.__loadConfigFile()
        serverConfig = config["Blockchain"]
        return serverConfig["chainname"] + "@" + serverConfig["address"] + ":" + serverConfig["port"]

    @staticmethod
    def getBlockChainName():
        config = ConfigLoader.__loadConfigFile()
        serverConfig = config["Blockchain"]
        return serverConfig["chainname"]

    @staticmethod
    def getIotaAddress():
        config = ConfigLoader.__loadConfigFile()
        nodeConfig = config["IOTA"]
        return nodeConfig["address"]

    @staticmethod
    def getIotaSeed():
        config = ConfigLoader.__loadConfigFile()
        nodeConfig = config["IOTA"]
        return nodeConfig["seed"]

    @staticmethod
    def getIotaNode():
        config = ConfigLoader.__loadConfigFile()
        nodeConfig = config["IOTA"]
        return nodeConfig["node"]


if __name__ == "__main__":
    print(ConfigLoader.getIotaSeed())
