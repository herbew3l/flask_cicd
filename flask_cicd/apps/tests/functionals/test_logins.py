# from flask_cicd.apps.homes.tests.controls import app


def test_login_route(app, client):
    """ 
    GIVEN a Flask application configured for testing
    WHEN the '/login' route is requested (GET)
    THEN check that the response is valid
    """
    with app.test_client() as test_client:
        res = test_client.get('/login')
        print("test_login_route__status_code__%s" % res.status_code)
        assert res.status_code == 308

if __name__ == "__main__":
    test_login_route(app, client)

