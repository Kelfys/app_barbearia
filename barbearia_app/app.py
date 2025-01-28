from flask import Flask, render_template, request, redirect, url_for, flash
import urllib.parse

app = Flask(__name__)
app.secret_key = 'seu_segredo_aqui'  # Alterar para uma chave secreta segura em produção

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Obtendo dados do formulário
        nome = request.form['nome']
        whatsapp = request.form['whatsapp']
        servico = request.form['servico']
        horario = request.form['horario']
        
        # Preços e cálculo do total
        precos = {
            "corte": 30,
            "barba": 20,
            "corte_e_barba": 50,
            "sobrancelha": 10,
            "outros": 0
        }
        preco_servico = precos.get(servico, 0)
        taxa_adicional = 2
        total = preco_servico + taxa_adicional

        # Criando a mensagem para o WhatsApp
        mensagem = f"Novo agendamento!\n\nNome: {nome}\nNúmero: {whatsapp}\nServiço: {servico}\nHorário: {horario}\nTotal: R$ {total:.2f}\n"
        mensagem_url = urllib.parse.quote(mensagem)  # Codificando a mensagem para a URL

        # Gerar o link para o WhatsApp
        numero_whatsapp = "+5521975286720"
        url_whatsapp = f"https://wa.me/{numero_whatsapp}?text={mensagem_url}"

        # Redireciona para o WhatsApp com a mensagem
        return redirect(url_whatsapp)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
