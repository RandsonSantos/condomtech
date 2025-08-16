from flask import Flask, render_template

app = Flask(__name__)

# Rota para a página inicial
@app.route('/')
def home():
    return render_template('index.html')

# Rota para a página de serviços
@app.route('/services')
def services():
    service_list = [
        {'title': 'Segurança Eletrônica', 'icon': 'bi-shield-lock', 'description': 'Instalação e manutenção de câmeras, alarmes e cercas elétricas para a proteção de seu patrimônio.'},
        {'title': 'Automação', 'icon': 'bi-house-door', 'description': 'Transformamos ambientes com sistemas inteligentes para controle de iluminação, clima e outros dispositivos.'},
        {'title': 'Controle de Acesso', 'icon': 'bi-person-badge', 'description': 'Soluções modernas e seguras para gerenciar entrada e saída em condomínios e empresas.'},
        {'title': 'Monitoramento', 'icon': 'bi-camera-video', 'description': 'Monitoramento 24h para garantir a segurança de seus bens.'},
        {'title': 'Manutenção Preventiva', 'icon': 'bi-tools', 'description': 'Manutenção programada para evitar falhas e prolongar a vida útil de seus equipamentos.'},
        {'title': 'Rede de Computadores', 'icon': 'bi-ethernet', 'description': 'Infraestrutura completa para redes cabeadas e Wi-Fi, garantindo velocidade e estabilidade.'},
        {'title': 'Interfonia', 'icon': 'bi-telephone', 'description': 'Sistemas de interfonia para comunicação eficiente em condomínios e empresas.'},
        {'title': 'Informática', 'icon': 'bi-laptop', 'description': 'Suporte técnico e soluções de informática para empresas.'},
        {'title': 'Desenvolvimento de Sistemas', 'icon': 'bi-code-slash', 'description': 'Sistemas sob medida para otimizar processos e aumentar a produtividade.'}
    ]
    return render_template('services.html', services=service_list)

# Rota para a página de contato
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Rota para a página "Sobre Nós"
@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)