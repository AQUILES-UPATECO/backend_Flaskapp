from ..database import DatabaseConnection
class Ejemplo:
    def __init__(self, actor_id = None, first_name = None, last_name = None, last_update = None):
        self.actor_id = actor_id
        self.first_name = first_name
        self.last_name = last_name
        self.last_update = last_update

    @classmethod
    def create_actor(self, actor):
        query = "INSERT INTO sakila.actor (first_name, last_name, last_update) VALUES (%s,%s,%s);"
        params = (actor.first_name, actor.last_name, actor.last_update)
        DatabaseConnection.execute_query(query, params)

    @classmethod
    def get_actor(self,actor_id):
        query = "SELECT first_name, last_name, last_update FROM sakila.actor WHERE actor_id = %s;"
        params = (actor_id,)
        result = DatabaseConnection.fetch_one(query, params)
        print(type(result))
        if result is not None:
            return Ejemplo(
                actor_id = actor_id,
                first_name = result[0],
                last_name = result[1],
                last_update = result[2]
        )
        else:
            return None
        




    # @classmethod
    # def get_actors():
    #     query = "SELECT first_name, last_name, last_update FROM sakila.actor;"
    #     result = DatabaseConnection.fetch_all(query)
    #     if result is not None:
    #         return Actor(
    #             actor_id = result[0],
    #             first_name = result[1],
    #             last_name = result[2],
    #             last_update = result[3]
    #     )
    #     else:
    #         return None