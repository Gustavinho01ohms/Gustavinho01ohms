from Chatbot import GerarConteudo

prompt = input("?")
conversa = GerarConteudo(prompt)
textogerado = conversa.gerarTexto()

print(textogerado)