from models import Pet, db
from app import app

class Seed():
    db.drop_all()
    db.create_all()
    
    clifford = Pet(name="Clifford", species="dog", age = 10, savailable=False)
    smokey = Pet(name="Smokey", species="cat", age = 14, available=True)
    bobo = Pet(name="Bobo", species="dog", age = 8, available=True)
    nemo = Pet(name="Nemo", species="fish", age = 2, available=True)
    camy = Pet(name="Camy", species="dog", age =7, available=False)
    james = Pet(name="James", species="cat", age = 5, available=True)
    arnald = Pet(name="Arnald", species="salamander", age=3, available= False)
    
    db.session.add(clifford)
    db.session.add(smokey)
    db.session.add(bobo)
    db.session.add(nemo)
    db.session.add(camy)
    db.session.add(james)
    db.session.add(arnald)
    
    db.session.commit()
