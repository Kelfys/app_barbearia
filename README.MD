
# Barbershop - Sistema de Agendamento Online

Bem-vindo ao **Barbershop**, um sistema simples e funcional para agendamento de serviços de barbearia! 💈✂️

Este projeto permite que clientes agendem cortes de cabelo, barba, ou outros serviços diretamente pelo site, com confirmação visual do horário e valor total.

---

## Funcionalidades

- Agendamento de serviços (corte, barba, corte + barba, selagem, outros)
- Cálculo automático do total baseado no serviço escolhido
- Validação de formulário (nome, WhatsApp, horário)
- Mensagens de feedback ao usuário após o envio do agendamento
- Layout responsivo, compatível com desktop e mobile

---

## Tecnologias utilizadas

- **HTML5** e **CSS3** para estrutura e estilo
- **JavaScript** para interatividade (cálculo do total)
- **Python + Flask** para backend e processamento de formulários
- **Jinja2** para templates dinâmicos
- **Bootstrap** ou CSS customizado (se aplicável) para estilização

---

## Instalação

Siga estes passos para rodar o projeto localmente:

1. Clone o repositório:
   ```bash
   git clone https://github.com/seuusuario/barbershop.git

2. Acesse a pasta do projeto:

cd barbershop


3. Crie um ambiente virtual (opcional, mas recomendado):

python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows


4. Instale as dependências:

pip install -r requirements.txt


5. Execute o servidor Flask:

flask run


6. Abra o navegador e acesse:

http://127.0.0.1:5000




---

Como usar

1. Preencha seu nome e número de WhatsApp.


2. Escolha o tipo de serviço.


3. Selecione o horário desejado.


4. Confira o total do serviço.


5. Clique em Agendar.


6. Você verá uma mensagem confirmando seu agendamento.




---

Estrutura do projeto

barbershop/
│
├── templates/
│   └── index.html        # Página principal com formulário
│
├── static/
│   ├── css/
│   │   └── style.css     # Estilos do site
│   └── js/
│       └── script.js     # Script para cálculo do total
│
├── app.py                # Backend em Flask
├── requirements.txt      # Dependências do Python
└── README.md             # Documentação do projeto


---

Contribuição

Contribuições são bem-vindas! 😄
Se você quiser melhorar este projeto, sinta-se à vontade para abrir issues ou pull requests.


---

Licença

Este projeto está sob a licença MIT. Sinta-se livre para usar e adaptar!


---

