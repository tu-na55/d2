# FROM node:latest
FROM node:12.5.0-alpine

ENV LANG=C.UTF-8
ENV TZ=Asia/Tokyo

# 本番環境では production
# ENV NODE_ENV=development

# ENV HOME="/app"
# WORKDIR ${HOME}

ADD . /app
WORKDIR /app

# RUN mkdir -p /usr/src/app
# WORKDIR /usr/src/app

RUN apk update && \
    apk upgrade && \
    npm install -g npm && \
    npm install -g @vue/cli

    # apk add git

# RUN npm install -g npm && \
#     npm install -g core-js@latest && \
#     npm install -g @vue/cli && \
#     npm install -g @vue/cli-init && \
#     npm install -g nuxt create-nuxt-app


# RUN npm install yarn
# RUN yarn

# RUN yarn install
# RUN yarn add @nuxtjs/axios

ENV HOST 0.0.0.0
EXPOSE 3000
