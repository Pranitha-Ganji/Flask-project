from app import create_app, db

app = create_app()

if __name__ == '__main__':
    # Automatically create database tables before launching if they don't exist
    with app.app_context():
        db.create_all()
        
    app.run(debug=True)