import requests


class TestCursos:
    headers = {'Authorization': 'Token 6e2cebcba726eacad3f5e95ef387f0865067a8fe'}
    url_base = 'http://localhost:8000/api/v2/cursos/'

    def test_get_cursos(self):
        cursos = requests.get(url=self.url_base, headers=self.headers)

        assert cursos.status_code == 200
        
    def test_get_curso(self):
        curso = requests.get(url=f'{self.url_base}2/', headers=self.headers)

        assert curso.status_code == 200

    def test_post_curso(self):
        new = {
            "titulo": "Curso de oratória",
            "url": "https://www.gokursos.com/oratoria-retorica-e-eloquencia/p?idtag=6c5101ba-0849-49a6-82ad-b655aeb8b564"
        }

        response = requests.post(url=self.url_base, headers=self.headers, data=new)

        assert response.status_code == 201
        assert response.json()['titulo'] == new["titulo"]

    def test_put_curso(self):
        updated = {
            "titulo": "Novo curso de oratória",
            "url": "https://curso/oratoria-novo"
        }

        response = requests.put(url=f'{self.url_base}6/', headers=self.headers, data=updated)

        assert response.status_code == 200

    def test_delete_curso(self):
        response = requests.delete(url=f'{self.url_base}7/', headers=self.headers)

        assert response.status_code == 204 and len(response.text) == 0