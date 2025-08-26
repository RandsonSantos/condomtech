from flask import Flask, render_template

app = Flask(__name__)

# Rota para a página inicial
@app.route('/')
def home():
    return render_template('index.html')

# NOVO: Rota para a página de Empresas
@app.route('/empresas')
def empresas():
    services = [
        {
            "title": "Segurança Corporativa",
            "description": "Sistemas de segurança avançados para proteger sua empresa.",
            "detalhes": "Monitoramento 24h, controle de acesso por biometria, câmeras inteligentes, integração com central de segurança e relatórios de atividade.",
            "icon": "bi-shield-check"
        },
        {
            "title": "Rede e Servidores",
            "description": "Infraestrutura de rede robusta e gerenciamento de servidores.",
            "detalhes": "Instalação de redes cabeadas e Wi-Fi, servidores dedicados, backup automático, firewall corporativo e suporte técnico especializado.",
            "icon": "bi-server"
        },
        {
            "title": "Automação Comercial",
            "description": "Soluções de automação para otimizar operações comerciais.",
            "detalhes": "Controle de iluminação, climatização, portões, sistemas de atendimento, integração com sistemas ERP e gestão por aplicativo.",
            "icon": "bi-building"
        }
    ]
    return render_template('empresas.html', services=services)

# NOVO: Rota para a página de Condomínios
@app.route('/condominios')
def condominios():
    services = [
        {
            "title": "Portaria Autônoma",
            "description": "Controle de acesso seguro e eficiente 24h.",
            "detalhes": "Sistema com reconhecimento facial, QR Code, integração com aplicativo e histórico de acessos. Elimina a necessidade de porteiro físico, reduz custos e aumenta a segurança.",
            "icon": "bi-person-video"
        },
        {
            "title": "Automação Predial",
            "description": "Automação de portões, iluminação e áreas comuns.",
            "detalhes": "Controle remoto de dispositivos, agendamento de rotinas, sensores inteligentes e economia de energia para áreas comuns do condomínio.",
            "icon": "bi-building-check"
        },
        {
            "title": "Monitoramento de Áreas Comuns",
            "description": "Vigilância completa para a segurança dos moradores.",
            "detalhes": "Câmeras em pontos estratégicos, acesso remoto via app, gravação em nuvem e alertas em tempo real para a central de segurança.",
            "icon": "bi-camera-video-fill"
        }
    ]
    return render_template('condominios.html', services=services)

# NOVO: Rota para a página da Loja
@app.route('/loja')
def loja():
    return render_template('loja.html')

#ROTA PARA OS PRODUTOS#

@app.route('/cameras')
def cameras():
    return render_template('cameras.html')

@app.route('/alarmes')
def alarmes():
    return render_template('alarmes.html')

@app.route('/automacao')
def automacao():
    return  render_template('automcao.html')

@app.route('/kits')
def kits():
    return render_template('kits.html')











# Rota para a página de serviços
@app.route('/services')
def services():
    service_list = [
        {
            "title": "Segurança Eletrônica",
            "description": "Instalação e manutenção de câmeras, alarmes e cercas elétricas para a proteção de seu patrimônio.",
            "detalhes": "Oferecemos soluções completas com câmeras HD, sensores de movimento, alarmes integrados e cercas eletrificadas com monitoramento remoto.",
            "icon": "bi-shield-lock",
            "color": "text-success"
        },
        {
            "title": "Automação",
            "description": "Transformamos ambientes com sistemas inteligentes para controle de iluminação, clima e outros dispositivos.",
            "detalhes": "Controle por aplicativo, sensores de presença, agendamento de rotinas e integração com Alexa/Google Home.",
            "icon": "bi-house-door",
            "color": "text-primary"
        },
        {
            "title": "Controle de Acesso",
            "description": "Soluções modernas e seguras para gerenciar entrada e saída em condomínios e empresas.",
            "detalhes": "Biometria, QR Code, tags RFID, reconhecimento facial e integração com portaria remota.",
            "icon": "bi-person-badge",
            "color": "text-success"
        },
        {
            "title": "Monitoramento",
            "description": "Monitoramento 24h para garantir a segurança de seus bens.",
            "detalhes": "Central de vigilância com câmeras em tempo real, alertas automáticos e gravação em nuvem.",
            "icon": "bi-camera-video",
            "color": "text-success"
        },
        {
            "title": "Manutenção Preventiva",
            "description": "Manutenção programada para evitar falhas e prolongar a vida útil de seus equipamentos.",
            "detalhes": "Check-ups periódicos, limpeza de equipamentos, atualização de sistemas e suporte técnico.",
            "icon": "bi-tools",
            "color": "text-warning"
        },
        {
            "title": "Rede de Computadores",
            "description": "Infraestrutura completa para redes cabeadas e Wi-Fi, garantindo velocidade e estabilidade.",
            "detalhes": "Instalação de roteadores, switches, cabeamento estruturado, firewall e suporte remoto.",
            "icon": "bi-ethernet",
            "color": "text-purple"
        },
        {
            "title": "Interfonia",
            "description": "Sistemas de interfonia para comunicação eficiente em condomínios e empresas.",
            "detalhes": "Interfones digitais, vídeo porteiro, integração com controle de acesso e suporte técnico.",
            "icon": "bi-telephone",
            "color": "text-secondary"
        },
        {
            "title": "Informática",
            "description": "Suporte técnico e soluções de informática para empresas.",
            "detalhes": "Manutenção de computadores, instalação de softwares, backup, antivírus e consultoria técnica.",
            "icon": "bi-laptop",
            "color": "text-purple"
        },
        {
            "title": "Desenvolvimento de Sistemas",
            "description": "Sistemas sob medida para otimizar processos e aumentar a produtividade.",
            "detalhes": "Criação de sistemas web, aplicativos, dashboards, integração com banco de dados e automação de tarefas.",
            "icon": "bi-code-slash",
            "color": "text-orange"
        }
    ]
    return render_template('services.html', services=service_list)

# NOVA: Rota para a página de Soluções
@app.route('/solucoes')
def solucoes():
    return render_template('solucoes.html')

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