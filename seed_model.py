from db import SessionLocal
from models import ModelVersion


def seed():
    with SessionLocal() as db:
        active_model = db.query(ModelVersion).filter(ModelVersion.is_active == True).first()

        if not active_model:
            print("No active model found in database. Creating reference to models/model.pt...")
            prod_model = ModelVersion(
                name="v1-production",
                weights_path="models/model.pt", 
                is_active=True,
                metrics={"classes": ["akiec", "bcc", "bkl", "df", "mel", "nv", "vasc"]}
            )
            db.add(prod_model)
            db.commit()
            print("Successfully seeded the database! Your model will load on next startup.")
        else:
            print(
                f"Database already has an active model record: '{active_model.name}' pointing to '{active_model.weights_path}'")


if __name__ == "__main__":
    seed()
