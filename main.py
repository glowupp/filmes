from flask import Flask, render_template, url_for # Importa a biblioteca

app = Flask(__name__) # Inicializa a aplicação

posts = [
    {
        'title': 'Duna',
        'year': '2021',
        'hour': '2h 35m',
        'genre': 'Ficção científica/Aventura',
        'content': 'Paul Atreides é um jovem brilhante, dono de um destino além de sua compreensão. Ele deve viajar para o planeta mais perigoso do universo para garantir o futuro de seu povo.',
        'date_posted': 'April 20, 2021'
    },
    {
        'title': 'Venom: Tempo de Carnificina',
        'year': '2021',
        'hour': '1h 45m',
        'genre': 'Ação/Ficção científica',
        'content': 'O relacionamento entre Eddie e Venom está evoluindo. Buscando a melhor forma de lidar com a inevitável simbiose, esse dois lados descobrem como viver juntos e, de alguma forma, se tornarem melhores juntos do que separados.',
        'date_posted': 'April 21, 2021'
    },
    {
        'title': '007 - Sem Tempo para Morrer (No Time to Die)',
        'year': '2021',
        'hour': '2h 43m',
        'genre': 'Ação/Aventura',
        'content': 'James Bond deixa o MI6 e se muda para a Jamaica, mas um antigo amigo aparece e pede sua ajuda para encontrar um cientista desaparecido. Bond mergulha no caso e percebe que a busca é, na verdade, uma corrida para salvar o mundo.',
        'date_posted': 'April 21, 2021'
    },
    {
        'title': 'Eternos',
        'year': '2021',
        'hour': '2h 37m',
        'genre': 'Ação/Aventura',
        'content': 'Os Eternos são uma raça de seres imortais que viveram durante a antiguidade da Terra, moldando sua história e suas civilizações enquanto batalhavam os malignos Deviantes.',
        'date_posted': 'April 21, 2021'
    },
    {
        'title': 'Doutor Estranho 2',
        'year': '2022',
        'hour': 'Indefinido',
        'genre': 'Aventura/Fantasia',
        'content': 'Doctor Strange in the Multiverse of Madness é um futuro filme estadunidense de super-herói baseado no personagem homônimo da Marvel Comics.',
        'date_posted': 'April 25, 2021'
    }
]


@app.route('/') # Cria uma rota
def main():
  return render_template('layout.html', posts=posts)

if __name__ == '__main__':
  app.run(debug=True) # Executa a aplicação