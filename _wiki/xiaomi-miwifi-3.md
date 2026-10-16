---
title: "Xiaomi MiWiFi 3"
layout: page
permalink: /xiaomi-miwifi-3/
---

O Xiaomi MiWiFi é um dos poucos roteadores dual band que podem ser comprados no Brasil compatíveis com LibreMesh. No entanto a instalação deles é um pouco complicada. Nem o chef nem o cooker no momento geram imagens para ele, portanto as configurações locais têm que ser feitas na mão.

Aqui vão os passos:

- Siga essas instruções para obter acesso ssh/dropbear: https://wiki.openwrt.org/toh/xiaomi/mir3#to_get_sshdropbear_access (não esqueça de fazer downgrade do firmware antes)

- Pegue os arquivos do libremesh rootfs e kernel aqui:
https://mega.nz/#!8A9CUJLQ!gJNC3SfwDdmMZ4y9BXlWp4mcn1FTAU3vWgsVYK2vW4w
https://mega.nz/#!1QdkxKgb!7htQD4bE9AbYotPkEQYriI5zF2LDe27A62h7S2tq9VM

- Copie os arquivos vis scp para o roteador:
```

scp lede-ramips-mt7620nand-miwifi-r3-squashfs-kernel1.bin   root@192.168.15.1:/tmp/
scp lede-ramips-mt7620nand-miwifi-r3-squashfs-rootfs0.bin   root@192.168.15.1:/tmp/
```
- Entre por ssh:
```
ssh root@192.168.15.1
```

- Dê os seguintes comandos (copiados da instruções do Chen [https://github.com/ptpt52/lede-source/issues/1](https://github.com/ptpt52/lede-source/issues/1))
```

nvram set flag_last_success=1
nvram set boot_wait=on
nvram set uart_en=1
nvram commit
mtd write /tmp/lede-ramips-mt7620nand-miwifi-r3-squashfs-kernel1.bin kernel1
mtd write /tmp/lede-ramips-mt7620nand-miwifi-r3-squashfs-rootfs0.bin rootfs0
reboot
```

E isso é tudo!
Caso você já tenha instalado o openwrt/lede por algum motivo no roteador, use o arquivo para sysupgrade:

https://mega.nz/#!tV0EzJZD!XblvULWZgjvx0d9RqdwJYbKkZOKTeHT-J6oBRQYw0Ls

E use o comando sysupgrade dentro do roteador para atualizar o sistema
