from app.models.Coffee import Coffee, db

def get_coffee_by_id(coffee_id):
    coffee = Coffee.query.get(coffee_id)
    print(coffee)
    if coffee == None:
        return None
    return coffee.to_dict()

def get_all_coffees():
    return [coffee.to_dict() for coffee in Coffee.query.all()]

def create_coffee(data):
    coffee = Coffee(nama=data['nama'], harga=data['harga'], keterangan=data.get('keterangan', ''))
    db.session.add(coffee)
    db.session.commit()
    return coffee.to_dict()

def update_coffee(coffee_id, data):
    coffee = Coffee.query.get(coffee_id)
    if coffee:
        coffee.nama = data.get('nama', coffee.nama)
        coffee.harga = data.get('harga', coffee.harga)
        coffee.keterangan = data.get('keterangan', coffee.keterangan)
        db.session.commit()
        return coffee.to_dict()
    return None

def delete_coffee(coffee_id):
    coffee = Coffee.query.get(coffee_id)
    if coffee:
        db.session.delete(coffee)
        db.session.commit()
        return True
    return False