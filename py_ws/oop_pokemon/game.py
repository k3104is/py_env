class Game:
  def __init__(self, pokemon1, pokemon2):
    self._pokemon1 = pokemon1
    self._pokemon2 = pokemon2
  def battle(self):
    self._start()
    self._pokemon1.attack()
    self._pokemon2.attack()

  def _start(self):
    print(f'{self._pokemon1.name}があらわれた！{self._pokemon1.name}のHPは{self._pokemon1.hp}だ！')
    print(f'{self._pokemon2.name}があらわれた！{self._pokemon2.name}のHPは{self._pokemon2.hp}だ！')
