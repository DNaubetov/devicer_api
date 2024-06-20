import datetime
import uuid

from pydantic import BaseModel
from beanie import Document



class Network(BaseModel):
    ip: str
    mac: str
    network_type: str


class Computer(Document):
    uuid_pc: uuid.UUID
    comp_name: str
    user_name: str
    model: str
    processor: str
    ram: str
    create_data: datetime.datetime | None = datetime.datetime.now()
    network: list[Network]

    class Config:
        json_schema_extra = {
            "example": {'uuid_pc': 'f47ac10b-58cc-4372-a567-0e02b2c3d479',
                        'comp_name': 'DESKTOP-10IM671',
                        'user_name': 'a.xayrullayev',
                        'model': 'HP ProOne 440 G6 24 All-in-One PC',
                        'processor': 'Intel(R) Core(TM) i5-10500T CPU @ 2.30GHz',
                        'ram': '15.78',
                        'network': [{'ip': '10.40.9.189', 'mac': '38-CA-84-4D-02-43', 'network_type': 'ethernet'},
                                    {'ip': '10.40.9.177', 'mac': '04-CF-4B-89-7A-97', 'network_type': 'wireless_network'}],
                        'create_data': datetime.datetime.now()
                        }

        }

    class Setting:
        name = "computer"


class ComputerUpdate(BaseModel):
    uuid_pc: uuid.UUID
    comp_name: str
    user_name: str
    model: str
    processor: str
    ram: str
    create_data: datetime.datetime | None = datetime.datetime.now()
    network: list[Network]

    class Config:
        json_schema_extra = {
            "example": {'uuid_pc': 'f47ac10b-58cc-4372-a567-0e02b2c3d479',
                        'comp_name': 'DESKTOP-10IM671',
                        'user_name': 'a.xayrullayev',
                        'model': 'HP ProOne 440 G6 24 All-in-One PC',
                        'processor': 'Intel(R) Core(TM) i5-10500T CPU @ 2.30GHz',
                        'ram': '15.78',
                        'network': [{'ip': '10.40.9.189', 'mac': '38-CA-84-4D-02-43', 'network_type': 'ethernet'},
                                    {'ip': '10.40.9.177', 'mac': '04-CF-4B-89-7A-97', 'network_type': 'wireless_network'}],
                        'create_data': datetime.datetime.now()
                        }
        }
