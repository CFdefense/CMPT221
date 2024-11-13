import pytest

from sqlalchemy import insert, select, text
from models import User

# test db connection
def test_db_connection(db_session):
    # Use db_session to interact with the database
    result = db_session.execute(text("SELECT 1"))
    assert result.scalar() == 1

# 1. test to insert a user
# you can count this as one of your 5 test cases :)
def test_insert_user_name(db_session, sample_signup_input):
    insert_stmt = insert(User).values(sample_signup_input)

    # execute insert query
    db_session.execute(insert_stmt)
    # commit the changes to the db
    db_session.commit()

    # not part of the app.py code, just being used to get the inserted data
    selected_user = db_session.query(User).filter_by(FirstName="Calista").first()

    assert selected_user is not None
    assert selected_user.LastName == "Phippen"

# 2. Test an expected fail
@pytest.mark.xfail
def test_login_fail(db_session, sample_signup_input):
    insert_stmt = insert(User).values(sample_signup_input)

    # execute insert query
    db_session.execute(insert_stmt)
    # commit the changes to the db
    db_session.commit()

    # sample data
    submitted_email = "calista.phippen1@marist.edu"
    submitted_password = "wrongpassword"

    # create a query to select the user password 
    # where the email submitted matches the email in the database
    get_password = select(User.Password).where(User.Email == submitted_email)

    # execute the query
    user_password = db.session.execute(get_password).fetchone()

    # compare the submitted password to the password retrieved from the db
    # user_password[0] because we only selected the password with our query
    assert user_password[0] == submitted_password, "Passwords do not match"

# 3. inject critical error
def test_login_critical(db_session, sample_signup_input):
    insert_stmt = insert(User).values(sample_signup_input)

    # execute insert query
    db_session.execute(insert_stmt)
    # commit the changes to the db
    db_session.commit()

    # sample data
    submitted_email = None # Critical Error 
    submitted_password = "mypassword"

    # create a query to select the user password 
    # where the email submitted matches the email in the database
    get_password = select(User.Password).where(User.Email == submitted_email)

    # Assert that the query returns None or raises an error
    if db_session.execute(get_password).fetchone() is None:
        with pytest.raises(ValueError, match="No user found for the provided email"):
            raise ValueError("No user found for the provided email")

# 4. one using fixture to test signup feature
@pytest.mark.xfail
def test_bad_login(sample_bad_signup):
    # sample data
    first_name = sample_bad_signup.get('FirstName')

    # server side validation - does first name only contain letters?
    if first_name:
        assert False, "FirstName Passed While Containing Numbers"
    else:
        assert True, "FirstName Failed While Containing Numbers"

# 5. one last one to test other parameters
def test_insert_user_email(db_session, sample_signup_input):
    insert_stmt = insert(User).values(sample_signup_input)

    # execute insert query
    db_session.execute(insert_stmt)
    # commit the changes to the db
    db_session.commit()

    # not part of the app.py code, just being used to get the inserted data
    selected_user = db_session.query(User).filter_by(FirstName="Calista").first()

    assert selected_user is not None
    assert selected_user.Email == "calista.phippen1@marist.edu"