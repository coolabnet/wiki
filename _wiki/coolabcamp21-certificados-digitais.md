---
title: "CoolabCamp21 Certificados Digitais"
layout: page
permalink: /coolabcamp21-certificados-digitais/
---

Sábado, 03/04/21, 14:00 Facilitador: @fernaovellozo

- A tecnologia utilizada para produzir certificados que utilizamos nessas infraestruturas é a mesma utilizada para eCPF/eCNPJ, mas há muito pouco suporte para formatos não-proprietários (PFX vs PEM)
- Burocracias centralizadoras
- Cartórios da Internet
- Referências:
   - RFC5280 https://tools.ietf.org/html/rfc5280
   - https://cabforum.org/
   - PFX: Como não se deve fazer um padrão/protocolo de critpografia https://www.cs.auckland.ac.nz/~pgut001/pubs/pfx.html
   - Legislação no Brasil (não relacionada às AC's de domínios na Internet):
       - http://www.planalto.gov.br/ccivil_03/mpv/antigas_2001/2200-2.htm
       - https://www.gov.br/iti/pt-br/acesso-a-informacao/perguntas-frequentes/icp-brasil
- PFX:
   - Padrão de arquivos para autoridades certificadoras (feito pela Microsoft)
   - Chaves públicas e privadas (criptografia assimétrica)
   - PEM: formato aberto para chaves assimétricas
   - Certificados emitidos por empresas privadas
       - Cobram por cada subdomínio (uma linha a mais em um arquivo)
       - Modelo de negócio problemático
           - Autoridades certificadores sendo hackeadas
               - Outras notícias
               - Infraestrutura de chaves públicas da symantec [colocar referência]
                   - Hackers iranianos emitindo certificados para google.com
           - Mozilla e Google, Cloudfare e letsencrpy fizeram uma parceria para lidar com autoridades certificadoras
               - https, página vai para o topo da pesquisa do google

             LetsEncrypt - autoridade certificadora aberta
                 https://letsencrypt.org/pt-br/

Dica de boa prática:
- Proteção da chave privada
- Qualquer aplicação que sirva https diretamente precisa ter acesso à chave privada.
- Por isso, pode ser bom limitar o acesso à chave privada a um número menor de aplicações mais robustas/seguras.
- Por exemplo: usar wildcard somente quando houver um proxy reverso (ex: Nginx).
- Para aplicaçoes que escutam HTTPS diretamente, preferir usar certificados para domínios específicos (sem ser wildcard).
- Para guardar a chave privada: criar uma partição criptografada
- Manter lista de certificados revogados
    - Tabelão de 3 megas para ver se 1 certificado está valido ou não
    - Nunca foi devidamente implementada
    - OCSP: protocolo para contornar a situação (https://pt.wikipedia.org/wiki/Protocolo_de_status_de_certificado_online_(OCSP))
        - Outros problemas: difícil de implementar
        - Problema de segurança
        - Problema de carga
    - OCSP stapling (https://en.wikipedia.org/wiki/OCSP_stapling)
        - Atual padrão para verificação de revogação de certificados

- Certbot cliente para instalar no servidor:
    - Disponível para vários proxys
        - Apache
        - Nginx
        - Protocolo ACME

        wildcard: requer verificações a mais para ser seguro
            provar que o dominio é seu criando: http challenge
            gera string automaticamente
            (reload na configuração pois o ngix pode estar usando certificado antigo)

        X509 Extensions:

Rede de confiança de assinatura de chaves (OpenPGP: https://www.openpgp.org/)
    multiplas pessoas assinam uma chave falando que é confiável

Trilema: é difícil de garantir as seguintes 3 coisas ao mesmo tempo:
- humanamente compreensivel
- seguro
- descentralizado

https://en.wikipedia.org/wiki/Zooko%27s_triangle

Gestão de certificados em máquinas linux
CFSSL -> cloudflare
Step CA

Imagens docker:

https://github.com/nginx-proxy/acme-companion
https://github.com/nginx-proxy/docker-letsencrypt-nginx-proxy-companion
