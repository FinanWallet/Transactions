from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, insert, select
from config.db import metadata, engine
from sqlalchemy.sql import text

meta = MetaData()

categories = Table('category', metadata, Column('id', Integer, primary_key=True), 
               Column('name', String(50)))

subcategories = Table('subcategory', metadata, Column('id', Integer, primary_key=True), 
               Column('name', String(50)), 
               Column('category_id', Integer, ForeignKey('category.id')))

metadata.create_all(engine)

try:
    with engine.connect() as connection:
        # Insert categories and keep track of the inserted IDs
        category_names = ['Obligations', 'Game', 'Growth', 'Financial freedom', 'Social responsibility', 'Incidentals']
        category_ids = {}
        for name in category_names:
            # Check if the category already exists
            stmt = select(categories).where(categories.c.name == name)
            result = connection.execute(stmt)
            category = result.fetchone()
            if category is None:
                # If the category does not exist, insert it
                stmt = insert(categories).values(name=name)
                result = connection.execute(stmt)
                category_ids[name] = result.inserted_primary_key[0]

        connection.commit()

        # Map categories to subcategories
        subcategories_dict = {
            'Obligations': ['Rent', 'Pantry', 'Laundry', 'Pets', 'House'],
            'Game': ['Restaurant', 'Party', 'Alcohol'],
            'Growth': ['Education', 'Technology', 'Travel'],
            'Financial freedom': ['Savings', 'Investment'],
            'Social responsibility': ['Donation', 'Gifts'],
            'Incidentals': []
        }

        # Insert subcategories with reference to the category IDs
        for category_name, subcategory_names in subcategories_dict.items():
            for subcategory_name in subcategory_names:
                # Check if the subcategory already exists
                stmt = select(subcategories).where((subcategories.c.name == subcategory_name) & (subcategories.c.category_id == category_ids[category_name]))
                result = connection.execute(stmt)
                subcategory = result.fetchone()
                if subcategory is None:
                    # If the subcategory does not exist, insert it
                    stmt = insert(subcategories).values(name=subcategory_name, category_id=category_ids[category_name])
                    connection.execute(stmt)

        connection.commit()
except Exception as e:
    print(f"An error occurred: {e}")