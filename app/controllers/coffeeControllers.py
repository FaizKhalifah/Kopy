from app.models.Coffee import Coffee, db

def get_all_coffees():
    return [coffee.to_dict() for coffee in Coffee.query.all()]

def create_coffee(data):
    coffee = Coffee(nama=data['nama'], harga=data['harga'], keterangan=data.get('keterangan', ''))
    db.session.add(coffee)
    db.session.commit()
    return coffee.to_dict()