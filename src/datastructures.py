
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = [
            {"id" : 1, "name": "John","last_name": last_name, "age": 33, "lucky_numbers": [7, 13, 22]},
            {"id" : 2, "name": "Jane","last_name": last_name, "age": 35, "lucky_numbers": [10, 14, 3]},
            {"id" : 3, "name": "Jimmy", "last_name": last_name,"age": 5, "lucky_numbers": [1]}
        ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    # Método para generar un ID único
    def _generateId(self):
        return randint(0, 99999999)

    # Método para agregar un miembro a la familia
    def add_member(self, member):       

    # Genera un ID único al miembro si no tiene uno
        if "id" not in member:
            member["id"] = self._generateId()

    # Agregar el apellido al miembro automáticamente
        member["last_name"] = self.last_name

    # Añadir el miembro a la lista
        self._members.append(member)

        return member  # Retorna el miembro agregado

    # Método para eliminar un miembro de la familia por su ID
    def delete_member(self, id):
        # Recorre la lista y elimina el miembro con el ID proporcionado
        for i, member in enumerate (self._members):
            if member["id"] == id:
                removed_member = self._members.pop(i)
                return {"done": True, "member": removed_member}   # Retorna el miembro eliminado
        return None                 # Si no se encuentra,retorna None
        
    # Método para obtener un miembro por su iD
    def get_member(self, id):
        for member in self._members:
            if member["id"] == id:
                return member  # Retorna el miembro encontrado
        return None  # Si no se encuentra, retorna None
    # Busca y retorna el miembro con el ID proporcionado        

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members



