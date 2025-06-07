<h1>🧠 Automação de Login - Plataforma Alura</h1>

  <p>Este projeto tem como objetivo demonstrar o uso de <strong>automação com Selenium</strong> integrada com <strong>interfaces gráficas em Python</strong>, utilizando a biblioteca <code>customtkinter</code>. A aplicação coleta as credenciais do usuário por meio de uma interface gráfica e realiza o login automaticamente no portal da <a href="https://cursos.alura.com.br" target="_blank">Alura</a>.</p>

  <h2>📌 Funcionalidades</h2>
  <ul>
    <li>Interface moderna para coleta de usuário e senha</li>
    <li>Automatização do login na plataforma Alura via Selenium</li>
    <li>Organização modular com arquivos separados por responsabilidade</li>
    <li>Instalação automática do driver do Chrome</li>
  </ul>

  <h2>🚀 Tecnologias utilizadas</h2>
  <ul>
    <li>Python 3.10+</li>
    <li><a href="https://github.com/TomSchimansky/CustomTkinter" target="_blank">CustomTkinter</a></li>
    <li><a href="https://www.selenium.dev/" target="_blank">Selenium</a></li>
    <li><a href="https://pypi.org/project/webdriver-manager/" target="_blank">WebDriver Manager</a></li>
  </ul>

  <h2>🗂 Estrutura do Projeto</h2>
  <pre>
main.py
login/
├── receber_dados.py     # Interface gráfica
└── login_alura.py       # Automação de login
  </pre>

  <h2>⚙️ Como executar</h2>
  <ol>
    <li><strong>Clone o repositório</strong>
      <pre><code>git clone https://github.com/seu-usuario/nome-do-repositorio.git
cd nome-do-repositorio</code></pre>
    </li>
    <li><strong>(Opcional) Crie e ative um ambiente virtual</strong>
      <pre><code>python -m venv venv
source venv/bin/activate    # Linux/Mac
.\venv\Scripts\activate     # Windows</code></pre>
    </li>
    <li><strong>Instale as dependências</strong>
      <pre><code>pip install -r requirements.txt</code></pre>
      Ou manualmente:
      <pre><code>pip install selenium customtkinter webdriver-manager</code></pre>
    </li>
    <li><strong>Execute o script</strong>
      <pre><code>python main.py</code></pre>
    </li>
  </ol>

  <h2>✅ Pré-requisitos</h2>
  <ul>
    <li>Python instalado</li>
    <li>Google Chrome atualizado</li>
  </ul>

  <h2>🧠 Créditos e Observações</h2>
  <p>Este projeto foi desenvolvido para fins educacionais e demonstração de integração entre interfaces gráficas e automação web. As credenciais informadas são processadas localmente e <strong>não são armazenadas</strong>.</p>

  <h2>📌 Aviso Legal</h2>
  <p>Este projeto não é afiliado oficialmente à plataforma Alura. O uso deve respeitar os <a href="https://www.alura.com.br/termos-de-uso" target="_blank">termos de uso da Alura</a>.</p>

  <h2>📬 Contato</h2>
  <p>Feito com 💡 por <strong>Juan Frois</strong><br>
  🔗 <a href="https://www.linkedin.com/in/juan-frois" target="_blank">linkedin.com/in/juan-frois</a></p>

</body>
</html>
