Projeto feito no BuserCamp de pesquisa de dados de uma determinada rota de ônibus.

Maior parte do código que eu fiz de fato (crawler e o trabalho nos dados para apresentar) está em core/views.py (back) e em frontend/pages/index.vue (front).
No views tem o crawler e os dados que ele procura para mandar para o front.
No index tem o todo o processo de conseguir transformar esses dados para botar nos gráficos. Para ver como os gráficos funcionam, acessar https://chartkick.com/vue

Próximos objetivos:
Multithread no back, mudar como é feita a requisição e o recebimento dos dados no front.
Conectar no banco de dados para poder guardar dados de rotas, e poder botar requerimento de login para usar
