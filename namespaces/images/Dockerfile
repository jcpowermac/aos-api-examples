FROM fedora

RUN dnf -y install nginx 
RUN echo "export NGINXSUM=$(sha256sum /usr/sbin/nginx | head -c 64)" >> /etc/profile.d/nginx.sh

CMD ["nginx", "-g", "daemon off;"]
