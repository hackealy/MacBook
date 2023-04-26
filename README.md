Inicie o servidor de escuta em seu ambiente controlado em outra máquina ou em uma VM. Por exemplo, você pode usar o netcat (nc) para ouvir a porta 4444:

 # nc -lvp 4444

Execute o arquivo de script no seu Macbook digitando o seguinte comando no terminal:

 # python reverseshell.py
 
Após a execução do arquivo de script, você deve ver uma conexão estabelecida no servidor de escuta. Agora você pode enviar comandos do servidor para o seu Macbook e obter a saída dos comandos executados no seu terminal.

Para executar o código, você precisará ter o Python 3 instalado em seu Macbook. Se você não tiver o Python 3 instalado, pode baixá-lo do site oficial do Python (https://www.python.org/downloads/
