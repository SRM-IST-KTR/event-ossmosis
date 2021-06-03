module.exports = {
  publicPath: process.env.NODE_ENV === "production" ? "./" : "/",
  devServer: {
    proxy: {
      "^/api": {
        target: `http://localhost:${process.env.API_PORT}`,
      },
    },
    disableHostCheck: true,
  },
};
