from app import factory
import app

app = factory.create_app(celery=app.celery)
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

