module.exports = {
  purge: ["./index.html", "./src/**/*.{vue,js,ts,jsx,tsx}"],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {
      minHeight: {
        'detailBox': '25em',
       }
    },
    
  },
  variants: {
    extend: {},
  },
  plugins: [],
};
