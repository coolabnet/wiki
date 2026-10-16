---
title: "Archer C5 OpenWRT e firmware de fabrica"
layout: page
permalink: /archer-c5-openwrt-e-firmware-de-fabrica/
---

Partindo de um roteador com LibreMesh com problemas no ambiente gráfico, começamos com a questão de devolver a firmware original diretamente ou tentar fazer o caminho de instalação via openwrt?

Nesse caso, como o ambiente gráfico não está funcionando vamos mudar o sistema LibreMesh para um Openwrt “puro” e depois para o original, alterando a firmware (corte do setor de boot)

O link para a firmware pode ser acessado direto [aqui](https://static.tp-link.com/res/down/soft/Archer_C5_V1.20_150428.zip), e para a pagina dela que mostra que a ultima versao é de 2015 [aqui](https://www.tp-link.com/en/support/download/archer-c5/v1.20/#Firmware).

`Atenção: Siga esses passos por usa conta e risco!`

    Começamos acessando o router por shell:

     # ssh root@10.13.0.1 -v

    Depois partindo da pasta onde foi salvo o openwrt para o modelo que baixamos:

     # scp openwrt-18.06.2-ar71xx-generic-archer-c5-v1-squashfs-sysupgrade.bin root@10.13.0.1:/tmp
    openwrt-18.06.2-ar71xx-generic-archer-c
    100% 3968KB 734.9KB/s   00:05
</code>
    Agora voltando ao router:
`# cd /tmp/`
    Executamos o procedimento de sysupgrade:
`root@LiMe-56b747:/tmp# sysupgrade openwrt-18.06.2-ar71xx-generic-archer-c5
    -v1-squashfs-sysupgrade.bin
    Image metadata not found
    Use sysupgrade -F to override this check when downgrading or flashing to vendor firmware
    Image check 'fwtool_check_image' failed.
    root@LiMe-56b747:/tmp#
    root@LiMe-56b747:/tmp# sysupgrade -F openwrt-18.06.2-ar71xx-generic-archer
    -c5-v1-squashfs-sysupgrade.bin
    Image metadata not found
    Image check 'fwtool_check_image' failed but --force given - will update anyway!
    Saving config files...
    Commencing upgrade. Closing all shell sessions.
    debug1: channel 0: free: client-session, nchannels 1
    Connection to 10.13.183.71 closed by remote host.
    Connection to 10.13.183.71 closed.
    Transferred: sent 5488, received 8560 bytes, in 339.8 seconds
    Bytes per second: sent 16.1, received 25.2
    debug1: Exit status -1`
    se tudo deu certo, agora devemos ter um servidor dhcp iniciando no roteador, mas no meu caso não foi…. vamos ao safe outra vez… e na segunda vez repetindo a gravação, lembrei de ter esquecido de mandar apagar as configs antigas no comando sysupgrade, usando a opção -n
`# sysupgrade -n -F openwrt-18.06.2-ar71xx-generic-archer-c5
    -v1-squashfs-sysupgrade.bin`
    E se tudo deu certo, estamos prontos para iniciar o roteador e acessar ele por cabo conectado e pelo ip 192.168.1.1
`<code>ping 192.168.1.1`
</code>
    Agora com o firmware de antes OEM vamos cortar os primeiros 0x20200 (que são 131,584 = 257512) Bytes do firmware original (1512 Vendor-info + 256*512 U-Boot):
`dd if=ArcherC5v1_en_3_14_3_up_boot\(150428\).bin of=tplink.bin skip=257 bs=512
    31744+0 registros de entrada
    31744+0 registros de saída
    16252928 bytes (16 MB, 16 MiB) copiados, 0,116377 s, 140 MB/s`
    Agora podemos fazer a gravação direto pela interface da Luci em system - firmware ou usando o shell:

`scp tplink.bin root@192.168.1.1:/tmp/`

    Conectar no router:

`ssh root@192.168.1.1 -v`

    Agora ir a pasta tmp e rodar o procedimento mais seguro que é o sysupgrade

`sysupgrade /tmp/tplink.bin`

    Ou menos aconselhado, mas eficiente mtd:

`mtd -r write /tmp/tplink.bin firmware`

E se tudo deu certo, voltamos a ter um roteador com a firmware de fábrica!

**Happy Downgrading!!**
