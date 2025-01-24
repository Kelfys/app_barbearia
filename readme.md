---

# Agendamento de Serviços para Barbearia

Este projeto permite que clientes agendem serviços de barbearia diretamente pelo site, incluindo o cálculo de preços para diferentes tipos de serviços, e a confirmação do agendamento via WhatsApp.

## Funcionalidades

- **Agendamento de Serviços:** O cliente pode escolher entre diferentes tipos de serviços, como corte de cabelo, barba ou ambos, e agendar o horário desejado.
- **Cálculo de Preço:** O sistema calcula automaticamente o total com base no serviço escolhido e uma taxa adicional de R$ 2,00.
- **Confirmação via WhatsApp:** Após preencher o formulário, os dados do agendamento (nome, número do WhatsApp, tipo de serviço e horário) são enviados para um número de WhatsApp pré-configurado.

## Como Funciona

1. **Formulário de Agendamento:** O cliente preenche o formulário com seu nome, número de WhatsApp, tipo de serviço e horário desejado.
2. **Cálculo de Total:** Ao selecionar o tipo de serviço, o preço é calculado automaticamente e exibido.
3. **Envio de Dados para WhatsApp:** Quando o formulário é enviado, os dados são formatados e enviados para um número de WhatsApp via uma URL específica, permitindo ao cliente confirmar o agendamento diretamente no WhatsApp.

## Estrutura do Projeto

A estrutura do projeto é composta por:

```
barbearia_app/
│
├── static/
│   ├── css/
│   │   └── style.css        # Estilos do site
│   ├── js/
│   │   └── script.js        # Lógica do cálculo de preço
│
├── templates/
│   └── index.html           # Página HTML do formulário de agendamento
│
├── app.py                   # Backend em Flask para processar os agendamentos
└── requirements.txt         # Dependências do projeto
```

## Como Rodar o Projeto

### 1. Instalar Dependências

Primeiro, crie um ambiente virtual e instale as dependências necessárias listadas no arquivo `requirements.txt`.

```bash
pip install -r requirements.txt
```

### 2. Iniciar o Servidor Flask

Depois de instalar as dependências, inicie o servidor Flask para rodar o aplicativo:

```bash
python app.py
```

O servidor estará rodando no `http://127.0.0.1:5000/` por padrão.

### 3. Acessar o Formulário

Abra um navegador e acesse `http://127.0.0.1:5000/` para visualizar o formulário de agendamento.

### 4. Enviar Agendamento via WhatsApp

Ao submeter o formulário, o agendamento será enviado para o número de WhatsApp configurado. A mensagem inclui os dados preenchidos, como o nome, número de WhatsApp, tipo de serviço e horário.

## Tecnologias Utilizadas

- **Flask:** Framework web para construir o backend.
- **HTML:** Para estruturar a página do formulário de agendamento.
- **CSS:** Para estilizar a página e melhorar a experiência do usuário.
- **JavaScript:** Para calcular o preço total dinamicamente com base no serviço selecionado.

## Personalizações

- **Número do WhatsApp:** O número para envio dos agendamentos via WhatsApp foi configurado como `+5521975286720`. Você pode alterar isso no código backend (`app.py`), caso queira usar um número diferente.
- **Preços:** Os preços dos serviços podem ser ajustados diretamente no código JavaScript ou no backend, conforme sua necessidade.

## Contribuindo

Se você deseja contribuir para o projeto, fique à vontade para abrir uma **issue** ou um **pull request**. Será um prazer analisar e integrar suas melhorias!

---