from xml.dom.minidom import CharacterData
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _


class SpecialCharactersValidator:
    def __init__(self):
        self.characters = {"!", "@", "#", "?", "]"}
        pass

    def validate(self, password, user=None):
        # Check that password has at least one uppercase letter
        if password.islower():
            raise ValidationError(
                _("This password must contain at least 1 uppercase letter"),
                code="password_requires_uppercase_letter",
                params={"min_uppercase_letters": 1},
            )

        # Check that password has at least one lowercase letter
        if password.isupper():
            raise ValidationError(
                _("This password must contain at least 1 lowercase letter"),
                code="password_requires_lowercase_letter",
                params={"min_lowercase_letters": 1},
            )

        # Check that password contains at least one special character
        if not any(c in password for c in self.characters):
            special_characters = ",".join(self.characters)
            raise ValidationError(
                _(
                    f"This password must contain at least 1 of the following characters: {special_characters}"
                ),
                code="password_requires_special_character",
                params={"requires_special_character_in": self.characters},
            )

    def get_help_text(self):
        return _(
            "Your password must contain at least 1 uppercase and lowercase letter, and also include one of following special characters: "
        )
