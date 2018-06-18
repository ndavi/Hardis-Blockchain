import plyvel

db = []
db.append(plyvel.DB('/home/ophelia/.multichain/hardis-demo/wallet/txs.db/'))
db.append(plyvel.DB('/home/ophelia/.multichain/hardis-demo/entities.db/'))
db.append(plyvel.DB('/home/ophelia/.multichain/hardis-demo/blocks/index/'))
db.append(plyvel.DB('/home/ophelia/.multichain/hardis-demo/permissions.db/'))


for base in db:
    for key, value in base:
        try:
            stream = key.decode('utf-8')
            print(stream)
            if "test" in stream:
                attack = stream.replace("test","attack")
                base.delete(key)
                base.put(attack.encode('utf-8'), value)
            print(value.decode('utf-8'))
        except UnicodeDecodeError:
            pass
