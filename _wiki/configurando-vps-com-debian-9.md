---
title: "Configurando VPS com Debian 9"
layout: page
permalink: /configurando-vps-com-debian-9/
---

Guia de configuração inicial (baseline) de uma VPS Debian/Ubuntu: atualização do sistema, fuso horário, sincronização de relógio, atualizações automáticas, hardening de kernel e swap.

## 1. Atualizar o sistema

```bash
apt update
apt full-upgrade -y
apt autoremove -y
apt autoclean -y
```

Depois, verifique se é necessário reiniciar (por exemplo, após atualização de kernel):

```bash
if [ -f /var/run/reboot-required ]; then reboot; fi
```

## 2. Fuso horário

```bash
timedatectl set-timezone America/Sao_Paulo
timedatectl
```

## 3. Sincronização de horário (chrony)

```bash
apt install -y chrony
systemctl enable --now chrony
systemctl status chrony
```

Se necessário, ajuste os servidores NTP em `/etc/chrony/chrony.conf`.

## 4. Atualizações automáticas de segurança

```bash
apt install -y unattended-upgrades apt-listchanges
dpkg-reconfigure -plow unattended-upgrades
```

Para reiniciar periodicamente após atualização de kernel, adicione ao cron — por exemplo, todo domingo às 3h30:

```cron
30 3 * * 0 root systemctl reboot
```

## 5. Hardening de kernel (sysctl)

Crie `/etc/sysctl.d/99-hardening.conf`:

```ini
kernel.kptr_restrict = 1
kernel.dmesg_restrict = 1
net.ipv4.conf.all.accept_redirects = 0
net.ipv4.conf.default.accept_redirects = 0
net.ipv6.conf.all.accept_redirects = 0
net.ipv6.conf.default.accept_redirects = 0
net.ipv4.tcp_syncookies = 1
net.ipv4.tcp_max_syn_backlog = 2048
net.ipv4.tcp_synack_retries = 2
net.ipv4.tcp_syn_retries = 5
vm.swappiness = 1
```

Aplique as configurações:

```bash
sysctl --system
```

## 6. Swap

```bash
fallocate -l 2G /swapfile   # ou: dd if=/dev/zero of=/swapfile bs=1M count=2048
chmod 600 /swapfile
mkswap /swapfile
swapon /swapfile
echo '/swapfile none swap sw 0 0' >> /etc/fstab
```

## 7. SSH: não propagar variáveis de locale

Comente a linha `SendEnv LANG LC_*` em `/etc/ssh/ssh_config` para evitar avisos de locale ao conectar:

```bash
sed -i -E 's/^[[:space:]]*SendEnv[[:space:]]+LANG[[:space:]]+LC_\*/#&/' /etc/ssh/ssh_config
```

## 8. Opcional: MOTD e dotfiles

- Use `figlet` para gerar um banner no login (`/etc/motd`).
- Personalize `.bashrc` e `.bash_aliases` em `/root` e `/etc/skel` para aplicar a novos usuários.
