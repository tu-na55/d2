import { Configuration } from '@nuxt/types'

// nuxt.config.ts
// export default {}
const config: Configuration = {
  mode: 'universal',
  // mode: 'spa',

  // router: {
  //   base: '/nuxt-app/'
  // },

  // .envに書いた方がいい？
  // server: {
  //   port: 3000,
  //   host: '0.0.0.0',
  // },

  /*
   ** Headers of the page
   */
  head: {
    // base: {
    //   href: 'router.base'
    // },

    title: process.env.npm_package_name || '',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      {
        hid: 'description',
        name: 'description',
        content: process.env.npm_package_description || ''
      }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' },
      // add google font
      // { rel: 'stylesheet', href: 'https://fonts.googleapis.com/css?family=Roboto:300,400,500,700|Material+Icons' }
  ]
  },
  /*
   ** Customize the progress-bar color
   */
  loading: { color: '#fff' },

  /*
   ** Global CSS
   */
  css: [
    // add style
    // '~/assets/style/app.styl'

    // add ページ推移時のトランジション
    '~/assets/css/transitions.css'
  ],

  /*
   ** Plugins to load before mounting the App
   */
  plugins: [
    // 設置済みの場合：pulugin/[mod].js
    // '~/plugins/vuetify.js',
    // '~/plugins/axios'

    // プッシュ通知用
    // { src: '~/plugins/axios.js', ssr: false }
    // { src: '~plugins/PushNotification.js', ssr: false }
  ],

  /*
   ** Nuxt.js dev-modules
   */
  buildModules: [
    '@nuxt/typescript-build',
    // '@nuxtjs/vuetify'
  ],
  /*
   ** Nuxt.js modules
   */
  modules: [
    // Doc: https://axios.nuxtjs.org/usage
    '@nuxtjs/axios',
    '@nuxtjs/auth',
    '@nuxtjs/pwa',
    // ['@nuxtjs/pwa', { icon: false }],

    // Doc: https://github.com/nuxt-community/dotenv-module
    '@nuxtjs/dotenv',
    // [
    //   '@nuxtjs/dotenv',
    //   { filename: process.env.NODE_ENV !== 'production' ? ".env.dev" : ".env.prod" }
    // ]

    '@nuxtjs/eslint-module'
  ],

  // 参考
  // auth: {
  //   fetchUserOnLogin: true,
  //   strategies: {
  //     local: {
  //       endpoints: {
  //         login: { url: '/api/auth/token/create/', method: 'post', propertyName: 'auth_token' },
  //         logout: { url: '/api/auth/token/destroy/', method: 'post' },
  //         user: { url: '/api/auth/me/', propertyName: false },
  //       },
  //       tokenType: 'Token',
  //       tokenName: 'Authorization'
  //     }
  //   },
  //   redirect: {
  //     login: '/',
  //     home: '/'
  //   }
  // },

  // 参考
  // toast: {
  //   position: 'center',
  //   theme: 'bubble'
  // },

  pwa: {
    workbox: {
      // キャッシュの設定
      // dev: true, //開発環境でもPWAできるように
      swDest: 'static/sw.js',
    },
    manifest: {
      name: 'nuxt-app',
      short_name: 'nuxt-PWA',
      lang: 'ja',
      display: 'standalone',
      start_url: 'index.html',
      // start_url: '/?mode=pwa',   // アイコンから起動した時のURL

      // プッシュ通知用
      // gcm_sender_id: 'XXX',  // Push7の設定を追記
      // gcm_user_visible_only: true,     // Push7の設定を追記

      theme_color: '#ff4a93',    // アプリケーションの既定のテーマ色を定義
      background_color: '#ffdce6',  // 背景の色
      // icons: [
      //   {
      //     src: '/icon.png',
      //     sizes: '512x512',
      //     type: 'image/png'
      //   }
    },
  },


  /*
   ** Axios module configuration
   ** See https://axios.nuxtjs.org/options
   */
  axios: {
    baseURL: "http://localhost:8000/api"
    // baseURL: "http://127.0.0.1:49588/api"

    // baseURL: 'http://django:8000',
    // browserBaseURL: 'http://localhost:8000'
  },
  /*
   ** Build configuration
   */
  build: {
    /*
     ** You can extend webpack config here
     */
    // 参考
    // publicPath: '/assets/',

    // 参考
    // extractCSS: true,

    extend(config, ctx) {



      if (ctx.isDev && ctx.isClient) {
      // 参考
      // chrome devtool用に追加
      //   config.devtool = 'inline-cheap-module-source-map'

      /*
      ** Run ESLint on save
      */
        // add
        if (!config.module) return
      // eslintは共通の書き方
        config.module.rules.push({
          enforce: 'pre',
          // test: /\.(js|vue)$/,
          test: /\.(js|ts|vue)$/,
          loader: 'eslint-loader',
          exclude: /(node_modules)/
        })
      }
    }
  },
  // if nuxt.config.ts
  // typescript: {
  //   typeCheck: {
  //     eslint: true
  //   }
  // }
}

// if nuxt.config.ts
export default config
