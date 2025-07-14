from app import create_app, db
from app.models import ChartData

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    # --- Dummy data for Device Traffic Bar Chart ---
    device_data = [
        ("Linux", 20000000),
        ("Mac", 23000000),
        ("iOS", 21000000),
        ("Windows", 26000000),
        ("Android", 10000000),
        ("Other", 24000000)
    ]

    # --- Dummy data for Location Donut Chart ---
    location_data = [
        ("United States", 38.6),
        ("Canada", 22.5),
        ("Mexico", 30.8),
        ("Other", 8.1)
    ]

    # --- Dummy data for User Growth Line Chart ---
    growth_data = [
        ("Jan", 10),
        ("Feb", 30),
        ("Mar", 50),
        ("Apr", 60),
        ("May", 80),
        ("Jun", 100)
    ]

    # Insert all into ChartData
    for label, value in device_data:
        db.session.add(ChartData(label=label, value=value, type="device"))

    for label, value in location_data:
        db.session.add(ChartData(label=label, value=value, type="location"))

    for label, value in growth_data:
        db.session.add(ChartData(label=label, value=value, type="growth"))

    db.session.commit()
    print("✅ Dummy chart data inserted into chartdata table.")
