test = {'name': 'c',
 'points': 0.1,
 'suites': [{'cases': [{'code': '>>> tomato = Item("tomato", 4, "vegetable")\n'
                                '\n'
                                '>>> kale = Item("kale", 1, "vegetable")\n'
                                '\n'
                                '>>> apple = Item("apple", 2, "fruit")\n'
                                '\n'
                                '>>> chicken = Item("chicken", 3, "meat")\n'
                                '\n'
                                '>>> oreos = Item("oreos", 6, "junk_food")\n'
                                '\n'
                                '>>> stuff = GroceryList([tomato, kale, apple, '
                                'chicken, oreos])\n'
                                '\n'
                                '>>> stuff.items\n'
                                '[tomato, kale, apple, chicken, oreos]\n'
                                '\n'
                                '>>> stuff.buy_cheapest()\n'
                                '\n'
                                '>>> stuff.items\n'
                                '[tomato, apple, chicken, oreos]\n'
                                '\n'
                                '>>> stuff.buy_cheapest()\n'
                                '\n'
                                '>>> stuff.items\n'
                                '[tomato, chicken, oreos]\n'
                                '\n'
                                '>>> stuff.buy_cheapest()\n'
                                '\n'
                                '>>> stuff.items\n'
                                '[tomato, oreos]\n'
                                '\n'
                                '>>> stuff.buy_cheapest()\n'
                                '\n'
                                '>>> stuff.items\n'
                                '[oreos]\n'
                                '\n'
                                '>>> stuff.buy_cheapest()\n'
                                '\n'
                                '>>> stuff.items\n'
                                '[]\n'
                                '\n'
                                '>>> milk = Item("milk", 2, "dairy")\n'
                                '\n'
                                '>>> mo_stuff = GroceryList([milk, apple, '
                                'oreos])\n'
                                '\n'
                                '>>> mo_stuff.items\n'
                                '[milk, apple, oreos]\n'
                                '\n'
                                '>>> mo_stuff.buy_cheapest()\n'
                                '\n'
                                '>>> mo_stuff.items\n'
                                '[apple, oreos]\n'}],
             'scored': True,
             'setup': '>>> from q5 import *',
             'type': 'doctest'}]}