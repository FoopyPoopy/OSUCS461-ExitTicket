from OSUCS461.Config import MySQL as DatabaseConfig
from OSUCS461.ThirdParty.MySQL import MySQL
from OSUCS461.Utilities import createHash, nowSeconds
from OSUCS461.Models import UserWrite, User, UserPost, UserPostWrite

DB = MySQL(**DatabaseConfig)

class UserDB:
    table = "user"

    @staticmethod
    def create(user: UserWrite) -> str:
        uuid = createHash(UserDB.table)
        result = DB.Add(table=UserDB.table, data={"uuid": uuid, "name": user.name, "time_created": nowSeconds()})

        return result["uuid"]
    
    @staticmethod
    def get_all() -> list[User]:
        result = DB.GetAll(UserDB.table)

        return list(map(lambda r: User(**r), result))
    
    @staticmethod
    def get(uuid: str) -> User:
        result = DB.GetBy(UserDB.table, field_params={"uuid": uuid})

        return User(**result)
    
    @staticmethod
    def update(uuid: str, user: UserWrite) -> bool:
       return DB.Update(UserDB.table, data={"name": user.name}, field_params={"uuid": uuid})

       
    
    @staticmethod
    def delete(uuid: str) -> bool:
        result = DB.DeleteWhere(UserDB.table, field_params={"uuid": uuid})

        return result["result"]
    
class UserPostDB:
    table = "user_post"

    @staticmethod
    def create(user_uuid: str, post: UserPostWrite) -> str:
        uuid = createHash(UserPostDB.table)
        result = DB.Add(UserPostDB.table, data={
            "uuid": uuid,
            "user_uuid": user_uuid,
            "post_9char": post.text[:9],
            "text": post.text,
            "time_created": nowSeconds()
        })

        return result["uuid"]
    
    @staticmethod
    def get_all(user_uuid: str):
        result = DB.GetAllWhere(UserPostDB.table, field_params={"user_uuid": user_uuid})

        return list(map(lambda r: UserPost(**r), result))
    
    @staticmethod
    def get(user_uuid: str, uuid: str) -> UserPost:
        result = DB.GetBy(UserPostDB.table, field_params={"uuid": uuid, "user_uuid": user_uuid})

        return UserPost(**result)
    
    

