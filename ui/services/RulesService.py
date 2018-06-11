import getpass

class RulesService:

    @staticmethod
    def filterMyObjects(objects_to_filter):
        result = []
        me = getpass.getuser()
        for object in objects_to_filter:
            id, owner = object
            if(me == owner):
                result.append(object)
        return result