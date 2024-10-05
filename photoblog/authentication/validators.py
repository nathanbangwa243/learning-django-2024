from django.core.exceptions import ValidationError


class ContainsLetterValidator:
    def validate(self, password, user=None):
        if not any(char.isalpha() for char in password):
            raise ValidationError(
                'The password must contain a letter',
                code='password_no_letters'
            )

    def get_help_text(self):
        return 'Your password must contain at least one upper or lower case letter.'

class ContainsNumberValidator:
    def validate(self, password, user=None):
        if not any(char.isdigit() for char in password):
            raise ValidationError(
                'The password must contain a number',
                code='password_no_numbers'
            )

    def get_help_text(self):
        return 'Your password must contain at least one number.'


class ProfilePhotoValidator:
    def __call__(self, uploaded_photo):
        # On récupère la taille du fichier en Mo
        size_mb = uploaded_photo.size / (1024 * 1024)  # Taille en Mo

        if size_mb > 10:  # Limite de 10 Mo
            raise ValidationError(
                'The file size must have a maximum size of 10MB',
                code='photo_larger_size'
            )

    def get_help_text(self):
        return 'The file size must have a maximum size of 10MB'

