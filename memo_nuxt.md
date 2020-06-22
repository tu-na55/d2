
___
◎jsconfig.json
```json
{
  "compilerOptions": {
    "baseUrl": ".",
    "paths": {
      "~/*": ["./*"],
      "@/*": ["./*"],
      "~~/*": ["./*"],
      "@@/*": ["./*"]
    }
  },
  "exclude": ["node_modules", ".nuxt", "dist"]
}


```


■package.json
◎通常版
```json
  "scripts": {
    "lint": "eslint --ext .js,.vue src",
    "lint:fix": "eslint --fix --ext .js,.vue src"
  },
```

◎nuxtビルド時
```json
    "lint": "eslint --ext .js,.vue --ignore-path .gitignore ."

    "eslint": "^6.1.0",
    "eslint-config-prettier": "^6.10.0",
    "eslint-plugin-nuxt": ">=0.4.2",
    "eslint-plugin-prettier": "^3.1.2",
    "prettier": "^1.19.1"
```

```json
    // remove dev @nuxtjs/vuetify => dependencies: vuetify
  "dependencies": {
    "@nuxt/typescript-runtime": "^0.4.0",
    "@nuxtjs/auth": "^4.9.1",
    "@nuxtjs/axios": "^5.3.6",
    "@nuxtjs/dotenv": "^1.4.0",
    "@nuxtjs/pwa": "^3.0.0-0",
    "nuxt": "^2.0.0",
    "nuxt-property-decorator": "^2.7.2",
    // vuexいらない説
    "vuex": "^3.4.0"
  },
  body-parser connect-redis moment
  express express-session


  "devDependencies": {
    "@nuxt/typescript-build": "^0.6.0",
    "@nuxtjs/eslint-config-typescript": "^1.0.0",
    "@nuxtjs/eslint-module": "^1.0.0",

  }


★devまとめ
１：@nuxt/typescript-build @nuxtjs/eslint-config-typescript @nuxtjs/eslint-module
２：@nuxtjs/eslint-config 
３：eslint prettier eslint-config-prettier
４：eslint-config-standard 
// eslint-friendly-formatter
４：eslint-plugin-import eslint-plugin-node eslint-plugin-promise eslint-plugin-standard 
５：eslint-plugin-jest eslint-plugin-prettier eslint-plugin-vue eslint-plugin-nuxt
// eslint-loader eslint-plugin-html 

@vue/test-utils
babel-eslint browser-env
nodemon
```



◎eslintrc
vueでもreactでも基本的に同じ。大きな差はes、jsx、plugin、rulesぐらい。
※rulesは何も書かなくていい。

```js
module.exports = {  
    "env": {
        // "commonjs": true,
        "browser": true,
        // "node": true,
        "es6": true  
    },  
    "extends": [  
        "eslint:recommended",  
        "plugin:vue/essential"  
    ],  
    "globals": {  
        "Atomics": "readonly",  
        "SharedArrayBuffer": "readonly"  
    },  
    "parserOptions": {
      // "ecmaFeatures": {
      //   "jsx": true
      // },
        "ecmaVersion": 2018,  
        "sourceType": "module"  
    },  
    "plugins":
        // "react"  
        "vue"
    ],  
    "rules": {  
        // "no-console": "off",
        // "react/no-set-state": "error",
        // "react/prop-types": 0,
        // "semi": ["error", "always"]
    }  
}  
```

tsとprettierの設定を追加。
※他の設定もextendsする場合は、'plugin:prettier/recommended'が最後にくるように注意。
```js
  extends: [
    '@nuxtjs/eslint-config-typescript',
    'prettier',
    'prettier/vue',
    'plugin:prettier/recommended',
    'plugin:nuxt/recommended'
  ],
  plugins: [
    'prettier'
  ],
```

.prettierrc
```json
{
  "semi": false,
  "arrowParens": "always",
  "singleQuote": true
}
```


google版
「基本はGoogleに従いたいけど、JSDocはどうしても書きたくない。個人開発だから特別に許して」という場合。
```
module.exports = {
    env: {
        es6: true,
    },
    extends: ['google', 'plugin:prettier/recommended'], // 基本はGoogle様に従う
    rules: {
        'require-jsdoc': 'off', //Docコメントがなくても怒られないようにする
    },
};
```


___
npm i -D sequelize-cli sequelize mysql2

◎MariaDB
プラグイン：WorkBench、A5:SQL Mk-2

◎postgreSQL
$ yarn add sequelize
$ yarn add pg
$ yarn add pg-hstore

PostgREST
Graphile
___
@nuxtjs/dotenv


___

<!-- 自動化 -->
puppeteer：ヘッドレスブラウザと自動入力

<!-- 検索 -->
lodash-es
moment

___
├── @nuxtjs/axios@5.5.4
├── @nuxtjs/pwa@2.6.0
├── cross-env@5.2.0
├── express@4.17.1
├── forever@1.0.0

├── nodemon@1.19.1
├── nuxt@2.8.1
└── wikijs@5.5.0
___



```bash
# Mac用Node.js管理ツール
npm install -g n

# ただしWINでは使えないので、Node.js公式からLTSをインストール。
npm update npm
npm install -g yarn
# とりあえず全アップグレード
yarn upgrade-interactive --latest


yarn init -y
yarn global add create-nuxt-app
yarn create nuxt-app app
# yarn create nuxt-app client ./client

  To get started:
        cd app
        yarn dev

  To build & start for production:
        cd app
        yarn build
        yarn start


yarn add express


# 静的ファイルを生成する。
# yarn run generate
# GitHub Pages にデプロイする。
# yarn run deploy
```


```bash
# vue-cliでのビルド
yarn global add @vue/cli
yarn global list --depth=0



# vue create vue-cli-app
yarn create nuxt-app client ./client
# SSR, server-side: none
# pwa, axios, dotenv
# typescript, typescript-runtime
# eslint, prettier
cd client

# npxと同等
# yarn -s run [pkg]
yarn -s run dev

# 追加
yarn add vuex nuxt-property-decorator
# tsconfigの"experimentalDecorators": trueを確認

yarn add @nuxtjs/vuetify -D
# configのmodulesに追記

# JWT認証
@nuxtjs/auth

cd pages
mkdir content1
# edit index.vue, content1/index.vue, components
# 干渉するので、layoutsには何もいれないこと。
# configのaxiosにサーバを追記

yarn -s run dev
# yarn run dev --port=3001

# lint再実行
yarn run lint --fix
```






◎PWA
```bash
service-worker.js

if ('serviceWorker' in navigator) {
  window.addEventListener('load', () => {
    navigator.serviceWorker.register('service-worker.js')
    .then(registration => {
      console.log('Service Worker is registered', registration);
    })
    .catch(err => {
      console.error('Registration failed:', err);
    });
  });
}


  # workbox: {
  #   dev: true, //開発環境でもPWAできるように
  # },

  manifest: {
    name: 'nuxt-app',
    short_name: 'PWAサンプル',
    lang: 'ja',
    display: "standalone",
    start_url: "index.html"
  },

```

TS化
```ts
// Import時には拡張子まで指定するようにすればOK
import pkg from './package.json'
//////////

// クラスの定義が必要になるので少し冗長になります。
// なおnuxt.config.tsのsrcDirを設定している場合は、tsconfig.jsonのbaseUrlをそれに合わせないとコンポーネントの読み込みに失敗します。
<script lang="ts">
import { Component, Vue } from 'nuxt-property-decorator'

@Component
export default class Logo extends Vue {}
</script>
```
