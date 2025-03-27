from collections import OrderedDict

class LRUCache:


    """
    Implementação de um cache LRU (Least Recently Used) usando OrderedDict.
    Armazena até 'capacity' itens. Quando o cache atinge o limite,
    remove o item menos utilizado (o mais "antigo" no dicionário).
    """


    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:

        
        """ Retorna o valor associado a 'key' e atualiza a posição no cache. """
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        """ Insere ou atualiza 'key'. Remove o item menos recente se exceder. """
        self.cache[key] = value
        self.cache.move_to_end(key)
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)


if __name__ == "__main__":
    # ExempLO
    cache = LRUCache(capacity=2)

    cache.put(1, 'A')
    cache.put(2, 'B')
    
    print(cache.get(1))  # deve retornar 'A', e mover (1) para o final

    cache.put(3, 'C')    # limite excedido; remove o item menos usado (key=2)

    print(cache.get(2))  # lá removido, deve retornar -1
    print(cache.get(1))  # ainda existe, deve retornar 'A'
    print(cache.get(3))  # deve retornar 'C'
