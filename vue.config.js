// const IS_PRODUCTION = process.env.NODE_ENV === 'production'

module.exports = {
  outputDir: 'dist',
  assetsDir: 'static',
  publicPath: process.env.NODE_ENV === 'production' ? '/neargreen-v2/' : '/',
  devServer: {
    proxy: {
      '/api*': {
        // Forward frontend dev server request for /api to django dev server
        target: 'http://localhost:8000/'
      }
    }
  }
}
