# heranca-em-bitcoin [Versão Linux]
Este programa manda e-mails automáticos depois de um certo tempo de inatividade. Pode fazer publicações no Nostr também.

## Pra usá-lo primeiro você deve seguir os seguintes passos:
1) Permitir que o aplicativo envie emails através do GMAIL. Siga o artigo abaixo para mais informações:
https://support.google.com/accounts/answer/185833?visit_id=638455376385662495-127977219&p=InvalidSecondFactor&rd=1
2) Baixar e configurar o GM Bot do Nostr conforme o tutorial abaixo:
https://dergigi.com/2023/01/19/how-to-build-a-nostr-gm-bot/
3) Configurar o arquivo config.json com a senha de acesso ao gmail (passo 1) e todas as senhas dos arquivos enviados para a pessoa que vai receber a herança

## Como funciona
Primeiro você vai criar três arquivos protegidos por senhas: Testamento, Seeds e Passphrase e vai enviar para a pessoa que vai receber a herança, porém sem revelar as senhas. As senhas serão enviadas no e-mail da pessoa configurado no config.json. É muito importante que a pessoa que recebeu os arquivos não saiba que você baixou esse programa.

# Observação: Jamais publique senhas ou dados sensiveis no Nostr.

Depois de baixar e configurar o programa com os passos de 1 a 3, abra um terminar e execute: python3 bkg_run.py isso fará com que o programa rode em um loop infinito. Não feche esse terminal, apenas minimize, pois ele é crucial pra o funcionamento do programa. Alternativamente você pode criar um cronjob e rodar um script que execute python3 IsManAlive.py

Para registrar que você está vivo abra outro terminal e execute hit_me.sh. Basta você executar esse script uma vez por dia e o programa entenderá que você está vivo.

### Se você não executar o script hit_me.sh as seguintes ações ocorrerão:

* Entre 2 e 29 dias:
Você recebe um lembrete no seu email e no Nostr que está sem bater o ponto a tantos dias &nbsp;
* Entre 30 e 89 dias:
A pessoa que estiver com o email configurado no config.json receberá o email com a mensagem que deve conter a senha para abrir o arquivo do Testamento
* Entre 90 e 179 dias:
A pessoa que estiver com o email configurado no config.json receberá o email com a mensagem que deve conter a senha para abrir o arquivo das Seeds
* Entre 180 e 359 dias:
A pessoa que estiver com o email configurado no config.json receberá o email com a mensagem que deve conter a senha para abrir o arquivo da Passprhase &nbsp;
