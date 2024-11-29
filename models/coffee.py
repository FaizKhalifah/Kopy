from ..main import db

class Coffee(db.model) : 
    __tablename__ = "Coffees"

    id = db.column(db.Integer,primary_key=True)
    name=db.column(db.String(100),nullable=False)
    description = db.Column(db.String(200))
    additional = db.Column(db.String(100))

    def to_dict(self):
        return{
            'id':self.id,
            'name':self.name,
            'description':self.description,
            'additional':self.additional
        }