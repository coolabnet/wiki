---
title: "Instalando LibreMesh no roteador Xiaomi MiWiFi 3"
layout: page
permalink: /instalando-libremesh-no-roteador-xiaomi-miwifi-3/
---

O Xiaomi MiWiFi é um dos poucos roteadores dual band que podem ser comprados no Brasil compatíveis com LibreMesh. No entanto a instalação deles é um pouco complicada. Nem o chef nem o cooker no momento geram imagens para ele, portanto as configurações locais têm que ser feitas na mão.

As versões de openwrt para esse roteador são baseadas nesse fork do lede aqui:

https://github.com/ptpt52/lede-source

Utilize esse fork se quiser compilar seu próprio firmware.

Aqui vão os passos:

- Siga essas instruções para obter acesso ssh/dropbear: https://wiki.openwrt.org/toh/xiaomi/mir3#to_get_sshdropbear_access (não esqueça de fazer downgrade do firmware antes)

- Pegue os arquivos do libremesh rootfs e kernel aqui:

https://mega.nz/file/RZ9ClLzQ#vK5KVRG-dAi1iJ-VxLaU74IEAxu3YpyKv9-fnM1CHTQ

https://mega.nz/file/IM10QB6Y#0U1muauXxq2Vynd6sq_WrBHOx6UvuclpYOW2G61IKjc

- Copie os arquivos via scp para o roteador:
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
