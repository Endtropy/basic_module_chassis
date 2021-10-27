class Config:

    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'

    SWAGGER = {
        "swagger": "2.0",
        # "openapi": "3.0.2",
        "info": {
            "title": "Title of modul",
            "description": "This is basic flask restful module chassis design",
            "contact": {
                "responsibleOrganization": "Gisat s.r.o",
                "responsibleDeveloper": "Michal Opletal",
                "email": "michal.opletal@gisat.cz",
                "url": "https://www.gisat.cz",
            },
            "license": {
                "name": "Apache 2.0",
                "url": "http://www.apache.org/licenses/LICENSE-2.0.html"
            },
            "version": "0.8.0"
        }
    }

config = Config()