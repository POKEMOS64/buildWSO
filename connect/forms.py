def validFile(value):
    import os
    exs = os.path.splitext(value.name)[1]
    validExtensions = ['.pdf', '.doc', '.docx']
    if not exs in validExtensions:
        raise ValidationError(u'File not supported')
