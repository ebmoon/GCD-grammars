from pathlib import Path
import lark

file_dir = Path(__file__).parent
print(file_dir)

with open(f"{file_dir}/json.lark", "r") as f:
    test_grammar = f.read()

l = lark.Lark(test_grammar, parser='lalr')

while True:
    inp = input()
    print()
    try:
        tree = l.parse(inp)
        print(tree.pretty())
    except Exception as e:
        print(e)
    print('---------')
