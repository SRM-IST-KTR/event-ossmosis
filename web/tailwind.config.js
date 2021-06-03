module.exports = {
  purge: ["./index.html", "./src/**/*.{vue,js,ts,jsx,tsx}"],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {
      minHeight: {
        detailBox: "30em",
        "80-screen": "80vh",
      },
      fontSize: {
        xxs: "0.5rem",
      },
    },
  },
  variants: {
    extend: {},
  },
  plugins: [],
};
