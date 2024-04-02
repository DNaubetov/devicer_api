from models.computers import Computer


async def check_computer_from_db(body: Computer):
    data = body.__copy__()
    data.create_data = None
    user_all_data_db = await Computer.find(Computer.user_name == body.user_name).to_list()
    for user in user_all_data_db:
        setattr(user, 'id', None)
        setattr(user, 'create_data', None)
    return data in user_all_data_db
