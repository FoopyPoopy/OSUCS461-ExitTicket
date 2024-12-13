from pydantic import BaseModel

class BasePydanticModel(BaseModel):
	class Config:
		from_attributes = False
		validate_assignment = True

class UserWrite(BaseModel):
    name: str

class User(UserWrite):
    uuid: str
    time_created: int

class UserPostWrite(BaseModel):
	text: str

class UserPost(UserPostWrite):
	uuid: str
	user_uuid: str
	post_9char: str
	time_created: int

