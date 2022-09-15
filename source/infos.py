class DocumentInfos:

    title = u'Documentation'
    first_name = 'Cédric'
    last_name = 'Donner'
    author = f'{first_name} {last_name}'
    year = u'2022'
    month = u'Septembre'
    seminary_title = u'Développement Web'
    tutor = u"Cédric Donner et Johan Jobin"
    release = "0.1"
    repository_url = "https://github.com/informatiquecsud/tm-donc-jobj-2223"

    @classmethod
    def date(cls):
        return cls.month + " " + cls.year

infos = DocumentInfos()