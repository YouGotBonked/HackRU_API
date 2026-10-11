from db import SessionLocal, engine
from models import Base, ModelVersion

def seed():
    print("Verifying database tables exist...")
    Base.metadata.create_all(bind=engine)

    with SessionLocal() as db:
        active_model = db.query(ModelVersion).filter(ModelVersion.is_active == True).first()

        if not active_model:
            print("No active model found in the database. Creating reference...")
            prod_model = ModelVersion(
                name="v1-production",
                weights_path="models/model.pt",
                is_active=True,
                metrics={"classes": ["akiec", "bcc", "bkl", "df", "mel", "nv", "vasc"]}
            )
            db.add(prod_model)
            db.commit()
            print("Database setup and model tracking initialized successfully!")
        else:
            print(f"Active model record '{active_model.name}' already configured.")


if __name__ == "__main__":
    seed()
