import configparser


class ConfigLoader:

    @staticmethod
    def __loadConfigFile():
        config = configparser.ConfigParser()
        config.read("config.cfg")
        return config

    @staticmethod
    def loadBlockChainAddress():
        config = ConfigLoader.__loadConfigFile()
        serverConfig = config["Blockchain"]
        return serverConfig["chainname"] + "@" + serverConfig["address"] + ":" + serverConfig["port"]

    @staticmethod
    def getChainName():
        config = ConfigLoader.__loadConfigFile()
        serverConfig = config["Blockchain"]
        return serverConfig["chainname"]

    @staticmethod
    def getAddress():
        config = ConfigLoader.__loadConfigFile()
        nodeConfig = config["IOTA"]
        return nodeConfig["address"]

    @staticmethod
    def getSeed():
        config = ConfigLoader.__loadConfigFile()
        nodeConfig = config["IOTA"]
        return nodeConfig["seed"]

    @staticmethod
    def getNode():
        config = ConfigLoader.__loadConfigFile()
        nodeConfig = config["IOTA"]
        return nodeConfig["node"]


if __name__ == "__main__":
    print(ConfigLoader.getSeed())
