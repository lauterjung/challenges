# warren-challenges
Nome: Miguel Busarello Lauterjung  

Por favor leia esse documento até o final, pois possui considerações importantes sobre o código. A linguagem escolhida foi Python versão 3.10. De acordo com a documentação (PEP-8), é recomendado o uso de snake_case na maioria das atribuições.
Para rodar os arquivos, é necessário instalar o Python, acessando o seguinte site e escolhendo o instalador conforme seu sistema operacional:  
https://www.python.org/downloads/  
Os arquivos .py contendo a resolução de cada desafio estão dentro das suas respectivas pastas.

# Como rodar o código
1) Terminal  
Informe o caminho completo do arquivo python.exe instalado no seu computador, e em seguida o caminho completo para o arquivo .py. Exemplo:  
C:/Users/User/AppData/Local/Programs/Python/Python310/python.exe c:/Users/User/warren-challenges/desafio_1/desafio_01.py  
  
Se o Python estiver adicionado na variável de ambiente do sistema PATH, é possível substituir o seu caminho completo por "py". Exemplo:  
py c:/Users/User/warren-challenges/desafio_1/desafio_01.py

2) Usando a IDE IDLE  
Essa IDE vem junto com a instalação do Python. Após abrir a IDLE Shell:
- Selecione File > Open;
- Selecione o arquivo .py do respectivo desafio;
- Na nova janela que abrir, selecione Run > Run Module.

3) Internet  
Em últimos casos, se não conseguir rodar no seu computador, é possível utilizar um interpretador Python online (ex.: https://www.online-python.com/). Copie e cole o código contido dentro dos arquivos .py na janela "main.py" do site, e clique no botão verde "Run".

# Desafio 1
O enunciado possui informações conflitantes:  
a) "[...] a soma de n + reverso(n) resultam em números ímpares [...]" não possui "120 números reversíveis abaixo de 1000" com essa propriedade, mas sim 440.  
b) Para que "120 números reversíveis abaixo de 1000". com essa propriedade existam, o enunciado deveria ser "[...] a soma de n + reverso(n) resultam em números [COM APENAS DÍGITOS] ímpares [...]".  

Um exemplo é o número 102 que, somado com seu reverso 201, também resulta em um número ímpar (303), mas que contém um dígito par (0). Tal número é contado considerando o enunciado a), mas não no enunciado b).  
  
Portanto, foram geradas duas soluções:
- desafio_01a.py, 
- desafio_01b.py
Para melhor visualização do resultado, são gerados os arquivos "output_01a.txt" e "output_01b.txt" no final da execução.

# Desafio 2
Dois algoritmos de resolução foram propostos:
- loop
- sorted list
  
O desempenho entre eles depende:
- Se a lista já vem ordenada;
- Do tamanho da lista (n);
- Do limite de alunos (x);
  
No geral o sorted list possui menor variância e um código mais limpo. Por esse motivo ele foi escolhido para a versão final do programa.

# Desafio 3
Foi usado uma implementação que trabalha similar a um gerador. Para resultados acima de 15 números, o resultado demora um pouco, mas o computador não irá travar.