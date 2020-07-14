
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


// andys2018-depencies
    "express": "^4.16.3",

    "nuxt": "^2.12.2",
    "nuxt-composition-api": "^0.5.0",
    "@nuxtjs/pwa": "^2.6.0",

    "@nuxtjs/feed": "^0.2.0",
    "@nuxtjs/sitemap": "^0.1.1",
    "@nuxtjs/google-analytics": "^2.0.2",

    "@nuxtjs/sentry": "^2.0.0",
    "@sentry/webpack-plugin": "^1.6.2",

    "contentful": "^7.0.5",

    "cross-env": "^5.2.0",
    "dotenv": "^6.1.0",

    "dayjs": "^1.7.7",
    "marked": "^0.5.1",
    "prismjs": "^1.15.0",
    "vue-lazyload": "^1.2.6"

// andys2018-dev
    "@nuxt/typescript-build": "^0.6.6",
    "babel-runtime": "^6.26.0",


    "nodemon": "^1.18.7",
    "npm-run-all": "^4.1.5",
    "bundlewatch": "^0.2.5",


    "typescript": "^3.8.3",
    "ts-loader": "^7.0.3",
    "@types/node": "^13.13.2",

    "prettier": "1.14.3",
    "prettier-stylelint": "^0.4.2",
    "eslint-config-prettier": "^3.1.0",
    "eslint-plugin-prettier": "2.6.2",


    "jest": "^26.0.1",
    "@types/jest": "^25.2.1",
    "ts-jest": "^25.4.0",


    "babel-eslint": "^8.2.1",
    "eslint": "^5.0.1",
    "eslint-config-typescript": "^1.1.0",
    "eslint-plugin-typescript": "^0.13.0",
    "typescript-eslint-parser": "^21.0.1"
    "eslint-plugin-vue": "^4.0.0",




    "stylelint": "^9.8.0",
    "stylelint-config-rational-order": "^0.0.2",
    "stylelint-config-recommended": "^2.1.0",

    "fork-ts-checker-webpack-plugin": "^0.5.0",
    "husky": "^1.1.4",
    "lint-staged": "^8.0.5",

    "lighthouse": "^5.6.0",

    "@types/prismjs": "^1.9.0",
    "@types/marked": "^0.4.2",


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
# npm ls -g --depth=0

npm install -g yarn
# とりあえず全アップグレード
yarn upgrade-interactive --latest

yarn init -y
yarn global add create-nuxt-app
yarn create nuxt-app app
# yarn create nuxt-app client ./client
# yarn global list --depth=0


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

##########
# 設定ファイルとsrcを分離
mkdir src
mv assets components layouts middleware pages plugins static store ./src

# nuxt.config.jsに追加
  srcDir: 'src',
# webpack.config.js作成
  '~': path.resolve(rootPath, '/src'),
  '@': path.resolve(rootPath, '/src'),
# jsconfig.jsonを修正
  "~/*": ["./src/*"],
  "@/*": ["./src/*"],
# tsconfig.jsonを修正
  "~/*": ["src/*"],
  "@/*": ["src/*"]
##########


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

```bash
# jest
yarn add -D jest ts-jest vue-jest @vue/test-utils @types/jest
yarn add -D babel-jest babel-core babel-preset-env

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
