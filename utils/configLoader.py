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
        serverConfig = config["SERVER"]
        return serverConfig["chainname"] + "@" + serverConfig["address"] + ":" + serverConfig["port"]

    @staticmethod
    def getChainName():
        config = ConfigLoader.__loadConfigFile()
        serverConfig = config["SERVER"]
        return serverConfig["chainname"]

    @staticmethod
    def getSeed():
        config = ConfigLoader.__loadConfigFile()
        nodeConfig = config["FULLNODE"]
        return nodeConfig["seed"]


if __name__ == "__main__":
    print(ConfigLoader.getSeed())
