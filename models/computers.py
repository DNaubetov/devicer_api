from pydantic import BaseModel
from beanie import Document

data = {'comp_name': 'DESKTOP-10IM671',
        'user name': 'a.xayrullayev',
        'model': 'HP ProOne 440 G6 24 All-in-One PC',
        'processor': 'Intel(R) Core(TM) i5-10500T CPU @ 2.30GHz',
        'ram': '15.78',
        'network': {'ethernet': {'ip': '10.40.9.189', 'mac': '38-CA-84-4D-02-43'},
                    'wireless_network': {'ip': '10.40.9.177', 'mac': '04-CF-4B-89-7A-97'}}}


class Net(BaseModel):
    ip: str
    mac: str


class Network(BaseModel):
    ethernet: Net
    wireless_network: Net


class Computer(Document):
    comp_name: str
    user_name: str
    model: str
    processor: str
    ram: str
    network: Network

    class Config:
        json_schema_extra = {
            "example": {'comp_name': 'DESKTOP-10IM671',
                        'user_name': 'a.xayrullayev',
                        'model': 'HP ProOne 440 G6 24 All-in-One PC',
                        'processor': 'Intel(R) Core(TM) i5-10500T CPU @ 2.30GHz',
                        'ram': '15.78',
                        'network': {'ethernet': {'ip': '10.40.9.189', 'mac': '38-CA-84-4D-02-43'},
                                    'wireless_network': {'ip': '10.40.9.177', 'mac': '04-CF-4B-89-7A-97'}}}

        }

    class Setting:
        name = "computer"


class ComputerUpdate(BaseModel):
    comp_name: str
    user_name: str
    model: str
    processor: str
    ram: str
    network: Network

    class Config:
        json_schema_extra = {
            "example": {'comp_name': 'DESKTOP-10IM671',
                        'user_name': 'a.xayrullayev',
                        'model': 'HP ProOne 440 G6 24 All-in-One PC',
                        'processor': 'Intel(R) Core(TM) i5-10500T CPU @ 2.30GHz',
                        'ram': '15.78',
                        'network': {'ethernet': {'ip': '10.40.9.189', 'mac': '38-CA-84-4D-02-43'},
                                    'wireless_network': {'ip': '10.40.9.177', 'mac': '04-CF-4B-89-7A-97'}}}

        }