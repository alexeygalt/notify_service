import pytest
import string
from core.social_auth.utils import password_generator


@pytest.mark.parametrize("size, chars", [
    (None, string.ascii_uppercase + string.ascii_lowercase + string.digits),
    (8, string.ascii_uppercase),
    (12, string.ascii_lowercase),
    (15, string.digits),
    (10, "!@#$%^"),
])
def test_password_generator(size, chars):
    if size is not None:
        password = password_generator(size=size, chars=chars)
        assert len(password) == size
        assert all(char in chars for char in password)
    else:
        with pytest.raises(TypeError):
            password_generator(size=size, chars=chars)