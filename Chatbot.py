import google.generativeai as genai


class GerarConteudo:
    def __init__(self, entrada):
        self.entrada = entrada
        genai.configure(api_key='Sua Chave API aqui')
        model = genai.GenerativeModel("gemini-1.5-flash")
        self.response = model.generate_content(
            entrada,
            generation_config=genai.types.GenerationConfig(
                candidate_count=1,
                stop_sequences=[""],
                max_output_tokens=2000,
                temperature=1.0,
            )
        )

    def gerarTexto(self):
        return self.response.text

