from ..models import coffee
from ..main import db

def get_all_coffees():
    return [coffee.to_dict() for coffee in coffee.query.all()]

def get_coffee_by_id(coffee_id):
    coffee = coffee.query.get(coffee_id)
    return coffee.to_dict() if coffee else None

# Membuat item baru
def create_coffee(data):
    new_coffee = coffee(name=data['name'], description=data.get('description'))
    db.session.add(new_coffee)
    db.session.commit()
    return new_coffee.to_dict()

# Memperbarui item
def update_coffee(coffee_id, data):
    coffee = coffee.query.get(coffee_id)
    if not coffee:
        return None
    coffee.name = data.get('name', coffee.name)
    coffee.description = data.get('description', coffee.description)
    db.session.commit()
    return coffee.to_dict()

# Menghapus item
def delete_coffee(coffee_id):
    coffee = coffee.query.get(coffee_id)
    if not coffee:
        return False
    db.session.delete(coffee)
    db.session.commit()
    return True