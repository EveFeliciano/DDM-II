import os
from bs4 import BeautifulSoup

# Função para salvar os conteúdos extraídos em arquivos
def salvar_arquivo(caminho, nome_arquivo, conteudo):
    with open(os.path.join(caminho, nome_arquivo), 'w', encoding='utf-8') as f:
        f.write(conteudo)

# Função para extrair e salvar os scripts e estilos do HTML
def extrair_e_salvar(html, pasta_js, pasta_css):
    # Usando BeautifulSoup para fazer o parsing do HTML
    soup = BeautifulSoup(html, 'html.parser')
    
    # Criar as pastas se não existirem
    os.makedirs(pasta_js, exist_ok=True)
    os.makedirs(pasta_css, exist_ok=True)

    # Extrair e salvar o conteúdo de JavaScript
    scripts = soup.find_all('script')
    for i, script in enumerate(scripts):
        if script.string:  # Verifica se há conteúdo dentro da tag <script>
            salvar_arquivo(pasta_js, f"script_{i+1}.js", script.string)
    
    # Extrair e salvar o conteúdo de CSS
    styles = soup.find_all('style')
    for i, style in enumerate(styles):
        if style.string:  # Verifica se há conteúdo dentro da tag <style>
            salvar_arquivo(pasta_css, f"style_{i+1}.css", style.string)
    
    print(f"JavaScript salvo em: {pasta_js}")
    print(f"CSS salvo em: {pasta_css}")

# Exemplo de uso
html_exemplo = """
<html>
<head>
    <style>
        body { background-color: lightblue; }
        h1 { color: blue; }
    </style>
</head>
<body>
    <h1>Exemplo de Página</h1>
    <p>Texto com alguns estilos e scripts.</p>
    <script>
        console.log('Este é um script JavaScript');
    </script>
    <script>
        alert('Outro script JavaScript');
    </script>
</body>
</html>
"""

# Defina as pastas onde os arquivos serão salvos
pasta_js = "js_scripts"
pasta_css = "css_styles"

# Executar a extração e salvar os arquivos
extrair_e_salvar(html_exemplo, pasta_js, pasta_css)
