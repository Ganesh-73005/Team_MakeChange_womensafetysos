from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from config import Config
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    CORS(app)
    db.init_app(app)
    migrate.init_app(app, db)

    from routes import auth, sos, safe_route, chatbot
    app.register_blueprint(auth.bp)
    app.register_blueprint(sos.bp)
    app.register_blueprint(safe_route.bp)
    app.register_blueprint(chatbot.bp)

    @app.route('/test')
    def test_route():
        return 'Welcome to the Safety App API'

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)