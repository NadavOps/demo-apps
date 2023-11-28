FROM nginx:1.23.3-alpine

COPY index.html /
ENV BACKGROUND_COLOR=white
ENV MESSAGE="─=≡Σ((( つ＞＜)つ"

CMD ["/bin/sh" , "-c" , "envsubst < /index.html > /usr/share/nginx/html/index.html && exec nginx -g 'daemon off;'"]
