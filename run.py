from app import factory
import app

if __name__ == "__main__":
    app = factory.create_app(celery=app.celery)
    app.run(host="0.0.0.0", debug=True)

