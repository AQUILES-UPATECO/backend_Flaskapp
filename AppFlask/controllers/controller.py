from ..model.actors import Actor
from flask import request
from flask import jsonify

class ActorController:
    @classmethod
    def create_actor(self):
        
        actor = Actor(
        first_name = request.args.get('first_name', ''),
        last_name = request.args.get('last_name', ''),\
        last_update = request.args.get('last_update', '')
        )

        Actor.create_actor(actor)
        return {'message': 'Actor creado con exito'}, 200
    
    @classmethod
    def get_actor(cls, actor_id):
        actor_instance = Actor.get_actor(actor_id)
           
             
        
        if actor_instance:
            response_data = {
                "id": actor_instance.actor_id,
                "nombre": actor_instance.first_name,
                "apellido": actor_instance.last_name,
                "ultima_actualizacion": actor_instance.last_update
                }
            
            return jsonify(response_data), 200
        
        else:
    
            return {"msg": "No se encontró el actor"}, 404
    




    
    # @classmethod
    # def get_actors(self):
    #     results = Actor.get_actors
    #     actors = []
    #     for result in results:
    #         actors.append({
    #             "id": result[0],
    #             "nombre": result[1],
    #             "apellido": result[2],
    #             "ultima_actualizacion": result[3]
    #     })
    #     return actors, 200
        

    # @classmethod
    # def update_actor(self, actor):
    # #Implementación del método
    #     pass

    # @classmethod
    # def delete_actor(self, actor):
    # #Implementación del método
    #     pass

    # @classmethod
    # def delete_actors(self):
    # #Implementación del método
    #     pass