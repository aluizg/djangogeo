# Projeto de Geolocalização em Python com Django

Este projeto é uma aplicação web desenvolvida em Python utilizando o framework Django, que permite a geolocalização de usuários e a exibição de mapas interativos. A aplicação utiliza APIs de geolocalização para obter a localização do usuário e exibir pontos de interesse em um mapa.

## Pacotes a serem instalados
Para executar este projeto, você precisará instalar os seguintes pacotes Python:
- Django
- Geoip2
- Requests

```commandline
pip install django geoip2 requests
```

## Criando o Projeto Django e Aplicação
Para criar um novo projeto Django, execute o seguinte comando no terminal:
```commandline
django-admin startproject djangogeo .
```

Em seguida, crie uma nova aplicação dentro do projeto:
```commandline
django-admin startapp core
```