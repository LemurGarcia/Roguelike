CELLS = {
    '*': {'name': 'Каменная стена', 'walkable': False, 'destructible': False,
          'description': 'Вы видите обыкновенную стену, слегка покрытую плесенью. Плесень шевелится.',
          'pic':[
              " __________",
              "___|____|____",
              "_|____|_____",
              "____|_____|__"
          ]
          },
    ' ': {'name': 'Пол', 'walkable': True, 'destructible': False, 'description': 'Ничего интересного.'},
    '=': {'name': 'Лестница', 'walkable': True, 'destructible': False,
          'description': 'Лестница, ведущая куда-то наверх. Куда именно - непонятно, слишком темно.',
          'pic': [
              "            ",
              "        o   ",
              "      _/|______ ",
              "    _/_|_____| |",
              "  o/_|_____|   |",
              "  ||_____|_____|"
          ]
          },
    '/': {'name': 'Перила', 'walkable': False, 'destructible': False, 'description': 'Мощные каменные поручни.'},
   '\\': {'name': 'Перила', 'walkable': False, 'destructible': False, 'description': 'Мощные каменные поручни.'},
    '#': {'name': 'Сундук', 'walkable': True, 'destructible': True,
          'description': 'Крепкий сундук. Чтобы открыть его, скорее всего понадобится ключ.',
          'pic': [
                "    _________   ",
                "  /         /|  ",
                " /_________/ |  ",
                " |____ ____| |",
                " |    i    | |    ",
                " |_________|/  "

          ]
          }
}

ACTORS = {
    '@': {'name': 'Герой', 'type':'player', 'class':'Hero', 'description': 'Это вы.'},
    'G': {'name': 'Привиденьице', 'type':'enemy', 'class':'Ghost', 'description':'Привиденьице. Оно говорит: "Шурх! Шурх!".\n Привидения не атакуют, если их не провоцировать.'},
    'F': {'name': 'Фаггро', 'type':'enemy', 'class':'Fahgro', 'description':'Маленькое, но очень злобное создание, обитающее в основном под землёй. Фаггро атакуют всё, что движется, и едят всё, что могут разгрызть или хотя бы проглотить.'},
}
