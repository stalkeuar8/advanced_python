import pytest
from pass_valid import pass_validator

class TestPassValid:

    @pytest.mark.pass_validity
    @pytest.mark.parametrize(
        'password, res',
        [
            pytest.param('Qw!e6wwww', (True, 'Password is valid'), id='valid'),
            pytest.param('qq!qw666www', (False, "Password must contain uppercase letter"), id='no_uppers'),
            pytest.param('QWE!6WWWW', (False, "Password must contain lowercase letter"), id='no_lowers'),
            pytest.param('gg!G666', (False, "Password to short"), id='short_pass'),
            pytest.param('Qwe!ggg6w ww', (False, "Password must be without spaces"), id='spaces'),
            pytest.param('!66666666', (False, "Password must contain letter"), id='no_letters'),
            pytest.param('Q66ggwwww', (False, "Password must contain special symbols"), id='no_specs'),
            pytest.param('Q!!ggwwww', (False, "Password must contain digit"), id='no_digits'),
        ]
    )
    def test_pass_valid(self, password, res):
        assert pass_validator(password) == res
        assert isinstance(pass_validator(password), tuple)

