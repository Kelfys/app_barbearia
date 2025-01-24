// static/js/script.js
function atualizarTotal() {
    const precos = {
        corte: 30,
        barba: 20,
        corte_e_barba: 50,
        outros: 0
    };

    const taxa = 2;
    const servico = document.getElementById("servico").value;
    let precoServico = precos[servico] || 0;
    let total = precoServico + taxa;

    document.getElementById("total").innerText = "Total: R$ " + total.toFixed(2);
}

// Adiciona o evento ao carregar a página para garantir que o total seja atualizado
document.addEventListener('DOMContentLoaded', function() {
    // Atualiza o total sempre que o serviço for alterado
    document.getElementById("servico").addEventListener('change', atualizarTotal);
    
    // Também atualiza o total ao carregar a página, caso o valor padrão já tenha sido escolhido
    atualizarTotal();
});
