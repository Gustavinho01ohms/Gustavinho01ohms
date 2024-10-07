from Chatbot import GerarConteudo

prompt = input("Sobre o que vamos falar? ")
conversa = GerarConteudo(prompt)
textogerado = conversa.gerarTexto()

print(textogerado)