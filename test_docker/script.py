# Código vai listar arquivos do diretório atual e para cada arquivo,
# vai imprimir o nome e conteúdo.

from pathlib import Path

current_dir = Path.cwd() #cwd = current work direct
current_file = Path(__file__).name

print(f"Files in {current_dir}:") # Todos os arquivos

for filepath in current_dir.iterdir():
    if filepath.name == current_file: # Ignorar o próprio arquivo
        continue

    print(f" - {filepath.name}")

    if filepath.is_file():
        content = filepath.read_text(encoding = 'utf-8')
        print(f" Content: {content}")


