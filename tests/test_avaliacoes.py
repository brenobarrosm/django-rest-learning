import requests


class TestAvaliacoes:
    base_url = 'http://localhost:8000/api/v2/avaliacoes/'
    headers = {'Authorization': 'Token 6e2cebcba726eacad3f5e95ef387f0865067a8fe'}

    def test_get_avaliacoes(self):
        avaliacoes = requests.get(url=self.base_url)

        assert avaliacoes.status_code == 200

    def test_post_avaliacao(self):
        new = {
            "curso": 2,
	        "nome": "Albert",
	        "email": "albert@gmail.com",
	        "avaliacao": 4
        }

        avaliacao = requests.post(url=self.base_url, headers=self.headers, data=new)

        assert avaliacao.status_code == 201

