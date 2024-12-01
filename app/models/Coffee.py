from app import db

class Coffee(db.Model):
    __tablename__ = 'coffee'

    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(100), nullable=False)
    harga = db.Column(db.Float, nullable=False)
    keterangan = db.Column(db.Text)

    def __repr__(self):
        return f"<Coffee {self.nama}>"

    def to_dict(self):
        return {
            "id": self.id,
            "nama": self.nama,
            "harga": self.harga,
            "keterangan": self.keterangan,
        }
